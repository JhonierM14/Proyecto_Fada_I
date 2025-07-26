from form.AlgoritmosOrdenamiento.MedidasTenciaCentral import promedio
from form.encuestado import Encuestado

class Pregunta:
    def __init__(self, nombre: str, encuestados: list[Encuestado]):
        self.nombre = nombre
        self.encuestados = encuestados

    def _iterate_encuestados(self):
        """
        Generador que itera sobre encuestados, manejando tanto listas Python como LDEs
        """
        if hasattr(self.encuestados, 'getData'):  # Es una LDE
            current = self.encuestados
            while current:
                yield current.getData()
                current = current.getNext()
        else:  # Es una lista Python
            for encuestado in self.encuestados:
                yield encuestado

    def getNombre(self) -> str:
        return self.nombre
        
    def getEncuestados(self):
        return self.encuestados

    def getIDS(self) -> list[int]:
        """
        Retorna una lista con los ids de los encuestados de una pregunta 
        """
        return [e.getID() for e in self._iterate_encuestados()]

    def get_experticias(self) -> list[int]:
        """
        Retorna una lista con la experticia de los encuestados de una pregunta
        """
        return [e.getExperticia() for e in self._iterate_encuestados()]
    
    def get_opiniones(self) -> list[int]:
        """
        Retorna una lista con las opiniones de todos los encuestados de una pregunta
        """
        return [e.getOpinion() for e in self._iterate_encuestados()]
    
    def getPromedioPregunta(self) -> int:
        """
        Retorna el puntaje promedio de la pregunta
        """
        return round(promedio(self.get_opiniones()), 2)
