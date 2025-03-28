from heladeria.app import app
from heladeria.config.db import db
from flask_login import UserMixin
from sqlalchemy.orm import sessionmaker

# Crear sesión
Session = sessionmaker(bind=db.engine)
session = Session()

class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default = False)
    email = db.Column(db.String(120), nullable=False, default = False)
    cliente = db.Column(db.Boolean, nullable=False, default = False)
    empleado = db.Column(db.Boolean, nullable=False, default = False)


with app.app_context():
    if not session.query(User).first():
        users = [
            User(id=1, username="admin", password="123", is_admin=True, email="username1@un.com", cliente=True, empleado=True),
            User(id=2, username="empleado", password="123", is_admin=False, email="username2@un.com", cliente=False, empleado=True),
            User(id=3, username="cliente", password="123", is_admin=False, email="username3@un.com", cliente=True, empleado=False),
            User(id=4, username="cualquiera", password="123", is_admin=False, email="cualquiera@un.com", cliente=False, empleado=False),
        ]
        
        session.add_all(users)
        session.commit()