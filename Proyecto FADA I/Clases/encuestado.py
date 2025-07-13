class Encuestado:
    def __init__(self, id, nombre, experticia, opinion):
        self.id = id 
        self.nombre = nombre
        self.experticia = experticia
        self.opinion = opinion

    def getID(self):
        return self.id
    def getNombre(self):
        return self.nombre
    def getExperticia(self):
           return self.experticia
    def getOpinion(self):
         return self.opinion
    def setID(self, id):
         self.id = id
    def setNombre(self, nombre):
         self.nombre = nombre
    def setExperticia(self, experticia):
         self.experticia = experticia
    def setOpinion(self, opinion):
         self.opinion = opinion