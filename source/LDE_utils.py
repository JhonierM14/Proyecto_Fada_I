from data_structures.listadoble import *
from form.MedidasTenciaCentral import mediana
import time

#---------------------------------------------- PUNTO 3 ----------------------------------------------

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
    inicio = time.time()
    # Ordenar descendentemente la lista dependiendo del promedio del promedio de sus preguntas
    lista = List_Merge_Sort(lista, lambda e: Promedio_Tema(e.getPreguntas(), M), "descendente")
    resultado = ""

    while lista: # Mientras hayan temas
        # Concatenar al resultado el promedio de promedios del tema y su nombre
        resultado = resultado + f"{[Promedio_Tema(lista.data.getPreguntas(), M)]}" + " Tema " + f"{lista.data.getNombre()}:" + "\n"
        lista = lista.next # Avanzar al siguiente tema
    final = time.time()
    print("Ordenar temas " + f"{1000*(final - inicio):.10f}")
    return resultado # Retornamos los temas por orden descendente de sus promedios

#---------------------------------------------- PUNTO 5 ----------------------------------------------

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
                            return "Pregunta con mayor promedio de opinion: [" f"{lde_promedio(i.data.getEncuestados(), 1)}""] Pregunta: " f"{i.data.getNombre()}"
            
            i=i.next

        if i:
            key=i
        else:
            return "Pregunta con mayor promedio de opinion: [" f"{round(lde_promedio(key.data.getEncuestados(), 1), 2)}""] Pregunta: " f"{key.data.getNombre()}\n" 
    return "Pregunta con mayor promedio de opinion: [" f"{round(lde_promedio(key.data.getEncuestados(), 1), 2)}""] Pregunta: " f"{key.data.getNombre()}\n" 

#Es necesario llamar la funcion con una deep copy de la encuesta, ya que si no, se enviaría la encuesta como referencia,
#asi que cualquier cambio que le haga a encuesta_lde en la funcion tambien modificaría la encuesta_lde original y me dañaría los otros puntos.
#lde_punto5 tiene el string que debe salir en el output

#---------------------------------------------- PUNTO 6 ----------------------------------------------

def promedio_opinion(pregunta):
    nodo = pregunta.encuestados
    suma = 0
    count = 0
    while nodo:
        suma += nodo.data.opinion
        count += 1
        nodo = nodo.next
    return suma / count if count > 0 else 0

def punto6_LDE(encuesta):
    """
    Encuentra la pregunta con menor promedio de opiniones en toda la encuesta.
    """

    tiempo_inicio = time.time()
    resultado = ""
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
        resultado = f"Pregunta con menor promedio de opinion: [{round(promedio_opinion(menor_pregunta), 2)}] Pregunta: {menor_pregunta.nombre}\n"
    else:
        print("No se encontró ninguna pregunta.")

    tiempo_final = time.time()

    return resultado

#---------------------------------------------- PUNTO 7 ----------------------------------------------

# A esta función se le pasa la lista entrelazada con los temas
def Mayor_X_Pregunta(lista, K, M, dato):
    inicio = time.time()
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
        final = time.time()
        resultado = "Pregunta con mayor extremismo: " + f"{[Extremismo_Pregunta(mayor.data.getEncuestados())]}" + " Pregunta: " + mayor.data.getNombre() + "\n"
        print("extremismo: " +  f"{1000*(final - inicio):.10f}")
        return resultado
    if dato == "mediana":
        final = time.time()
        resultado = "Pregunta con mayor mediana de opinión: " + f"{[List_Median(List_Merge_Sort(mayor.data.getEncuestados(), lambda e: e.getOpinion(), "ascendente")).getOpinion()]}" + " Pregunta: " + mayor.data.getNombre() + "\n"
        print("mediana: " + f"{1000*(final - inicio):.10f}")
        return resultado

#---------------------------------------------- PUNTO 8 ----------------------------------------------

def punto8_LDE(encuesta):
    """
    Pregunta con menor mediana de opiniones
    En caso de empate, se usa la pregunta con menor identificador
    Retorna un string con el resultado
    """

    # Crear una lista doblemente enlazada para almacenar las preguntas con su mediana
    head_preguntas = None
    pregunta_id = 1
    
    # Cargar preguntas directamente en la LDE
    for tema_idx, tema in enumerate(encuesta._iterate_temas(), 1):
        for pregunta_idx, pregunta in enumerate(tema._iterate_preguntas(), 1):
            # Obtener opiniones de la pregunta
            opiniones = pregunta.get_opiniones()
            mediana_pregunta = mediana(opiniones)
            
            # Crear objeto pregunta con mediana para la lista
            pregunta_con_mediana = {
                'pregunta': pregunta,
                'mediana': mediana_pregunta,
                'tema_idx': tema_idx,
                'pregunta_idx': pregunta_idx,
                'id': pregunta_id,
                'nombre_completo': f"Pregunta {tema_idx}.{pregunta_idx}"
            }
            
            # Insertar directamente en lista doblemente enlazada
            head_preguntas = List_Insert_End(head_preguntas, pregunta_con_mediana)
            pregunta_id += 1
    
    # Usar el método de ordenamiento de la estructura LDE
    lde_sorter = LDE(None)  # Instancia para usar los métodos
    head_preguntas = lde_sorter.List_Insertion_Sort_Mediana(head_preguntas)
    
    # La primera pregunta en la lista ordenada tiene la menor mediana
    menor_mediana = head_preguntas.getData()
    return f"Pregunta con menor mediana de opinion: [{int(menor_mediana['mediana'])}] Pregunta: {menor_mediana['nombre_completo']}"

#---------------------------------------------- PUNTO 9 ----------------------------------------------

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
        map = List_Insert_End(LDE(key.data.getOpinion()), a)
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
            return "Pregunta con mayor moda de opinion: " + "[" + f"{lde_moda(key.data.getEncuestados()).data}" + "] Pregunta: " + key.data.getNombre() + "\n"
    return "Pregunta con mayor moda de opinion: " + "[" + f"{lde_moda(key.data.getEncuestados()).data}" + "] Pregunta: " + key.data.getNombre() + "\n"

#---------------------------------------------- PUNTO 10 ----------------------------------------------

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
          resultado = f"Pregunta con menor moda de opinion: [{moda_opinion(menor_pregunta)}] Pregunta: {menor_pregunta.nombre}\n"
     else:
          print("No se encontró ninguna pregunta.")


     tiempo_final = time.time()

     return resultado

#---------------------------------------------- PUNTO 11 ----------------------------------------------

# A esta función se le pasa la lista entrelazada con los encuestados
def Extremismo_Pregunta(lista):
    actual = lista # Obtenemos la lista de encuestados
    extremismo = 0 # Contador para saber cuantos encuestados tienen una opinion extrema

    while actual:
        if actual.data.getOpinion() == 0 or actual.data.getOpinion() == 10: # Si el encuestado tiene una opinion de 0 o 10
            extremismo += 1 # Se le suma 1 al extremismo
        actual = actual.next # Avanzamos al siguiente encuestado
        
    return round((extremismo / List_Size(lista)), 2) # Devuelve el porcentaje de encuestados que tienen una opinión de 0 o 10

#---------------------------------------------- PUNTO 12 ----------------------------------------------

def lde_consenso(pregunta):
    consenso = lde_moda(pregunta.data.getEncuestados()).next.data/List_Size(pregunta.data.getEncuestados())
    return consenso

def lde_mayor_consenso(encuesta):
    temas=encuesta.getTemas()
    key=None
    while temas:
        preguntas = temas.data.getPreguntas()
        key = lde_join(key, preguntas)
        temas=temas.next

    while key.next:
        i=key.next
        while i and lde_consenso(key) >= lde_consenso(i):
            if lde_consenso(key) == lde_consenso(i):
                if key.data.getNombre() <= i.data.getNombre():
                    i=i.next
                else:
                    if i.next:
                        key = i
                    else:
                        return "Pregunta con mayor consenso: " + "[" + f"{round(lde_consenso(i), 2)}" + "] Pregunta: " + f"{i.data.getNombre()}"
            else:
                i=i.next
                
        if i:
            key=i
        else:
            return "Pregunta con mayor consenso: " + "[" + f"{round(lde_consenso(key), 2)}" + "] Pregunta: " + f"{key.data.getNombre()}"
    #Si ocurre este caso, significa que la ultima pregunta es la que tiene el mayor consenso
    return "Pregunta con mayor consenso: " + "[" + f"{round(lde_consenso(key), 2)}" + "] Pregunta: " + f"{key.data.getNombre()}"