#Clase abb (Arbol Binario de Busqueda):
class abb:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def arb_insert(root, key):
    if root is None:
        return abb(key)
    
    if root.val>=key:
        if root.left == None:
            root.left = abb(key)
        arb_insert(root.left, key)
    
    if root.val<key:
        if root.right == None:
            root.right = abb(key)
        arb_insert(root.right, key)

#Solo sirve para imprimir los valores del arbol de forma ascendiente
def inorder(root):
    if root is None:
        return root
    inorder(root.right)
    print(root.val, end=" ")
    inorder(root.left)
    
