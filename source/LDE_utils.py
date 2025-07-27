import time, copy

from data_structures.listadoble import List_Median, List_Merge_Sort, List_Print, List_Size

def contar_encuestados_encuesta_LDE(temas):
    """
    Retorna el número total de encuestados en toda la encuesta (estructura LDE).
    """
    total = 0
    nodo_tema = temas
    while nodo_tema:
        tema = nodo_tema.data
        nodo_pregunta = tema.preguntas
        while nodo_pregunta:
            pregunta = nodo_pregunta.data
            nodo_encuestado = pregunta.encuestados
            while nodo_encuestado:
                total += 1
                nodo_encuestado = nodo_encuestado.next
            nodo_pregunta = nodo_pregunta.next
        nodo_tema = nodo_tema.next
    return total

#Punto 1: Ordenar encuestados de la pregunta ascendentemente segun su opinion
#Insertion sort: lde
def lde_insertion_sort(head):
    key=head.next
    while key:
        i=key.prev
        while i and key.data.getOpinion()>=i.data.getOpinion():
            key_0=copy.copy(key)
            if key.data.getOpinion()==i.data.getOpinion():
                if key.data.getExperticia()>i.data.getExperticia():
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

#Sirve para pasar una lde a un string con las ids de los encuestados
def lde_displayID(head):
    current = head
    str=""
    while current:
        str = str + f"{current.data.getID()}"+ " <-> "
        current = current.next
    str=str+"None"
    return str

def lde_escribir_opiniones(encuesta):
    temas=encuesta.getTemas()
    str = ""
    while temas:
        str=str+("Tema "+f"{temas.data.getNombre()}:"+"\n")
        preguntas = temas.data.getPreguntas()
        while preguntas:
            head = lde_insertion_sort(preguntas.data.getEncuestados())
            str=str +"Pregunta "+f"{preguntas.data.getNombre()}: "+f"{lde_displayID(head)}"+"\n"
            preguntas=preguntas.next
        temas=temas.next
    return str

#Esta es la salida de los encuestados de todas las preguntas de todos los temas ordenados
# lde_print = (lde_escribir_opiniones(encuesta_lde)

#Punto 2

def promedio_tema(tema):
    """
    Calcula el promedio del promedio de opiniones de todas las preguntas del tema.
    """
    nodo_pregunta = tema.preguntas
    suma_promedios = 0
    count = 0

    while nodo_pregunta:
        pregunta = nodo_pregunta.data
        suma_promedios += promedio_opinion(pregunta)
        count += 1
        nodo_pregunta = nodo_pregunta.next

    return suma_promedios / count if count > 0 else 0

def ordenar_preguntas_por_promedio_opinion(preguntas):
    """
    Ordena una lista doblemente enlazada de preguntas por promedio de opinión descendente.
    """
    if preguntas is None or preguntas.next is None:
        return preguntas  # ya está ordenada o vacía

    nueva_cabeza = None

    actual = preguntas
    while actual:
        siguiente = actual.next
        actual.prev = actual.next = None  # desconectar temporalmente

        if nueva_cabeza is None:
            nueva_cabeza = actual
        else:
            # insertar actual en nueva_cabeza de forma ordenada
            nodo = nueva_cabeza
            anterior = None
            while nodo:
                p1 = promedio_opinion(actual.data)
                p2 = promedio_opinion(nodo.data)
                if p1 > p2:
                    break
                elif p1 == p2:
                    # empate: promedio de experticia
                    e1 = promedio_experticia(actual.data)
                    e2 = promedio_experticia(nodo.data)
                    if e1 > e2:
                        break
                    elif e1 == e2:
                        n1 = contar_encuestados(actual.data)
                        n2 = contar_encuestados(nodo.data)
                        if n1 > n2:
                            break
                anterior = nodo
                nodo = nodo.next
            if anterior is None:
                actual.next = nueva_cabeza
                nueva_cabeza.prev = actual
                nueva_cabeza = actual
            else:
                actual.next = anterior.next
                if anterior.next:
                    anterior.next.prev = actual
                anterior.next = actual
                actual.prev = anterior

        actual = siguiente

    return nueva_cabeza

def mostrar_ids_encuesta_completa(temas):
    """
    Muestra en una única línea los IDs de todos los encuestados que respondieron en toda la encuesta (LDE).
    """

    nodo_tema = temas
    while nodo_tema:
        tema = nodo_tema.data
        nodo_pregunta = tema.preguntas
        while nodo_pregunta:
            pregunta = nodo_pregunta.data
            imprimir_ids_encuestados_lde(pregunta.encuestados)
            nodo_pregunta = nodo_pregunta.next
        nodo_tema = nodo_tema.next

    print() 

def imprimir_ids_encuestados_lde(nodo):
    """
    Imprime los IDs de una LDE de encuestados
    """
    while nodo:
        print(nodo.data.id, end=" ")
        nodo = nodo.next

def punto2_LDE(encuesta):
    """
    Por cada tema, se busca que las preguntas estén ordenadas 
    descendentemente según su promedio del valor de opinión.
    La salida se imprime por tema y por pregunta, mostrando sus promedios.
    """
    tiempo_inicio = time.time()

    nodo_tema = encuesta.Temas
    while nodo_tema:
        tema = nodo_tema.data
        tema.preguntas = ordenar_preguntas_por_promedio_opinion(tema.preguntas)
        print(f"[{round(promedio_tema(tema), 2)}] Tema {tema.nombre}:")
        nodo_pregunta = tema.preguntas
        while nodo_pregunta:
            pregunta = nodo_pregunta.data
            prom = round(promedio_opinion(pregunta), 2)
            print(f"[{prom}] Pregunta {pregunta.nombre}")
            List_Print(pregunta.encuestados)
            nodo_pregunta = nodo_pregunta.next

        nodo_tema = nodo_tema.next

    mostrar_ids_encuesta_completa(encuesta.Temas)

    tiempo_final = time.time()

    return contar_encuestados_encuesta_LDE(encuesta.Temas), tiempo_final - tiempo_inicio

#Punto 3

# A esta función se le pasa la lista entrelazada con los encuestados
def Promedio_Pregunta(lista):
    actual = lista # Obtenemos la lista de encuestados
    opinion = 0 # Contador para ir sumando las opiniones de los encuestados

    while actual: # Mientras hayan encuestados
        opinion += actual.data.getOpinion() # Sumar al contador la opinión del encuestado
        actual = actual.next # Avanzar al siguiente encuestado
        
    return round((opinion / List_Size(lista)), 2) # Devolver el promedio de las opiniones de los encuestados

# A esta función se le pasa la lista entrelazada con las preguntas
def Promedio_Tema(lista, M):
    pregunta_actual = lista # Obtenemos la lista de preguntas
    promedio = 0 # Contador para ir sumando los promedios de las preguntas

    while pregunta_actual:
        promedio += Promedio_Pregunta(pregunta_actual.data.getEncuestados()) # Sumamos el promedio de la pregunta al contador
        pregunta_actual = pregunta_actual.next # Cambiamos a la siguiente pregunta
        
    return round(promedio / M, 2) # Retornamos el promedio de los promedios de las preguntas

# A esta función se le pasa la lista entrelazada con los temas
def Ordenar_Tema_Por_Promedio(lista, M):
    # Ordenar descendentemente la lista dependiendo del promedio del promedio de sus preguntas
    lista = List_Merge_Sort(lista, lambda e: Promedio_Tema(e.getPreguntas(), M), "descendente")
    resultado = ""

    while lista: # Mientras hayan temas
        # Concatenar al resultado el promedio de promedios del tema y su nombre
        resultado = resultado + f"{[Promedio_Tema(lista.data.getPreguntas(), M)]}" + " Tema " + f"{lista.data.getNombre()}:" + "\n"
        lista = lista.next # Avanzar al siguiente tema

    print(resultado)
    return resultado # Retornamos los temas por orden descendente de sus promedios

#Punto 4

def punto4_LDE():
     pass

#Punto 5
#Punto 5: Pregunta con mayor promedio de opiniones. 
#LDE:
#Funcion auxliar que calcula el promedio de un grupo de encuestados, segun su opinion o experticia
def lde_promedio(encuestados, method):
    total: int=0
    a: int = 0
    if method == 1:
        while encuestados:
            a=a+1
            total=total+encuestados.data.getOpinion()
            encuestados=encuestados.next
    elif method == 2:
            while encuestados:
                a=a+1
                total=total+encuestados.data.getExperticia()
                encuestados=encuestados.next
    else:
        return None
    return total/a

#Funcion principal que retorna la pregunta con mayor promedio
def lde_mayor_promedio(encuesta):
    temas=encuesta.getTemas()
    key=None
    while temas:
        preguntas = temas.data.getPreguntas()
        key = lde_join(key, preguntas)
        temas=temas.next

    while key.next:
        i=key.next
        while i and lde_promedio(key.data.getEncuestados(), 1) >= lde_promedio(i.data.getEncuestados(), 1):
            if lde_promedio(key.data.getEncuestados(), 1) == lde_promedio(i.data.getEncuestados(), 1):
                #Se calcula el promedio de las experticias y se almacena para no tener que calcular 2 veces despues
                prom_exp_key = lde_promedio(key.data.getEncuestados(), 2)
                prom_exp_i = lde_promedio(i.data.getEncuestados(), 2)
                #Comparacion de las experticias para el desempate
                if  prom_exp_key > prom_exp_i:
                    i=i.next
                elif prom_exp_key < prom_exp_i:
                    if i.next:
                        key=i
                    else:
                        #Si no hay i.next, significa que i es la ultima pregunta de la lista, 
                        #por lo cual no hay mas preguntas para comparar y se debe retornar i al ser mayor que key.
                        return "Pregunta de la encuesta con mayor promedio: [" f"{lde_promedio(i.data.getEncuestados(), 1)}""] Pregunta: " f"{i.data.getNombre()}"
                else:
                    #Comparacion del numero de encuestados de las preguntas para el segundo desempate. Si en este caso todavía
                    #hay empate, se toma la pregunta mas a la izquierda (key) como la que tiene mayor promedio.
                    if List_Size(key) >= List_Size(i):
                        i=i.next
                    else:
                        if i.next:
                            key=i
                        else:
                            return "Pregunta de la encuesta con mayor promedio: [" f"{lde_promedio(i.data.getEncuestados(), 1)}""] Pregunta: " f"{i.data.getNombre()}"
            
            i=i.next

        if i:
            key=i
        else:
            return "Pregunta de la encuesta con mayor promedio: [" f"{lde_promedio(key.data.getEncuestados(), 1)}""] Pregunta: " f"{key.data.getNombre()}" 
    return "Pregunta de la encuesta con mayor promedio: [" f"{lde_promedio(key.data.getEncuestados(), 1)}""] Pregunta: " f"{key.data.getNombre()}" 

#Es necesario llamar la funcion con una deep copy de la encuesta, ya que si no, se enviaría la encuesta como referencia,
#asi que cualquier cambio que le haga a encuesta_lde en la funcion tambien modificaría la encuesta_lde original y me dañaría los otros puntos.
#lde_punto5 tiene el string que debe salir en el output
# lde_punto5 = lde_mayor_promedio(copy.deepcopy(encuesta_lde))

#Punto 6

def punto6_LDE(encuesta):
    """
    Encuentra la pregunta con menor promedio de opiniones en toda la encuesta.
    """

    tiempo_inicio = time.time()

    nodo_tema = encuesta.Temas
    menor_pregunta = None

    while nodo_tema:
        nodo_pregunta = nodo_tema.data.preguntas
        while nodo_pregunta:
            p = nodo_pregunta.data
            if menor_pregunta is None or promedio_opinion(p) < promedio_opinion(menor_pregunta):
                menor_pregunta = p
            nodo_pregunta = nodo_pregunta.next
        nodo_tema = nodo_tema.next

    if menor_pregunta:
        print(f"La pregunta con menor promedio es '{menor_pregunta.nombre}' con promedio {round(promedio_opinion(menor_pregunta), 2)}")
    else:
        print("No se encontró ninguna pregunta.")

    tiempo_final = time.time()

    return contar_encuestados_encuesta_LDE(encuesta.Temas), tiempo_final - tiempo_inicio

#Punto 8

def punto8_LDE():
     pass

#Punto 9

#Funcion para encontrar la moda de la opinion de los encuestados de una pregunta
def lde_moda(encuestados):
    repeticiones=None  
    key=encuestados
    
    while key:
        i=key.next
        a=1
        while i:
            if key.data.getOpinion()==i.data.getOpinion():
                a=a+1
            i=i.next         
        map = List_Insert_End(lde(key.data.getOpinion()), a)
        repeticiones = List_Insert_End(repeticiones, map)
        key=key.next
    
    #Repeticiones es la LDE que contiene las opiniones de los encuestados junto a su numero de repeticiones
    key = repeticiones
    while key.next:
        #print(key.data.data, key.data.next.data)
        i=key.next
        while i and key.data.next.data >= i.data.next.data:
            #Se comparan las repeticiones para hallar la moda
            if key.data.next.data > i.data.next.data:
                i=i.next
            #Si hay mas de una moda, se compara el valor de la moda, y se toma como moda el menor de todos
            elif key.data.data <= i.data.data:
                    i=i.next
            elif i:
                key = i
            else:
                return key.data
        if i:
            key = i
        else:
            return key.data
    return key.data

#Funcion principal que retorna la pregunta de la encuesta con mayor moda de opiniones
def lde_mayor_moda(encuesta):
    temas=encuesta.getTemas()
    key=None
    while temas:
        preguntas = temas.data.getPreguntas()
        key = lde_join(key, preguntas)
        temas=temas.next
    while key.next:
        i = key.next
        while i and lde_moda(key.data.getEncuestados()).data >= lde_moda(i.data.getEncuestados()).data :
            if lde_moda(key.data.getEncuestados()).data == lde_moda(i.data.getEncuestados()).data:
                if key.data.getNombre() <= i.data.getNombre():
                    i=i.next
                else:
                    if i.next:
                        key = i
                    else:
                        return "Pregunta con mayor moda de opinion: " + "[" + f"{lde_moda(i.data.getEncuestados()).data}"+"] Pregunta: " + i.data.getNombre()
            else:
                i=i.next

        if i:
            key = i
        else:
            return "Pregunta con mayor moda de opinion: " + "[" + f"{lde_moda(key.data.getEncuestados()).data}" + "] Pregunta: " + key.data.getNombre()
    return "Pregunta con mayor moda de opinion: " + "[" + f"{lde_moda(key.data.getEncuestados()).data}" + "] Pregunta: " + key.data.getNombre()

#La salida
# lde_punto9 = lde_mayor_moda(copy.deepcopy(encuesta_lde))

#Punto 10

def punto10_LDE(encuesta):
     """
     Encuentra y muestra la pregunta con el menor valor de moda de opiniones
     en toda la encuesta, recorriendo todos los temas y preguntas.
     """
     tiempo_inicio = time.time()
     
     nodo_tema = encuesta.Temas
     menor_pregunta = None

     while nodo_tema:
          nodo_pregunta = nodo_tema.data.preguntas
          while nodo_pregunta:
               p = nodo_pregunta.data
               if menor_pregunta is None or moda_opinion(p) < moda_opinion(menor_pregunta):
                    menor_pregunta = p
               nodo_pregunta = nodo_pregunta.next
          nodo_tema = nodo_tema.next

     if menor_pregunta:
          print(f"La pregunta con menor moda es '{menor_pregunta.nombre}' con moda {moda_opinion(menor_pregunta)}")
     else:
          print("No se encontró ninguna pregunta.")


     tiempo_final = time.time()

     return contar_encuestados_encuesta_LDE(encuesta.Temas), tiempo_final - tiempo_inicio

def promedio_opinion(pregunta):
    nodo = pregunta.encuestados
    suma = 0
    count = 0
    while nodo:
        suma += nodo.data.opinion
        count += 1
        nodo = nodo.next
    return suma / count if count > 0 else 0

def promedio_experticia(pregunta):
    nodo = pregunta.encuestados
    suma = 0
    count = 0
    while nodo:
        suma += nodo.data.experticia
        count += 1
        nodo = nodo.next
    return suma / count if count > 0 else 0

def contar_encuestados(pregunta):
    nodo = pregunta.encuestados
    count = 0
    while nodo:
        count += 1
        nodo = nodo.next
    return count

def moda_opinion(pregunta):
    frec = [0] * 11
    nodo = pregunta.encuestados
    while nodo:
        frec[nodo.data.opinion] += 1
        nodo = nodo.next
    max_frec = max(frec)
    for i in range(11):
        if frec[i] == max_frec:
            return i

#Punto 11

# A esta función se le pasa la lista entrelazada con los encuestados
def Extremismo_Pregunta(lista):
    actual = lista # Obtenemos la lista de encuestados
    extremismo = 0 # Contador para saber cuantos encuestados tienen una opinion extrema

    while actual:
        if actual.data.getOpinion() == 0 or actual.data.getOpinion() == 10: # Si el encuestado tiene una opinion de 0 o 10
            extremismo += 1 # Se le suma 1 al extremismo
        actual = actual.next # Avanzamos al siguiente encuestado
        
    return round((extremismo / List_Size(lista)), 2) # Devuelve el porcentaje de encuestados que tienen una opinión de 0 o 10

# A esta función se le pasa la lista entrelazada con los temas
def Mayor_X_Pregunta(lista, K, M, dato):
    if lista is None:
        return 0
    temas = K # Obtenemos cuántos temas hay
    tema_actual = lista # Obtenemos la lista de temas
    preguntas_actuales = tema_actual.data.getPreguntas() # Obtenemos la lista de preguntas del primer tema como base
    mayor = preguntas_actuales # Por si hay empate de extremismo, se toma la pregunta con menor id

    while temas > 0:
        preguntas = M # Obtenemos cuántas preguntas hay en cada tema
        while preguntas > 0:
            if dato == "extremismo":
                if Extremismo_Pregunta(mayor.data.getEncuestados()) < Extremismo_Pregunta(preguntas_actuales.data.getEncuestados()):
                    mayor = preguntas_actuales # Actualizamos la pregunta con mayor extremismo
            if dato == "mediana":
                if List_Median(List_Merge_Sort(mayor.data.getEncuestados(), lambda e: e.getOpinion(), "ascendente")).getOpinion() < List_Median(List_Merge_Sort(preguntas_actuales.data.getEncuestados(), lambda e: e.getOpinion(), "ascendente")).getOpinion():
                    mayor = preguntas_actuales # Actualizamos la pregunta con mayor mediana
            preguntas_actuales = preguntas_actuales.next # Cambiamos a la siguiente pregunta
            preguntas -= 1

        tema_actual = tema_actual.next # Cambiamos al siguiente tema
        if tema_actual: # 
            preguntas_actuales = tema_actual.data.getPreguntas() # Cambiamos a las preguntas del siguiente tema
        temas -= 1
        
    if dato == "extremismo":
        resultado = "Pregunta con mayor extremismo: " + f"{[Extremismo_Pregunta(mayor.data.getEncuestados())]}" + " Pregunta: " + mayor.data.getNombre() + "\n"
        print(resultado)
        return resultado
    if dato == "mediana":
        resultado = "Pregunta con mayor mediana de opinión: " + f"{[List_Median(List_Merge_Sort(mayor.data.getEncuestados(), lambda e: e.getOpinion(), "ascendente")).getOpinion()]}" + " Pregunta: " + mayor.data.getNombre() + "\n"
        print(resultado)
        return resultado

#Punto 12

def lde_mayor_consenso(encuesta):
    temas=encuesta.Temas
    key=None
    while temas:
        preguntas = temas.data.preguntas
        #print(preguntas.next.next.data.nombre)
        key = lde_join(key, preguntas)
        temas=temas.next

    while key.next:
        i=key.next
        while i and lde_moda(key.data.encuestados).next.data/List_Size(key.data.encuestados) >= lde_moda(i.data.encuestados).next.data/List_Size(i.data.encuestados):
            cons_key = lde_moda(key.data.encuestados).next.data/List_Size(key.data.encuestados)

            if cons_key == lde_moda(i.data.encuestados).next.data/List_Size(i.data.encuestados):
                if key.data.getNombre() <= i.data.getNombre():
                    i=i.next
                else:
                    if i.next:
                        key = i
                    else:
                        return "Pregunta con mayor consenso: " + "[" + f"{round(cons_key, 2)}" + "] Pregunta: " + f"{key.data.nombre}"
            else:
                i=i.next
                
        if i:
            key=i
        else:
            return "Pregunta con mayor consenso: " + "[" + f"{round(cons_key, 2)}" + "] Pregunta: " + f"{key.data.nombre}"
    #Si ocurre este caso, significa que la ultima pregunta es la que tiene el mayor consenso, y por la logica del
    #codigo esta sería la i, mientras que cons_key tendria el consenso de la pregunta con mayor consenso anterio
    cons_key = lde_moda(key.data.encuestados).next.data/List_Size(key.data.encuestados)
    return "Pregunta con mayor consenso: " + "[" + f"{round(cons_key, 2)}" + "] Pregunta: " + f"{key.data.nombre}"

#La salida
# lde_punto12 = lde_mayor_consenso(copy.deepcopy(encuesta_lde))

def seleccionarFuncionLDE(metodo: int):
     """
     1. ordenar los encuestrados en cada pregunta segun su valor de opinion. 
     2. por cada tema, ordenar las preguntas por su promedio del valor de opinion de forma descendente.
     3. ordenar los temas por el promedio de sus preguntas.
     4. ordenar a todos los encuestados segun su experticia.
     5. Pregunta con mayor promedio de opiniones.
     6. Pregunta con menor promedio de opiniones.
     7. Pregunta con mayor  mediana de opiniones.
     8. Pregunta con menor mediana  opiniones.
     9. Pregunta con el mayor valor de moda de opiniones.
     10. Pregunta con el menor valor de moda de opiniones.
     11. Pregunta con mayor valor de extremismo.
     12. Pregunta con mayor consenso
     """
     match metodo:
        case 1:
            pass
        case 2:
            return punto2_LDE
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            return punto6_LDE
        case 7:
            pass
        case 8:
            pass
        case 9:
            pass
        case 10:
            return punto10_LDE
        case 11:
            pass
        case 12:
            pass
        case _:
            raise ValueError("funcion no implementada.")
         
