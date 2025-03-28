
from heladeria.config.db import db
from sqlalchemy.orm import sessionmaker

# Crear sesión
Session = sessionmaker(bind=db.engine)
session = Session()

class Ingrediente(db.Model):
    __tablename__ = "ingredientes"
    
    ingredienteID = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    calorias = db.Column(db.Integer, nullable=False)
    disponible = db.Column(db.String(50), nullable=False)  # "si" o "no"
    tipo = db.Column(db.String(50), nullable=False)  # Base o Complemento
    inventario = db.Column(db.Integer, nullable=False)
    es_saludable = db.Column(db.String(50), nullable=False)  # "Si" o "No"

with db.engine.connect() as conn:
    from heladeria.app import app
    with app.app_context():
        # Insertar datos solo si la tabla está vacía
        if not session.query(Ingrediente).first():
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
            session.add_all(ingredientes)
            session.commit()