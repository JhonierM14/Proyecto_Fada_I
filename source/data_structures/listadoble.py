class LDE: # Clase LDE (Lista Doblemente Entrelazada)
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def List_Print(lista):
    current = lista
    while current: # Recorremos la lista desde la cabeza hasta el final
        print(current.data, end=" <-> ") # Imprimimos el dato del nodo actual
        current = current.next # Cambiamos al siguiente nodo
    print("None") # Imprimimos None al final para indicar el final de la lista

def List_Insert(lista, llave):
    nuevo_nodo = LDE(llave)
    nuevo_nodo.next = lista # el puntero next del nuevo nodo apunta a la cabeza
    if lista: # si la cabeza es None (no hay un nodo después) no entra en este if
        lista.prev = nuevo_nodo # el puntero prev de la cabeza apunta al nuevo nodo
    return nuevo_nodo

def List_Insert_End(lista, data):
    nuevo = LDE(data) 
    if lista is None: # Si la lista está vacía, el nuevo nodo es la cabeza
        return nuevo
    actual = lista
    while actual.next: # mientras haya un siguiente nodo
        actual = actual.next # cambiamos al siguiente nodo
    actual.next = nuevo # el puntero next del último nodo apunta al nuevo nodo
    nuevo.prev = actual # el puntero prev del nuevo nodo apunta al último nodo
    return lista # Retornamos la cabeza de la lista

def lde_last(head):
    while head.next:
        head = head.next
    return head

def lde_join(lde1, lde2):
    if not lde1:
        return lde2
    elif not lde2:
        return lde1
    else:
        last = lde_last(lde1)
        last.next = lde2
        lde2.prev = last
        return lde1

def List_Size(lista):
    if lista is None: # Si la lista está vacía, retornamos 0
        return 0
    
    actual = lista
    size = 1 # Contador para saber el tamaño de la lista

    while actual.next: # Mientras haya un siguiente nodo
        size += 1 # Aumentamos el contador
        actual = actual.next # Cambiamos al siguiente nodo
    return size # Retornamos el tamaño de la lista

def List_Median(lista):
    if lista is None:
        return 0
    
    if List_Size(lista)%2 == 0: # Si la lista tiene un número par de elementos
        lista = List_Insert(lista, 0) # Añadimos un elemento cualquiera para que sea impar

    izq, der = List_Divide(lista) # Por la naturaleza de Divide, la mediana se encontrará al inicio de la lista derecha
    return der.data # Retornamos la mediana

#--------------------------------------FUNCIONES PARA MERGE SORT-------------------------------------

def List_Divide(lista):
    lista_izq = None # Lista para almacenar la mitad izquierda
    lista_der = None # Lista para almacenar la mitad derecha
    full_size = List_Size(lista) # Tamaño total de la lista
    mitad = full_size // 2 # Tamaño de la mitad de la lista
    contador = 0 # Contador para recorrer la lista original
    
    while contador < full_size: # Recorremos la lista original
        if contador < mitad: # Si el contador es menor que la mitad
            lista_izq = List_Insert_End(lista_izq, lista.data) # Añadimos el nodo a la lista izquierda
        else: # Si el contador es mayor o igual que la mitad
            lista_der = List_Insert_End(lista_der, lista.data) # Añadimos el nodo a la lista derecha
        lista = lista.next # Cambiamos al siguiente nodo
        contador += 1 # Aumentamos el contador

    return lista_izq, lista_der # Retornamos las dos mitades de la lista

def List_Merge(lista_izq, lista_der, metodo, orden):
    merged = None

    while lista_izq and lista_der:
        if orden == "ascendente":
            if metodo(lista_izq.data) <= metodo(lista_der.data):
                merged = List_Insert_End(merged, lista_izq.data)
                lista_izq = lista_izq.next
            else:
                merged = List_Insert_End(merged, lista_der.data)
                lista_der = lista_der.next
        if orden == "descendente":
            if metodo(lista_izq.data) >= metodo(lista_der.data):
                merged = List_Insert_End(merged, lista_izq.data)
                lista_izq = lista_izq.next
            else:
                merged = List_Insert_End(merged, lista_der.data)
                lista_der = lista_der.next

    while lista_izq:
        merged = List_Insert_End(merged, lista_izq.data)
        lista_izq = lista_izq.next

    while lista_der:
        merged = List_Insert_End(merged, lista_der.data)
        lista_der = lista_der.next

    return merged

def List_Merge_Sort(lista, metodo, orden):
    if List_Size(lista) <= 1: # caso base: si la lista tiene 0 o 1 elemento, ya está ordenada
        return lista # retorna la lista tal cual

    izq, der = List_Divide(lista) # divide la lista en dos mitades
    lista_izq = List_Merge_Sort(izq, metodo, orden) # ordena la mitad izquierda
    lista_der = List_Merge_Sort(der, metodo, orden) # ordena la mitad derecha

    return List_Merge(lista_izq, lista_der, metodo, orden) # junta las dos mitades ordenadas