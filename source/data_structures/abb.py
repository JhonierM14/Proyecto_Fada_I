#Clase abb (Arbol Binario de Busqueda):
class abb():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
    def getVal(self):
        return self.val

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
