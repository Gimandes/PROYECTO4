from heladeria.config.db import db
from heladeria.app import app
from heladeria.models.producto import Producto

# Ejecutar dentro del contexto de la aplicación Flask
with app.app_context():
    # Verifica si hay productos en la tabla
    if not db.session.query(Producto).first():
        productos = [
            Producto(productoID=1, tipo_producto="Malteada A", precio=8000, ingrediente1=1, ingrediente2=5, ingrediente3=10, total_calorias=520, rentabilidad=7988.2),
            Producto(productoID=2, tipo_producto="Copa A", precio=9500, ingrediente1=6, ingrediente2=8, ingrediente3=9, total_calorias=475, rentabilidad=9492.3),
            Producto(productoID=3, tipo_producto="Malteada B", precio=8300, ingrediente1=2, ingrediente2=7, ingrediente3=11, total_calorias=380, rentabilidad=8288.8),
            Producto(productoID=4, tipo_producto="Copa B", precio=9200, ingrediente1=4, ingrediente2=5, ingrediente3=12, total_calorias=560.5, rentabilidad=9192.55),
        ]
        
        db.session.add_all(productos)
        db.session.commit()
        print("Productos insertados correctamente.")
    else:
        print("La tabla Producto ya tiene datos.")
