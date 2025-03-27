from flask import request, redirect, url_for, flash
from config.db import db
from heladeria.models.producto import Producto
from heladeria.models.ingrediente import Ingrediente

def vender_producto():
    tipo_producto = request.args.get("tipo_producto")  # Obtener el producto seleccionado desde la URL

    print(f"🔹 Intentando vender: {tipo_producto}")  # ✅ Verificar si la función se ejecuta

    if not tipo_producto:
        flash("❌ Debes seleccionar un producto antes de vender.", "error")
        return redirect(url_for("vender"))

    # Buscar el producto en la base de datos
    producto = Producto.query.filter_by(tipo_producto=tipo_producto).first()

    if not producto:
        flash(f"❌ No encontramos el producto '{tipo_producto}' en la base de datos.", "error")
        return redirect(url_for("vender"))

    # Obtener los ingredientes asociados
    ingredientes = [
        db.session.get(Ingrediente, producto.ingrediente1),
        db.session.get(Ingrediente, producto.ingrediente2),
        db.session.get(Ingrediente, producto.ingrediente3),
    ]

    print(f"📋 Ingredientes encontrados: {[ing.nombre if ing else 'N/A' for ing in ingredientes]}")

    # Verificar inventario
    for ingrediente in ingredientes:
        if ingrediente is None:
            flash("❌ Ingrediente no encontrado en la base de datos.", "error")
            return redirect(url_for("vender"))
        if ingrediente.inventario <= 0:
            flash(f"❌ No hay suficiente {ingrediente.nombre} para hacer {tipo_producto}.", "error")
            return redirect(url_for("vender"))

    # Descontar inventario de los ingredientes
    for ingrediente in ingredientes:
        print(f"➡️ Descontando 1 unidad de {ingrediente.nombre} (Antes: {ingrediente.inventario})")
        ingrediente.inventario -= 1  # Restar 1 unidad al inventario
        print(f"✅ Nuevo inventario de {ingrediente.nombre}: {ingrediente.inventario}")

    db.session.commit()  # Guardar cambios en la base de datos    
    db.session.flush()  # 🔹 Forzar la actualización en la sesión
    print("✅ Inventario actualizado en la base de datos.")

    flash(f"✅ ¡Venta realizada! Disfruta tu {tipo_producto} 🍦", "success")
    return redirect(url_for("vender"))