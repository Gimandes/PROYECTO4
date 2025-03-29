from heladeria.config.db import db
from heladeria.app import app
from heladeria.models.user import User

with app.app_context():
    if not db.session.query(User).first():
        users = [
            User(id=1, username="admin", password="123", is_admin=True, email="username1@un.com", cliente=True, empleado=True),
            User(id=2, username="empleado", password="123", is_admin=False, email="username2@un.com", cliente=False, empleado=True),
            User(id=3, username="cliente", password="123", is_admin=False, email="username3@un.com", cliente=True, empleado=False),
            User(id=4, username="cualquiera", password="123", is_admin=False, email="cualquiera@un.com", cliente=False, empleado=False),
        ]
        
        db.session.add_all(users)
        db.session.commit()
        print("Usuarios insertados correctamente.")
    else:
        print("La tabla User ya tiene datos.")
