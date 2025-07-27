import copy

class LDE():
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

def List_Insert(lista, llave):
    nuevo_nodo = LDE(llave)
    nuevo_nodo.next = lista # el puntero next del nuevo nodo apunta a la cabeza
    if lista: # si la cabeza es None (no hay un nodo después) no entra en este if
        lista.prev = nuevo_nodo # el puntero prev de la cabeza apunta al nuevo nodo
    return nuevo_nodo

def List_Insert_End(head: LDE, data: LDE) -> object:
    """
    Inserta al final de la lista doblemente enlazada un objecto
    """
    nuevo = LDE(data)
    if head is None:
        return nuevo
    actual = head
    while actual.next:
        actual = actual.next
    actual.next = nuevo
    nuevo.prev = actual
    return head

def List_Print(head: LDE):
    nodo_actual = head
    while nodo_actual:
        print(nodo_actual.getData().getID(), end=" <-> ")  
        nodo_actual = nodo_actual.next  
    print("None")

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

#--------------------------------------Insertion sort LDE-------------------------------------

    def lde_insertion_sort(self, head):
        key=head.next
        while key:
            i=key.prev
            #Aqui se debe poner el metodo para extraer el atributo de los objetos que se quiere comparar
            while i and key.data>=i.data:
                #Copia del valor de key, se usa para intercambiar el valor de i y key sin problemas
                key_0=copy.copy(key)
                if key.data==i.data:
                    #Aqui se debe poner el metodo para extraer el atributo a comparar en caso de empate
                    if key.data>=i.data:
                        key.data=i.data
                        i.data=key_0.data
                        #Este if verifica si i NO es el primer elemento de la lista, ya que si lo fuera
                        #no tendria sentido asignarle a key la primera posicion de la lista, porque esto causaria una verificacion extra innecesaria
                        if i.prev:
                            key=i
                        i=i.prev
                    else:
                        i=i.prev
                else:
                    key.data=i.data
                    i.data=key_0.data
                    if i.prev:
                        key=i
                    i=i.prev        
            key=key.next
        return head

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
