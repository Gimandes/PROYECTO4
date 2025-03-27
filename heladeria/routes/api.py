from flask import Blueprint, jsonify, request
from heladeria.config.db import db
from heladeria.models.producto import Producto
from heladeria.models.ingrediente import Ingrediente

api = Blueprint('api', __name__)

# 🔹 Consultar todos los productos
@api.route('/productos', methods=['GET'])
def get_productos():
    productos = Producto.query.all()
    return jsonify([{"id": p.productoID, "nombre": p.tipo_producto, "precio": p.precio_producto} for p in productos])

# 🔹 Consultar un producto según su ID
@api.route('/productos/<int:id>', methods=['GET'])
def get_producto_by_id(id):
    producto = Producto.query.get(id)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify({"id": producto.productoID, "nombre": producto.tipo_producto, "precio": producto.precio_producto})

# 🔹 Consultar un producto según su nombre
@api.route('/productos/nombre/<string:nombre>', methods=['GET'])
def get_producto_by_nombre(nombre):
    producto = Producto.query.filter_by(tipo_producto=nombre).first()
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify({"id": producto.productoID, "nombre": producto.tipo_producto, "precio": producto.precio_producto})

# 🔹 Consultar calorías de un producto
@api.route('/productos/<int:id>/calorias', methods=['GET'])
def get_calorias_producto(id):
    producto = Producto.query.get(id)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify({"id": producto.productoID, "calorias": producto.total_calorias})

# 🔹 Consultar rentabilidad de un producto
@api.route('/productos/<int:id>/rentabilidad', methods=['GET'])
def get_rentabilidad_producto(id):
    producto = Producto.query.get(id)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify({"id": producto.productoID, "rentabilidad": producto.rentabilidad})

# 🔹 Consultar el costo de producción
@api.route('/productos/<int:id>/costo', methods=['GET'])
def get_costo_producto(id):
    producto = Producto.query.get(id)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify({"id": producto.productoID, "costo_produccion": producto.precio})

# 🔹 Vender un producto
@api.route('/productos/<int:id>/vender', methods=['POST'])
def vender_producto(id):
    producto = Producto.query.get(id)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify({"mensaje": f"Producto {producto.tipo_producto} vendido con éxito."})

# 🔹 Consultar todos los ingredientes
@api.route('/ingredientes', methods=['GET'])
def get_ingredientes():
    ingredientes = Ingrediente.query.all()
    return jsonify([{"id": i.ingredienteID, "nombre": i.nombre, "inventario": i.inventario} for i in ingredientes])

# 🔹 Consultar un ingrediente por ID
@api.route('/ingredientes/<int:id>', methods=['GET'])
def get_ingrediente_by_id(id):
    ingrediente = Ingrediente.query.get(id)
    if not ingrediente:
        return jsonify({"error": "Ingrediente no encontrado"}), 404
    return jsonify({"id": ingrediente.ingredienteID, "nombre": ingrediente.nombre, "inventario": ingrediente.inventario})

# 🔹 Consultar si un ingrediente es saludable
@api.route('/ingredientes/<int:id>/saludable', methods=['GET'])
def get_ingrediente_saludable(id):
    ingrediente = Ingrediente.query.get(id)
    if not ingrediente:
        return jsonify({"error": "Ingrediente no encontrado"}), 404
    return jsonify({"id": ingrediente.ingredienteID, "es_saludable": ingrediente.es_saludable})

# 🔹 Reabastecer un ingrediente
@api.route('/ingredientes/<int:id>/reabastecer', methods=['POST'])
def reabastecer_ingrediente(id):
    data = request.json
    cantidad = data.get("cantidad", 0)
    
    ingrediente = Ingrediente.query.get(id)
    if not ingrediente:
        return jsonify({"error": "Ingrediente no encontrado"}), 404
    
    ingrediente.inventario += cantidad
    db.session.commit()
    
    return jsonify({"mensaje": f"Ingrediente {ingrediente.nombre} reabastecido con éxito."})
