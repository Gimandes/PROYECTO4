from heladeria.config.db import db
from sqlalchemy.orm import sessionmaker

class Producto(db.Model):
    __tablename__ = "productos"

    productoID = db.Column(db.Integer, primary_key=True)
    tipo_producto = db.Column(db.String(45), nullable=False)
    precio_producto = db.Column(db.Float, nullable=False)
    ingrediente1 = db.Column(db.Integer, db.ForeignKey("ingredientes.ingredienteID"), nullable=False)
    ingrediente2 = db.Column(db.Integer, db.ForeignKey("ingredientes.ingredienteID"), nullable=False)
    ingrediente3 = db.Column(db.Integer, db.ForeignKey("ingredientes.ingredienteID"), nullable=False)
    nombre_ingrediente1 = db.Column(db.String(45), nullable=False)
    nombre_ingrediente2 = db.Column(db.String(45), nullable=False)
    nombre_ingrediente3 = db.Column(db.String(45), nullable=False)
    calorias1 = db.Column(db.Integer, nullable=False)
    calorias2 = db.Column(db.Integer, nullable=False)
    calorias3 = db.Column(db.Integer, nullable=False)
    total_calorias = db.Column(db.Float, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    rentabilidad = db.Column(db.Float, nullable=False)

