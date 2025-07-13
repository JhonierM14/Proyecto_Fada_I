class Pregunta:
    def __init__(self, nombre, encuestados):
        self.nombre = nombre
        self.encuestados = encuestados

    def obtener_opiniones(self):
        return [e.opinion for e in self.encuestados]

    def obtener_experticias(self):
        return [e.experticia for e in self.encuestados]