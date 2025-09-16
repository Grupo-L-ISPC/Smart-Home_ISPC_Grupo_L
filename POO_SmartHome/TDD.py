import unittest
from poo_smart_home.usuario import Usuario
from poo_smart_home.dispositivo import Dispositivo

class TestUsuarioDispositivo(unittest.TestCase):
    def test_usuario_sesion_y_cambio(self):
        u = Usuario("Ana", "1234")
        self.assertTrue(u.iniciar_sesion("Ana", "1234"))
        self.assertFalse(u.iniciar_sesion("Ana", "0000"))
        u.cambiar_contraseña("abcd")
        self.assertTrue(u.iniciar_sesion("Ana", "abcd"))

    def test_dispositivo_encender_apagar(self):
        d = Dispositivo("Luz sala")
        self.assertEqual(d.revisar_estado(), "apagado")
        d.encender()
        self.assertEqual(d.revisar_estado(), "encendido")
        d.apagar()
        self.assertEqual(d.revisar_estado(), "apagado")

    def test_dispositivo_modificar_estado(self):
        d = Dispositivo("Ventilador", True)
        d.modificar_estado(1)
        self.assertEqual(d.revisar_estado(), "encendido")
        d.modificar_estado(0)
        self.assertEqual(d.revisar_estado(), "apagado")

    def test_dispositivo_modificar_estado(self):
        d = Dispositivo("Ventilador", True)
        d.modificar_estado(1)
        self.assertEqual(d.revisar_estado(), "encendido")
        d.modificar_estado(0)
        self.assertEqual(d.revisar_estado(), "apagado")
    

