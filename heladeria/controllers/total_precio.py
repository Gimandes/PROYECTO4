from models.ingrediente import Ingrediente
from models.producto import Producto
from config.db import db

def calcular_precio():
    productos = Producto.query.all()
    ingredientes = {ing.ingredienteID: ing for ing in Ingrediente.query.all()}  

    for producto in productos:
        ingrediente1 = ingredientes.get(producto.ingrediente1, Ingrediente(nombre="Desconocido", precio=0))
        ingrediente2 = ingredientes.get(producto.ingrediente2, Ingrediente(nombre="Desconocido", precio=0))
        ingrediente3 = ingredientes.get(producto.ingrediente3, Ingrediente(nombre="Desconocido", precio=0))

        if "Malteada" in producto.tipo_producto: 
            producto.total_precio = ingrediente1.precio + ingrediente2.precio + ingrediente3.precio + 5.0
        else:
             producto.total_precio = ingrediente1.precio + ingrediente2.precio + ingrediente3.precio
        
    db.session.commit()  # Guardamos los cambios en la base de datos
    return productos

def rentabilidad():
    productos = Producto.query.all()
    ingredientes = {ing.ingredienteID: ing for ing in Ingrediente.query.all()}  

    for producto in productos:
        ingrediente1 = ingredientes.get(producto.ingrediente1, Ingrediente(nombre="Desconocido", precio=0))
        ingrediente2 = ingredientes.get(producto.ingrediente2, Ingrediente(nombre="Desconocido", precio=0))
        ingrediente3 = ingredientes.get(producto.ingrediente3, Ingrediente(nombre="Desconocido", precio=0))

        if "Malteada" in producto.tipo_producto: 
            producto.rentabilidad = producto.precio_producto - (ingrediente1.precio + ingrediente2.precio + ingrediente3.precio + 5.0)
        else:
             producto.rentabilidad = producto.precio_producto - (ingrediente1.precio + ingrediente2.precio + ingrediente3.precio) 
        
    db.session.commit()  # Guardamos los cambios en la base de datos
    return productos