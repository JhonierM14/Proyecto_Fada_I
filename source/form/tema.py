class Tema:
    def __init__(self, nombre, preguntas):
        self.nombre = nombre
        self.preguntas = preguntas
    
    def getNombre(self):
        return self.nombre
    def getPreguntas(self):
        return self.preguntas