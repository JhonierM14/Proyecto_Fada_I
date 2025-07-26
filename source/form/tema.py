class Tema:
    def __init__(self, id: int, nombre: str, preguntas):
        self.id = id
        self.nombre = nombre
        self.preguntas = preguntas

    def getID(self) -> int:
        return self.id
    def getNombre(self) -> str:
        return self.nombre
    def getPreguntas(self):
        return self.preguntas
    def setNombre(self, nombre: str):
        self.nombre = nombre
    def setPreguntas(self, preguntas):
        self.preguntas = preguntas
