from flask import Flask, render_template, request
from config.config import Config
from config.db import db
from models.ingrediente import Ingrediente
from models.producto import Producto
from controllers.vender import vender_producto

app = Flask(__name__, template_folder="templates")
app.config.from_object(Config)
db.init_app(app)
app.config['SECRET_KEY'] = 'tu_clave_secreta'

@app.route("/")
def home():
    return render_template("index.html") 

@app.route("/ingredientes")
def mostrar_ingredientes():
    ingredientes = Ingrediente.query.all()
    return render_template("ingredientes.html", ingredientes=ingredientes)

@app.route("/productos")
def mostrar_productos():
    productos = Producto.query.all()
    return render_template("productos.html", productos=productos)

@app.route("/vender", methods=["GET"])
def vender():
    if "tipo_producto" in request.args:
        return vender_producto()  # Llama a la función para vender si se envió un producto
    
    productos = Producto.query.all()  
    ingredientes = Ingrediente.query.all()
    return render_template("vender.html", productos=productos, ingredientes=ingredientes)
    
if __name__ == '__main__':
    app.run(debug=True)