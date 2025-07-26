from form.AlgoritmosOrdenamiento.mergeSort import merge_sort
from form.AlgoritmosOrdenamiento.MedidasTenciaCentral import promedio
from form.pregunta import Pregunta

class Tema:
    def __init__(self, nombre: str, preguntas: list[Pregunta]):
        self.nombre = nombre
        self.preguntas = preguntas

    def _iterate_preguntas(self):
        """
        Generador que itera sobre preguntas, manejando tanto listas Python como LDEs
        """
        if hasattr(self.preguntas, 'getData'):  # Es una LDE
            current = self.preguntas
            while current:
                yield current.getData()
                current = current.getNext()
        else:  # Es una lista Python
            for pregunta in self.preguntas:
                yield pregunta

    def getNombre(self) -> str:
        return self.nombre
    def getPreguntas(self) -> list[Pregunta]:
        return self.preguntas
    def setNombre(self, nombre: str):
        self.nombre = nombre
    def setPreguntas(self, preguntas: list[Pregunta]):
        self.preguntas = preguntas

    def getPromedioPreguntas(self) -> list:
        """
        Retorna una lista con los promedios individuales de las preguntas de un tema
        """
        return [pregunta.getPromedioPregunta() for pregunta in self._iterate_preguntas()]
    
    def getPromedioAllPreguntas(self) -> int:
        """
        Retorna el promedio de las preguntas de un tema
        """
        return round(promedio(self.getPromedioPreguntas()), 2)
    
    def getIDSEncuentadosTema(self) -> list:
        """
        Retorna una lista con el id de los encuestados de un tema
        """
        aux = []
        for pregunta in self._iterate_preguntas():
            aux += pregunta.getIDS()
        return aux