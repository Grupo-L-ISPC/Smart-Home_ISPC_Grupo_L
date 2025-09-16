import pytest
from automatizacion  import Automatizacion

def test_crear_automatizacion():
    a = Automatizacion("Encender luces", "horario")
    assert a.nombre == "Encender luces"
    assert a.tipo == "horario"

def test_ejecutar_automatizacion():
    a = Automatizacion("Apagar ventiladores", "manual")
    resultado = a.ejecutar()
    assert "Apagar ventiladores" in resultado
    assert "manual" in resultado