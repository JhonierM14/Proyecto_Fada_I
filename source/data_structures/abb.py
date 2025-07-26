#Clase abb (Arbol Binario de Busqueda):
class abb():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
    def getVal(self):
        return self.val

class abb_experticia():
    """
    Árbol binario de búsqueda ordenado por experticia
    """
    def __init__(self, encuestado):
        self.left = None
        self.right = None
        self.encuestado = encuestado
    
    def getEncuestado(self):
        return self.encuestado
    
    def insert_experticia(self, encuestado):
        """
        Insertar encuestado en ABB ordenado por experticia (descendente)
        En caso de empate, ordenar por ID (descendente - mayor ID)
        """
        root_enc = self.getEncuestado()
        
        # Criterio: experticia descendente, ID descendente en empates (mayor ID primero)
        if (encuestado.getExperticia() > root_enc.getExperticia() or 
            (encuestado.getExperticia() == root_enc.getExperticia() and 
             encuestado.getID() > root_enc.getID())):
            if self.left is None:
                self.left = abb_experticia(encuestado)
            else:
                self.left.insert_experticia(encuestado)
        else:
            if self.right is None:
                self.right = abb_experticia(encuestado)
            else:
                self.right.insert_experticia(encuestado)
    
    def inorder_experticia(self):
        """
        Recorrido inorder del ABB por experticia
        """
        if self.left:
            self.left.inorder_experticia()
        
        enc = self.encuestado
        print(f" ({enc.getID()}, Nombre:'{enc.getNombre()}', Experticia:{enc.getExperticia()}, Opinión:{enc.getOpinion()})")
        
        if self.right:
            self.right.inorder_experticia()

class abb_mediana():
    """
    Árbol binario de búsqueda ordenado por mediana de pregunta
    """
    def __init__(self, pregunta_data):
        self.left = None
        self.right = None
        self.pregunta_data = pregunta_data
    
    def getPreguntaData(self):
        return self.pregunta_data
    
    def insert_mediana(self, pregunta_data):
        """
        Insertar pregunta en ABB ordenado por mediana (ascendente)
        En caso de empate, ordenar por ID de pregunta (ascendente)
        """
        root_data = self.getPreguntaData()
        
        # Criterio: mediana ascendente, ID ascendente en empates
        if (pregunta_data['mediana'] < root_data['mediana'] or 
            (pregunta_data['mediana'] == root_data['mediana'] and 
             pregunta_data['id'] < root_data['id'])):
            if self.left is None:
                self.left = abb_mediana(pregunta_data)
            else:
                self.left.insert_mediana(pregunta_data)
        else:
            if self.right is None:
                self.right = abb_mediana(pregunta_data)
            else:
                self.right.insert_mediana(pregunta_data)
    
    def inorder_mediana(self):
        """
        Recorrido inorder del ABB por mediana
        """
        if self.left:
            self.left.inorder_mediana()
        
        pregunta_data = self.pregunta_data
        pregunta = pregunta_data['pregunta']
        print(f"[{pregunta_data['mediana']}] {pregunta_data['nombre_completo']}: {pregunta.getIDS()}")
        
        if self.right:
            self.right.inorder_mediana()
    
    def find_min_mediana(self):
        """
        Encontrar el nodo con la menor mediana (más a la izquierda)
        """
        current = self
        while current.left is not None:
            current = current.left
        return current.pregunta_data

class abb_consenso():
    """
    Árbol binario de búsqueda ordenado por consenso de pregunta
    """
    def __init__(self, pregunta_data):
        self.left = None
        self.right = None
        self.pregunta_data = pregunta_data
    
    def getPreguntaData(self):
        return self.pregunta_data
    
    def insert_consenso(self, pregunta_data):
        """
        Insertar pregunta en ABB ordenado por consenso (descendente)
        En caso de empate, ordenar por ID de pregunta (ascendente)
        """
        root_data = self.getPreguntaData()
        
        # Criterio: consenso descendente, ID ascendente en empates
        if (pregunta_data['consenso'] > root_data['consenso'] or 
            (pregunta_data['consenso'] == root_data['consenso'] and 
             pregunta_data['id'] < root_data['id'])):
            if self.left is None:
                self.left = abb_consenso(pregunta_data)
            else:
                self.left.insert_consenso(pregunta_data)
        else:
            if self.right is None:
                self.right = abb_consenso(pregunta_data)
            else:
                self.right.insert_consenso(pregunta_data)
    
    def inorder_consenso(self):
        """
        Recorrido inorder del ABB por consenso
        """
        if self.left:
            self.left.inorder_consenso()
        
        pregunta_data = self.pregunta_data
        pregunta = pregunta_data['pregunta']
        print(f"[{pregunta_data['consenso']:.2f}] {pregunta_data['nombre_completo']}: {pregunta.getIDS()}")
        
        if self.right:
            self.right.inorder_consenso()
    
    def find_max_consenso(self):
        """
        Encontrar el nodo con el mayor consenso (más a la izquierda)
        """
        current = self
        while current.left is not None:
            current = current.left
        return current.pregunta_data

def arb_insert(root, key):
    if root is None:
        return abb(key)

    if root.getVal().getID()>=key.getID():
        if root.left == None:
            root.left = abb(key)
        else:
            arb_insert(root.left, key)
    
    if root.getVal().getID()<key.getID():
        if root.right == None:
            root.right = abb(key)
        else:
            arb_insert(root.right, key)

#Solo sirve para imprimir los valores del arbol de forma ascendiente
def inorder(root: abb):
    if root is None:
        return root

    inorder(root.right)
    print(root.val.getNombre(), end=" ")
    inorder(root.left)
