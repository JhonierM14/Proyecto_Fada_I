#Clase abb (Arbol Binario de Busqueda):
class abb():
    def __init__(self, key = None):
        self.left = None
        self.right = None
        self.val = key
    
    def getVal(self):
        return self.val
    def gethijoIquierdo(self):
        return self.left
    def gethijoDerecho(self):
        return self.right

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

def promedio_opinion(pregunta):
    """
    Calcula el promedio de opinión de los encuestados de una pregunta (ABB).
    """
    total = 0
    count = 0

    def recorrer(nodo):
        nonlocal total, count
        if nodo is None or nodo.val is None:
            return
        recorrer(nodo.left)
        total += nodo.val.opinion
        count += 1
        recorrer(nodo.right)

    recorrer(pregunta.encuestados)
    return total / count if count > 0 else 0

def buscar_pregunta_menor_promedio(raiz, menor=None):
    if raiz is None:
        return menor

    menor = buscar_pregunta_menor_promedio(raiz.left, menor)
    actual_prom = promedio_opinion(raiz.val)
    if menor is None or actual_prom < promedio_opinion(menor):
        menor = raiz.val
    menor = buscar_pregunta_menor_promedio(raiz.right, menor)
    return menor

def moda_opinion(pregunta):
    frecuencias = [0] * 11
    nodo = pregunta.encuestados
    while nodo:
        frecuencias[nodo.val.opinion] += 1
        nodo = nodo.right
    max_frec = max(frecuencias)
    for i in range(11):
        if frecuencias[i] == max_frec:
            return i

def buscar_pregunta_menor_moda(raiz, menor=None):
    if raiz is None:
        return menor

    menor = buscar_pregunta_menor_moda(raiz.left, menor)
    actual_moda = moda_opinion(raiz.val)
    if menor is None or actual_moda < moda_opinion(menor):
        menor = raiz.val
    menor = buscar_pregunta_menor_moda(raiz.right, menor)
    return menor

def insertar_pregunta_arbol(raiz, pregunta):
    if raiz.val is None:
        raiz.val = pregunta
        return

    p1 = promedio_opinion(pregunta)
    p2 = promedio_opinion(raiz.val)

    if p1 > p2:
        if raiz.left:
            insertar_pregunta_arbol(raiz.left, pregunta)
        else:
            raiz.left = abb(pregunta)
    elif p1 < p2:
        if raiz.right:
            insertar_pregunta_arbol(raiz.right, pregunta)
        else:
            raiz.right = abb(pregunta)
    else:
        # Desempatar con experticia y luego con número de encuestados
        e1 = promedio_experticia(pregunta)
        e2 = promedio_experticia(raiz.val)
        if e1 > e2:
            if raiz.left:
                insertar_pregunta_arbol(raiz.left, pregunta)
            else:
                raiz.left = abb(pregunta)
        elif e1 < e2:
            if raiz.right:
                insertar_pregunta_arbol(raiz.right, pregunta)
            else:
                raiz.right = abb(pregunta)
        else:
            n1 = contar_encuestados(pregunta)
            n2 = contar_encuestados(raiz.val)
            if n1 > n2:
                if raiz.left:
                    insertar_pregunta_arbol(raiz.left, pregunta)
                else:
                    raiz.left = abb(pregunta)
            else:
                if raiz.right:
                    insertar_pregunta_arbol(raiz.right, pregunta)
                else:
                    raiz.right = abb(pregunta)

def promedio_experticia(pregunta):
    def _sumar(nodo):
        if nodo is None or nodo.val is None:
            return 0, 0  # suma, cantidad
        suma_izq, cant_izq = _sumar(nodo.left)
        suma_der, cant_der = _sumar(nodo.right)
        suma = suma_izq + nodo.val.experticia + suma_der
        cantidad = cant_izq + 1 + cant_der
        return suma, cantidad

    suma, cantidad = _sumar(pregunta.encuestados)
    return suma / cantidad if cantidad > 0 else 0

def contar_encuestados(pregunta):
    def _contar(nodo):
        if nodo is None or nodo.val is None:
            return 0
        return 1 + _contar(nodo.left) + _contar(nodo.right)
    
    return _contar(pregunta.encuestados)
