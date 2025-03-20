import pytest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from models.ingrediente import Ingrediente
from heladeria.controllers.saludable import es_sano, abastecer_ingrediente

def test_es_sano():
    assert es_sano(50, False) == True  
    assert es_sano(150, True) == True  
    assert es_sano(150, False) == False  

def test_abastecer_ingrediente():
    session = MagicMock(spec=Session)
    ingrediente = Ingrediente(ingredienteID=1, nombre="Azúcar", cantidad=0)
    
    session.query().filter_by().first.return_value = ingrediente
    
    resultado = abastecer_ingrediente(session, 1, 50)
    
    assert ingrediente.cantidad == 50
    session.commit.assert_called_once()
    assert resultado == "Ingrediente Azúcar reabastecido con 50 unidades."

def test_abastecer_ingrediente_suficiente_stock():
    session = MagicMock(spec=Session)
    ingrediente = Ingrediente(ingredienteID=1, nombre="Leche", cantidad=10)
    
    session.query().filter_by().first.return_value = ingrediente
    
    resultado = abastecer_ingrediente(session, 1, 50)
    
    assert ingrediente.cantidad == 10
    assert resultado == "El ingrediente Leche aún tiene 10 unidades disponibles."