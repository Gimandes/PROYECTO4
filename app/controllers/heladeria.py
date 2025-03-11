from sqlalchemy.orm import Session
from models.ingrediente import Ingrediente
from models.producto import Producto

def es_sano(calorias: int, vegetariano: bool) -> bool:
    return calorias < 100 or vegetariano

def abastecer_ingrediente(session: Session, ingrediente_id: int, nueva_cantidad: int):
   ingrediente = session.query(Ingrediente).filter_by(ingredienteID=ingrediente_id).first()
   
   if not ingrediente:
        raise ValueError("Ingrediente no encontrado")
   if ingrediente.cantidad == 0:
        ingrediente.cantidad = nueva_cantidad
        session.commit()
        return f"Ingrediente {ingrediente.nombre} reabastecido con {nueva_cantidad} unidades."
   return f"El ingrediente {ingrediente.nombre} aún tiene {ingrediente.cantidad} unidades disponibles."

def conteo_calorias(producto: Producto) -> float:
    calorias_totales = producto.ingrediente1.calorias + producto.ingrediente2.calorias + producto.ingrediente3.calorias
    return round(calorias_totales * 0.95, 2)

def costo_produccion(producto: Producto) -> float:
    return producto.ingrediente1.precio + producto.ingrediente2.precio + producto.ingrediente3.precio

def rentabilidad(producto: Producto) -> float:
    return producto.precio_venta - costo_produccion(producto)

def mejor_producto(session: Session):
    productos = session.query(Producto).all()
    if not productos:
        return "No hay productos registrados."

    producto_mas_rentable = max(productos, key=rentabilidad)
    return f"El mejor producto es: {producto_mas_rentable.nombre} con una rentabilidad de {rentabilidad(producto_mas_rentable)}"
