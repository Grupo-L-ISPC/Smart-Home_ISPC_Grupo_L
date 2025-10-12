class Usuario:
    def __init__(self, nombre: str, contraseña: str, es_admin: bool = False):
        self._nombre = nombre
        self._contraseña = contraseña
        self._es_admin = es_admin

    
    def iniciar_sesion(self, nombre: str, contraseña: str) -> bool:
        return self._nombre == nombre and self._contraseña == contraseña
    
    def registrarse(self, nombre: str, contraseña: str):
        """Simula registro de un usuario, reasignando atributos."""
        self.nombre = nombre
        self.contraseña = contraseña
        self.es_admin = False

    def cambiar_contraseña(self, nueva_contraseña: str):
        self._contraseña = nueva_contraseña

    def ver_datos(self) -> dict:
        return {
            "nombre": self._nombre,
            "es_admin": self._es_admin
            
        }

            
            
            
