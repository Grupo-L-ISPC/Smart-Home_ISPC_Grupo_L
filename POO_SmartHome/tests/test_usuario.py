import pytest
from POO_SmartHome.dominio.usuario import Usuario

def test_usuario_sesion_y_cambio():
    u = Usuario("Ana", "1234")
    assert u.iniciar_sesion("Ana", "1234")
    assert not u.iniciar_sesion("Ana", "0000")
    u.cambiar_contraseña("abcd")
    assert u.iniciar_sesion("Ana", "abcd")

def test_usuario_ver_datos():
    u = Usuario("Mauro", "clave", es_admin=True)
    datos = u.ver_datos()
    assert datos["nombre"] == "Mauro"
    assert datos["es_admin"] is True