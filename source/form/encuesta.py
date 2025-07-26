from form.tema import Tema
from form.AlgoritmosOrdenamiento.MedidasTenciaCentral import promedio

class Encuesta():
    'K => temas, ' \
    'M => preguntas, ' \
    'Nmin => cantidad minima de encuestados, ' \
    'Nmax => cantidad maxima de encuestados'

    "Se debe cumplir siempre que => Nmin < Nmax"
    
    def __init__(self, K: int, M: int, Nmin: int, Nmax: int, Temas: list[Tema]):
        self.K = K
        self.M = M
        self.Nmin = Nmin
        self.Nmax = Nmax
        self.Temas = Temas
    
    def getK(self) -> int:
        return self.K
    def getM(self) -> int:
        return self.M
    def getNmin(self) -> int:
        return self.Nmin
    def getNmax(self) -> int:
        return self.Nmax
    def getTemas(self) -> list:
        return self.Temas
    
    def setK(self, K: int):
        self.K = K
    def setM(self, M: int):
        self.M = M
    def setNmin(self, Nmin: int):
        self.Nmin = Nmin
    def setNmax(self, Nmax: int):
        self.Nmax = Nmax
    def setTemas(self, Temas: list[Tema]):
        self.Temas = Temas
