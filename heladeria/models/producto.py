from heladeria.app import app
from heladeria.config.db import db
from sqlalchemy.orm import sessionmaker

# Crear sesión
Session = sessionmaker(bind=db.engine)
session = Session()

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

with app.app_context():
    if not session.query(Producto).first():
        productos = [
            Producto(productoID=1, tipo_producto="Malteada A", precio=8000, ingrediente1=1, ingrediente2=5, ingrediente3=10, total_calorias=520, rentabilidad=7988.2),
            Producto(productoID=2, tipo_producto="Copa A", precio=9500, ingrediente1=6, ingrediente2=8, ingrediente3=9, total_calorias=475, rentabilidad=9492.3),
            Producto(productoID=3, tipo_producto="Malteada B", precio=8300, ingrediente1=2, ingrediente2=7, ingrediente3=11, total_calorias=380, rentabilidad=8288.8),
            Producto(productoID=4, tipo_producto="Copa B", precio=9200, ingrediente1=4, ingrediente2=5, ingrediente3=12, total_calorias=560.5, rentabilidad=9192.55),
        ]
        
        session.add_all(productos)
        session.commit()