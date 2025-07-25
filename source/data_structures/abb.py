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

def Arb_Insert(nodo, llave, metodo):
    if nodo is None or nodo.val is None:
        return abb(llave)
    
    if metodo(nodo.val) >= metodo(llave):
        if nodo.left == None:
            nodo.left = abb(llave)
        else:
            Arb_Insert(nodo.left, llave, metodo)
    
    if metodo(nodo.val) < metodo(llave):
        if nodo.right == None:
            nodo.right = abb(llave)
        else:
            Arb_Insert(nodo.right, llave, metodo)
            
    return nodo

#Solo sirve para imprimir los valores del arbol de forma ascendiente
def inorder(root: abb):
    if root is None:
        return root

    inorder(root.right)
    print(root.val.getNombre(), end=" ")
    inorder(root.left)

def Arb_Size(arbol):
    if arbol is None:
        return 0
    return 1 + Arb_Size(arbol.left) + Arb_Size(arbol.right)

def Arb_to_List(nodo, resultado): # Esta función pasa un arbol a una lista
        if nodo is None:
            return 0
        Arb_to_List(nodo.left, resultado)
        resultado.append(nodo.val)
        Arb_to_List(nodo.right, resultado)
    
def insertion_sort(arr, metodo):
    for i in range(1, len(arr)):
        key_item = arr[i]
        key = metodo(key_item)
        j = i - 1
        while j >= 0 and metodo(arr[j]) > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr

def Arb_Median(arbol, metodo):
    elementos = []
    Arb_to_List(arbol, elementos)
    elementos = insertion_sort(elementos, metodo)
    n = len(elementos)

    if n == 0:
        return None
    if n % 2 == 1:
        return elementos[n // 2]
    else:
        return elementos[n // 2 - 1]
