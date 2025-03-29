
from heladeria.config.db import db
from sqlalchemy.orm import sessionmaker

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
