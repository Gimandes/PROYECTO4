from models.ingrediente import Ingrediente
from models.producto import Producto
from config.db import db

def calcular_calorias():
    productos = Producto.query.all()
    ingredientes = {ing.ingredienteID: ing for ing in Ingrediente.query.all()}  

    for producto in productos:
        ingrediente1 = ingredientes.get(producto.ingrediente1, Ingrediente(calorias=0))
        ingrediente2 = ingredientes.get(producto.ingrediente2, Ingrediente(calorias=0))
        ingrediente3 = ingredientes.get(producto.ingrediente3, Ingrediente(calorias=0))

        if "Copa" in producto.tipo_producto: 
            producto.total_calorias = (ingrediente1.calorias + ingrediente2.calorias + ingrediente3.calorias) * 0.95
        else:
            producto.total_calorias = ingrediente1.calorias + ingrediente2.calorias + ingrediente3.calorias

    return productos