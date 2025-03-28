import time
from flask import Flask, render_template, request,  redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from heladeria.config.config import Config
from sqlalchemy.orm import sessionmaker
from heladeria.config.db import db
from heladeria.models.ingrediente import Ingrediente
from heladeria.models.producto import Producto
from heladeria.models.user import User
from heladeria.controllers.vender import vender_producto
from heladeria.controllers.saludable import es_sano
from heladeria.controllers.abastecer import abastecer
from heladeria.controllers.total_calorias import calcular_calorias
from heladeria.controllers.total_precio import calcular_precio, rentabilidad 
from flask_login import LoginManager, login_user, current_user, login_required, logout_user

app = Flask(__name__, template_folder="templates")
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'tu_clave_secreta'

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login" 
login_manager.login_message_category = "info"



def set_password(self, password):
        self.password = generate_password_hash(password)

def check_password(self, password):
        return check_password_hash(self.password, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def home():
    return render_template("index.html") 

# Ruta de login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            flash("Inicio de sesión exitoso", "success")
            return redirect(url_for("dashboard_admin" if user.is_admin else "dashboard_cliente" if user.cliente else "dashboard"))

        flash("Usuario o contraseña incorrectos", "error")

    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Has cerrado sesión", "info")
    return redirect(url_for("login"))

@app.route("/dashboard")
@login_required
def dashboard():
   return render_template("dashboard.html") 

@app.route("/dashboard_admin")
@login_required
def dashboard_admin():
    if current_user.is_admin:# Verifica si el usuario no es administrador
        return render_template("dashboard_admin.html")             
    else:
            flash("Acceso denegado. Solo los administradores pueden ingresar.", "danger")
            return redirect(url_for("dashboard"))

    
   

@app.route("/auth/profile")
@login_required
def auth_profile():
    if current_user.is_admin:
        return f"datos: {current_user.username}- {current_user.password} - {current_user.email}"
    return f"datos: {current_user.username}- {current_user.password}"

@app.route("/ingredientes")
@login_required
def mostrar_ingredientes():
    if current_user.is_admin or current_user.empleado:
        db.session.expire_all()
        ingredientes = Ingrediente.query.all()
        for ingrediente in ingredientes:
            print(f"{ingrediente.nombre}: {ingrediente.es_saludable}")  
        return render_template("ingredientes.html", ingredientes=ingredientes)
    else: 
        flash("Acceso denegado. Solo los administradores pueden ingresar.", "danger")
        return redirect(url_for("dashboard.html"))
    
@app.route("/productos")
@login_required
def mostrar_productos():
    if current_user.is_admin: 
        productos = Producto.query.all()
        ingredientes = Ingrediente.query.all() 
        productos_con_calorias = calcular_calorias()
        productos_con_precio = calcular_precio()   # Llamamos a la función del controlador
        producto_con_rentabilidad = rentabilidad ()
        return render_template("productos.html", productos=productos, producto_con_rentabilidad=producto_con_rentabilidad, ingredientes=ingredientes, productos_con_calorias=productos_con_calorias, productos_con_precio=productos_con_precio)

    elif current_user.empleado:  
        productos = Producto.query.all()
        ingredientes = Ingrediente.query.all() 
        productos_con_calorias = calcular_calorias()
        productos_con_precio = calcular_precio()   # Llamamos a la función del controlador
        return render_template("productos.html", productos=productos, ingredientes=ingredientes, productos_con_calorias=productos_con_calorias, productos_con_precio=productos_con_precio)
        
    elif current_user.cliente: 
            productos = Producto.query.all()
            productos_con_calorias = calcular_calorias()
            productos_con_precio = calcular_precio()   # Llamamos a la función del controlador
            return render_template("productos.html", productos=productos, productos_con_calorias=productos_con_calorias, productos_con_precio=productos_con_precio)
            
    else: 
            productos = Producto.query.all()
            productos_con_precio = calcular_precio()   # Llamamos a la función del controlador
            return render_template("productos.html", productos=productos, productos_con_precio=productos_con_precio)
        
@app.route("/vender", methods=["GET"])
@login_required
def vender():
    if current_user.is_admin or current_user.empleado or current_user.cliente:
        if "tipo_producto" in request.args:
            return vender_producto()  # Llama a la función para vender si se envió un producto
        
        productos = Producto.query.all()  
        ingredientes = Ingrediente.query.all()
        return render_template("vender.html", productos=productos, ingredientes=ingredientes)
    else: 
        flash("Acceso denegado. Solo los administradores pueden ingresar.", "danger")
        return redirect(url_for("dashboar.html"))

@app.route("/actualizar_saludable")
@login_required
def actualizar_todos_saludable():
    if current_user.is_admin or current_user.empleado:
        with app.app_context():
            es_sano(db.session)  # Pasa la sesión correctamente
        return redirect(url_for('mostrar_ingredientes'))  # Redirige a la tabla actualizada
    else: 
        flash("Acceso denegado. Solo los administradores pueden ingresar.", "danger")
        return redirect(url_for("dashboard"))

@app.route("/abastecer")
@login_required
def abastecer_ingredientes():
    if current_user.is_admin or current_user.empleado or current_user.cliente:  # Asegúrate de que `empleado` existe antes de usarlo
        return abastecer()  # Llamamos a la función directamente y devolvemos el resultado
    else:
        flash("Acceso denegado. Solo los administradores pueden ingresar.", "danger")
        return redirect(url_for("dashboard"))



@app.route("/auth", methods=["GET"]) 
def auth():
    username = request.args.get("username")  
    password = request.args.get("password")

    user = User.query.filter_by(username=username, password=password).first()

    if user:
        login_user(user)
        if user.is_admin: 
            return redirect(url_for("dashboard_admin"))
        return redirect(url_for("dashboard"))
    flash ("Las credenciales no estan registradas en nuestro sistema.", "error")
    return render_template("login.html", error="Usuario o contraseña incorrectos")    

with app.app_context():
    db.create_all

if __name__ == '__main__':
    app.run(debug=True)
