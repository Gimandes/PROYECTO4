from sqlalchemy.orm import Session
from models.ingrediente import Ingrediente

def es_sano(session: Session):
    ingredientes = session.query(Ingrediente).all()

    for ingrediente in ingredientes:
        es_vegetariano = str(ingrediente.vegetariano).strip().lower() == "si"
        es_saludable = ingrediente.calorias < 100 and es_vegetariano

        # Convertir True/False a '1' o '0' para CHAR
        valor_saludable = 'Si' if es_saludable else 'No'

        if ingrediente.es_saludable != valor_saludable:
            ingrediente.es_saludable = valor_saludable

    session.commit()

