class Dispositivo:
    def __init__(self, nombre: str, es_esencial: bool = False):
        self.nombre = nombre
        self._estado = 0  # 0 = apagado, 1 = encendido
        self.es_esencial = es_esencial

    def encender(self):
        self._estado = 1
    def apagar(self):
        self._estado = 0

    def revisar_estado(self) -> str:
        return "encendido" if self._estado == 1 else "apagado"

    def modificar_estado(self, nuevo_estado: int):
        if nuevo_estado in (0, 1):
            self._estado = nuevo_estado
