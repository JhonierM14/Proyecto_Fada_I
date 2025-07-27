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

    def _iterate_temas(self):
        """
        Generador que itera sobre temas, manejando tanto listas Python como LDEs
        """
        if hasattr(self.Temas, 'getData'):  # Es una LDE
            current = self.Temas
            while current:
                yield current.getData()
                current = current.getNext()
        else:  # Es una lista Python
            for tema in self.Temas:
                yield tema
    
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