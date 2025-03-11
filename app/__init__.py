from flask import Flask, render_template
from config.config import Config
from config.db import db
from models.ingrediente import Ingrediente
from models.producto import Producto

app = Flask(__name__, template_folder="templates")
app.config.from_object(Config)
db.init_app(app)

@app.route("/")
def home():
    return render_template("index.html") 

@app.route("/vender")
def mostrar_vender():
    return render_template("vender.html") 

@app.route("/ingredientes")
def mostrar_ingredientes():
    ingredientes = Ingrediente.query.all()
    return render_template("ingredientes.html", ingredientes=ingredientes)

@app.route("/productos")
def mostrar_productos():
    productos = Producto.query.all()
    return render_template("productos.html", productos=productos)

def vender(nombre_producto):
    producto = Producto.query.filter_by(nombre=nombre_producto).first()
    if not producto:
        return f"¡Oh no! No tenemos {nombre_producto}"

    ingredientes = [producto.ingrediente1_id, producto.ingrediente2_id, producto.ingrediente3_id]
    for ing_id in ingredientes:
        ingrediente = Ingrediente.query.get(ing_id)
        if ingrediente and ingrediente.inventario <= 0:
            raise ValueError(f"¡Oh no! Nos hemos quedado sin {ingrediente.nombre}")

    # Reducir inventario
    for ing_id in ingredientes:
        ingrediente = Ingrediente.query.get(ing_id)
        ingrediente.inventario -= 1

    return "¡Vendido!"

if __name__ == '__main__':
    app.run(debug=True)