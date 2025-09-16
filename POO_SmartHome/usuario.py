class Usuario:
    def __init__(self, nombre: str, contraseña: str, es_admin: bool = False):
        self.nombre = nombre
        self.contraseña = contraseña
        self.es_admin = es_admin

    def iniciar_sesion(self, nombre: str, contraseña: str) -> bool:
        """Devuelve True si los datos coinciden, False si no."""
        return self.nombre == nombre and self.contraseña == contraseña
    def registrarse(self, nombre: str, contraseña: str):
        """Simula registro de un usuario, reasignando atributos."""
        self.nombre = nombre
        self.contraseña = contraseña
        self.es_admin = False

    def cambiar_contraseña(self, nueva_contraseña: str):
        self.contraseña = nueva_contraseña
def ver_datos(self) -> dict:
        return {
            "nombre": self.nombre,
            "es_admin": self.es_admin
            
        }

            
            
            
