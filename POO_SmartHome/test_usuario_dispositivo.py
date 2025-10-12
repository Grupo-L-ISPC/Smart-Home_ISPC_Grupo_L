import pytest
from usuario import Usuario
from dispositivo import Dispositivo

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


def test_dispositivo_encender_apagar():
    d = Dispositivo("Luz sala")
    assert d.revisar_estado() == "apagado"
    d.encender()
    assert d.revisar_estado() == "encendido"
    d.apagar()
    assert d.revisar_estado() == "apagado"

@pytest.mark.parametrize("estado_inicial, nuevo_estado, esperado", [
    (False, 1, "encendido"),
    (True, 0, "apagado"),
])
def test_dispositivo_modificar_estado(estado_inicial, nuevo_estado, esperado):
    d = Dispositivo("Ventilador", estado_inicial)
    d.modificar_estado(nuevo_estado)
    assert d.revisar_estado() == esperado

