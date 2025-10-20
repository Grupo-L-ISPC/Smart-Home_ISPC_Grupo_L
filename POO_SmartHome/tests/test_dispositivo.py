import pytest
from POO_SmartHome.dominio.dispositivo import Dispositivo

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

