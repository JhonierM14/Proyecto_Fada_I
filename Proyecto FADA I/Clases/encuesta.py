class Encuesta:
    'K => temas, ' \
    'M => preguntas, ' \
    'Nmin => cantidad minima de encuestados, ' \
    'Nmax => cantidad maxima de encuestados'

    "Se debe cumplir siempre que => Nmin < Nmax"
    
    def __init__(self, K, M, Nmin, Nmax, Temas):
        self.K = K
        self.M = M
        self.Nmin = Nmin
        self.Nmax = Nmax
        self.Temas = Temas
    
    def getK(self):
        return self.K
    def getM(self):
        return self.M
    def getNmin(self):
        return self.Nmin
    def getNmax(self):
        return self.Nmax
    def getTemas(self):
        return self.Temas
    def setK(self, K):
        self.K = K
    def setM(self, M):
        self.M = M
    def setNmin(self, Nmin):
        self.Nmin = Nmin
    def setNmax(self, Nmax):
        self.Nmax = Nmax
    def setTemas(self, Temas):
        self.Temas = Temas