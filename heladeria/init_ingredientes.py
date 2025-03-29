from heladeria.config.db import db
from heladeria.app import app
from heladeria.models.ingrediente import Ingrediente

# Iniciar el contexto de la aplicación antes de cualquier operación con la base de datos
with app.app_context():
    # Verificar si la tabla tiene registros
    if not db.session.query(Ingrediente).first():
        ingredientes = [
            Ingrediente(ingredienteID=1, nombre="Leche entera", precio=1.5, calorias=150, disponible="si", tipo="Base", inventario=100, es_saludable="No"),
            Ingrediente(ingredienteID=2, nombre="Leche deslactosada", precio=1.7, calorias=140, disponible="si", tipo="Base", inventario=38, es_saludable="No"),
            Ingrediente(ingredienteID=3, nombre="Leche de almendras", precio=2.0, calorias=60, disponible="si", tipo="Base", inventario=40, es_saludable="Si"),
            Ingrediente(ingredienteID=4, nombre="Yogur natural", precio=2.2, calorias=120, disponible="si", tipo="Base", inventario=51, es_saludable="No"),
            Ingrediente(ingredienteID=5, nombre="Helado de vainilla", precio=3.5, calorias=250, disponible="si", tipo="Base", inventario=61, es_saludable="No"),
            Ingrediente(ingredienteID=6, nombre="Helado de chocolate", precio=3.5, calorias=270, disponible="si", tipo="Base", inventario=73, es_saludable="No"),
            Ingrediente(ingredienteID=7, nombre="Crema Batida", precio=2.0, calorias=200, disponible="si", tipo="Complemento", inventario=9, es_saludable="No"),
            Ingrediente(ingredienteID=8, nombre="Chocolate amargo", precio=3.0, calorias=180, disponible="si", tipo="Complemento", inventario=9, es_saludable="No"),
            Ingrediente(ingredienteID=9, nombre="Fresa", precio=1.2, calorias=50, disponible="si", tipo="Complemento", inventario=41, es_saludable="Si"),
            Ingrediente(ingredienteID=10, nombre="Miel", precio=1.8, calorias=120, disponible="si", tipo="Complemento", inventario=216, es_saludable="No"),
            Ingrediente(ingredienteID=11, nombre="Vainilla", precio=2.5, calorias=40, disponible="si", tipo="Complemento", inventario=32, es_saludable="Si"),
            Ingrediente(ingredienteID=12, nombre="Galleta Oreo", precio=1.75, calorias=220, disponible="no", tipo="Complemento", inventario=11, es_saludable="No"),
        ]
        db.session.add_all(ingredientes)
        db.session.commit()
        print("Ingredientes insertados correctamente.")
    else:
        print("La tabla Ingrediente ya tiene datos.")
