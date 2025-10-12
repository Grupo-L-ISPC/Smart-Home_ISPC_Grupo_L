class Automatizacion:
    def __init__(self, nombre: str, tipo: str):
        self.nombre = nombre
        self.tipo = tipo
        """
        Clase que representa una automatización dentro del sistema SmartHome.

        Atributos:
            nombre (str): Nombre de la automatización (ej: "Encender luces").
            tipo (str): Tipo de automatización (ej: "manual", "horario", "sensor").
        """

    def ejecutar(self):
        """Ejecuta la automatización y devuelve un mensaje indicando qué se está haciendo."""
        
        return f"Ejecutando automatización: {self.nombre} ({self.tipo})"