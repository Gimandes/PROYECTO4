from flask import request, render_template, redirect, url_for, flash
from heladeria.config.db import db
from heladeria.models.ingrediente import Ingrediente

def abastecer():
    print(request.args)
    ingrediente_id = request.args.get("ingrediente_id")
    cantidad = request.args.get("cantidad")

    if ingrediente_id and cantidad:
        try:
            ingrediente_id = int(ingrediente_id)
            cantidad = int(cantidad)

            if cantidad <= 0:
                flash("La cantidad debe ser un número entero positivo", "error")
                return redirect(url_for("abastecer"))

            ingrediente = Ingrediente.query.get(ingrediente_id)

            if not ingrediente:
                flash("Ingrediente no encontrado", "error")
                return redirect(url_for("abastecer"))

            ingrediente.inventario += cantidad
            db.session.flush()
            db.session.commit()

            flash("Inventario actualizado correctamente", "success")
            return redirect(url_for("abastecer"))

        except ValueError:
            flash("Entrada inválida. Asegúrate de ingresar un número válido", "error")
            return redirect(url_for("abastecer"))
        except Exception as e:
            flash(f"Error inesperado: {str(e)}", "error")
            return redirect(url_for("abastecer"))

    ingredientes = Ingrediente.query.all()
    return render_template("abastecer.html", ingredientes=ingredientes)
