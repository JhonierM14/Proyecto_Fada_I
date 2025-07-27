import copy

class LDE():

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
                lista_izq = List_Insert_End(lista_izq, lista.data)
            else:
                lista_der = List_Insert_End(lista_der, lista.data)
            lista = lista.next
            contador += 1

        return lista_izq, lista_der

    def List_Merge(self, lista_izq, lista_der):
        merged = None

        while lista_izq and lista_der:
            if lista_izq.data <= lista_der.data:
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

    def List_Merge_Sort(self, lista):
        if self.List_Size(lista) <= 1: # caso base: si la lista tiene 0 o 1 elemento, ya está ordenada
            return lista # retorna la lista tal cual

        izq, der = self.List_Divide(lista) # divide la lista en dos mitades
        lista_izq = self.List_Merge_Sort(izq) # ordena la mitad izquierda
        lista_der = self.List_Merge_Sort(der) # ordena la mitad derecha

        return self.List_Merge(lista_izq, lista_der) # junta las dos mitades ordenadas
    
    def List_Merge_Sort_Experticia(self, lista):
        """
        Merge sort para ordenar encuestados por experticia (descendente)
        En caso de empate, ordenar por ID (ascendente)
        """
        if self.List_Size(lista) <= 1:
            return lista

        izq, der = self.List_Divide(lista)
        lista_izq = self.List_Merge_Sort_Experticia(izq)
        lista_der = self.List_Merge_Sort_Experticia(der)

        return self.List_Merge_Experticia(lista_izq, lista_der)

    def List_Merge_Experticia(self, lista_izq, lista_der):
        """
        Fusiona dos listas ordenadas por experticia (descendente)
        En caso de empate, ordenar por ID (descendente)
        """
        merged = None

        while lista_izq and lista_der:
            enc_izq = lista_izq.data
            enc_der = lista_der.data
            
            # Comparar por experticia (descendente), luego por ID (descendente - mayor ID)
            if (enc_izq.getExperticia() > enc_der.getExperticia() or 
                (enc_izq.getExperticia() == enc_der.getExperticia() and 
                 enc_izq.getID() > enc_der.getID())):
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

    def List_Insertion_Sort_Mediana(self, lista):
        """
        Insertion sort para ordenar preguntas por mediana (ascendente)
        En caso de empate, ordenar por ID de pregunta (ascendente)
        """
        if lista is None or lista.next is None:
            return lista
        
        current = lista.next
        
        while current:
            next_node = current.next
            current_data = current.data
            
            # Buscar la posición correcta para insertar current
            search_ptr = lista
            
            # Si current debe ir al principio
            if (current_data['mediana'] < search_ptr.data['mediana'] or
                (current_data['mediana'] == search_ptr.data['mediana'] and
                 current_data['id'] < search_ptr.data['id'])):
                
                # Remover current de su posición actual
                if current.next:
                    current.next.prev = current.prev
                current.prev.next = current.next
                
                # Insertar current al principio
                current.next = lista
                current.prev = None
                lista.prev = current
                lista = current
            else:
                # Buscar posición en el medio o al final
                while (search_ptr.next and 
                       (search_ptr.next.data['mediana'] < current_data['mediana'] or
                        (search_ptr.next.data['mediana'] == current_data['mediana'] and
                         search_ptr.next.data['id'] < current_data['id']))):
                    search_ptr = search_ptr.next
                
                # Si current ya está en la posición correcta, continuar
                if search_ptr.next == current:
                    current = next_node
                    continue
                
                # Remover current de su posición actual
                if current.next:
                    current.next.prev = current.prev
                current.prev.next = current.next
                
                # Insertar current después de search_ptr
                current.next = search_ptr.next
                if search_ptr.next:
                    search_ptr.next.prev = current
                search_ptr.next = current
                current.prev = search_ptr
            
            current = next_node
        
        return lista
    
    def List_Insertion_Sort_Consenso(self, lista):
        """
        Insertion sort para ordenar preguntas por consenso (descendente)
        En caso de empate, ordenar por ID de pregunta (ascendente)
        """
        if lista is None or lista.next is None:
            return lista
        
        current = lista.next
        
        while current:
            next_node = current.next
            current_data = current.data
            
            # Buscar la posición correcta para insertar current
            search_ptr = lista
            
            # Si current debe ir al principio (mayor consenso o menor ID en empates)
            if (current_data['consenso'] > search_ptr.data['consenso'] or
                (current_data['consenso'] == search_ptr.data['consenso'] and
                 current_data['id'] < search_ptr.data['id'])):
                
                # Remover current de su posición actual
                if current.next:
                    current.next.prev = current.prev
                current.prev.next = current.next
                
                # Insertar current al principio
                current.next = lista
                current.prev = None
                lista.prev = current
                lista = current
            else:
                # Buscar posición en el medio o al final
                while (search_ptr.next and 
                       (search_ptr.next.data['consenso'] > current_data['consenso'] or
                        (search_ptr.next.data['consenso'] == current_data['consenso'] and
                         search_ptr.next.data['id'] < current_data['id']))):
                    search_ptr = search_ptr.next
                
                # Si current ya está en la posición correcta, continuar
                if search_ptr.next == current:
                    current = next_node
                    continue
                
                # Remover current de su posición actual
                if current.next:
                    current.next.prev = current.prev
                current.prev.next = current.next
                
                # Insertar current después de search_ptr
                current.next = search_ptr.next
                if search_ptr.next:
                    search_ptr.next.prev = current
                search_ptr.next = current
                current.prev = search_ptr
            
            current = next_node
        
        return lista

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

