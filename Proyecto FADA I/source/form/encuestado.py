class Encuestado:
    def __init__(self, id: int, nombre: str, experticia: int, opinion: int) -> object:
        self.id = id 
        self.nombre = nombre
        self.experticia = experticia
        self.opinion = opinion

    def getID(self) -> int:
        return self.id
    def getNombre(self) -> str:
        return self.nombre
    def getExperticia(self) -> int:
           return self.experticia
    def getOpinion(self) -> int:
         return self.opinion
    def setID(self, id: int):
         self.id = id
    def setNombre(self, nombre: str):
         self.nombre = nombre
    def setExperticia(self, experticia: int):
         self.experticia = experticia
    def setOpinion(self, opinion: int):
         self.opinion = opinion
    def data(self) -> str:
         return f"{self.getNombre()}"