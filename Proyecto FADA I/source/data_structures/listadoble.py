import copy

class LDE(): # Clase LDE (Lista Doblemente Entrelazada)
    
    def __init__(self, data: object):
        self.data = data
        self.next = None
        self.prev = None
    
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def getPrev(self):
        return self.prev

    def List_Insert(self, lista, llave):
        nuevo_nodo = LDE(llave)
        nuevo_nodo.next = lista # el puntero next del nuevo nodo apunta a la cabeza
        if lista: # si la cabeza es None (no hay un nodo después) no entra en este if
            lista.prev = nuevo_nodo # el puntero prev de la cabeza apunta al nuevo nodo
        return nuevo_nodo

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
    def List_Size(self, lista):
        if lista is None:
            return 0
        size = 1
        actual = lista
        while actual.next is not None:
            size += 1
            actual = actual.next
        return size

    def List_Divide(self, lista):
        lista_izq = None
        lista_der = None
        full_size = self.List_Size(lista)
        mitad = full_size // 2
        contador = 0
        
        while contador < full_size:
            if contador < mitad:
                lista_izq = self.List_Insert_End(lista_izq, lista.data)
            else:
                lista_der = self.List_Insert_End(lista_der, lista.data)
            lista = lista.next
            contador += 1

        return lista_izq, lista_der

    def List_Merge(self, lista_izq, lista_der):
        merged = None

        while lista_izq and lista_der:
            if lista_izq.data <= lista_der.data:
                merged = self.List_Insert_End(merged, lista_izq.data)
                lista_izq = lista_izq.next
            else:
                merged = self.List_Insert_End(merged, lista_der.data)
                lista_der = lista_der.next

        while lista_izq:
            merged = self.List_Insert_End(merged, lista_izq.data)
            lista_izq = lista_izq.next

        while lista_der:
            merged = self.List_Insert_End(merged, lista_der.data)
            lista_der = lista_der.next

        return merged

    def List_Merge_Sort(self, lista):
        if self.List_Size(lista) <= 1: # caso base: si la lista tiene 0 o 1 elemento, ya está ordenada
            return lista # retorna la lista tal cual

        izq, der = self.List_Divide(lista) # divide la lista en dos mitades
        lista_izq = self.List_Merge_Sort(izq) # ordena la mitad izquierda
        lista_der = self.List_Merge_Sort(der) # ordena la mitad derecha

        return self.List_Merge(lista_izq, lista_der) # junta las dos mitades ordenadas
    
    # def List_Delete(head, L, key):
    #     if head is None:
    #         print("Doubly linked list is empty")
    #         return None

    #     if head.next is None:
    #         return None

    #     current = head
    #     while current.next.next:
    #         current = current.next

    #     del_node = current.next
    #     current.next = None
    #     del del_node
    #     return head

def List_Insert_End(head: LDE, data: LDE) -> object:
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
