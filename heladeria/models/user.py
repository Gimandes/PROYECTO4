from heladeria.config.db import db
from flask_login import  UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default = False)
    email = db.Column(db.String(120), nullable=False, default = False)
    cliente = db.Column(db.Boolean, nullable=False, default = False)
    empleado = db.Column(db.Boolean, nullable=False, default = False)