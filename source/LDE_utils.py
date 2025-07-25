from controlador_LDE import *

#Punto 1: Ordenar encuestados de la pregunta ascendentemente segun su opinion
def punto1_LDE():
     # Se asigna a "lista" el arreglo que se quiere ordenar:
     lista: list = pregunta1_1.encuestados
     list_encuestados=[]
     for e in lista:
          list_encuestados.append(e.getID())
     print("Orden original: ", list_encuestados)

     for j in range(1, len(lista)):
          key=lista[len(lista)-j-1]
          i=len(lista)-j
          while i<len(lista) and key.getOpinion()<=lista[i].getOpinion():
               if key.getOpinion()==lista[i].getOpinion():
                    if key.getExperticia()>=lista[i].getExperticia():
                         #print(lista[i-1].getID())
                         #print(key.getID())
                         lista[i-1]=key
                         key=lista[i]
                    else:
                         lista[i-1]=lista[i]
               else:
                    lista[i-1]=lista[i]
               i=i+1
          lista[i-1]=key
          #print(lista)

     #Toca hacer esto para mostrar las ids
     list_encuestados=[]
     for e in lista:
          list_encuestados.append(e.getID())

     print("Nuevo orden: ", list_encuestados)

#Punto 2

def punto2_LDE():
     """
     por cada tema, se busca que las preguntas estén ordenadas 
     descendentemente según su promedio del valor de opinión
     """

     for tema in prueba.getTemas():
          print(f"[{tema.getPromedioAllPreguntas()}]{tema.getNombre()}:")
          for pregunta in tema.getPreguntas():
               print(f"[{pregunta.getPromedioPregunta()}] {pregunta.getNombre()}: {pregunta.getIDS()}\n")
     print(f"Lista de encuestados")

     print(prueba.getIDSEncuestadosEncuesta())
     
     print("#################################")

punto2_LDE()

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
#Funcion auxliar que calcula el promedio de un grupo de encuestados, segun su opinion o experticia
def lde_promedio(encuestados, method):
    total: int=0
    a: int = 0
    if method == "opinion":
        while encuestados:
            a=a+1
            total=total+encuestados.data.getOpinion()
            encuestados=encuestados.next
    else:
        if method == "experticia":
            while encuestados:
                a=a+1
                total=total+encuestados.data.getExperticia()
                encuestados=encuestados.next
    return total/a

#La funcion recibe una encuesta y extrae los 
def punto5_LDE(encuesta):
    temas=encuesta.getTemas()
    key=None
    while temas:
        preguntas = temas.data.getPreguntas()
        key = lde_join(key, preguntas)
        temas=temas.next

    while key.next:
        i=key.next
        while i and lde_promedio(key.data.getEncuestados(), "opinion") >= lde_promedio(i.data.getEncuestados(), "opinion"):
            if lde_promedio(key.data.getEncuestados(), "opinion") == lde_promedio(i.data.getEncuestados(), "opinion"):
                #Comparacion de las experticias para el desempate
                if lde_promedio(key.data.getEncuestados(), "experticia") > lde_promedio(i.data.getEncuestados(), "experticia"):
                    i=i.next
                elif lde_promedio(key.data.getEncuestados(), "experticia") < lde_promedio(i.data.getEncuestados(), "experticia"):
                    if i.next:
                        key=i
                    else:
                        #Si no hay i.next, significa que i es la ultima pregunta de la lista, 
                        #por lo cual no hay mas preguntas para comparar y se debe retornar i al ser mayor que key.
                        return List_Insert_End(lde(i), lde_promedio(i.data.getEncuestados(), "opinion"))
                elif lde_promedio(key.data.getEncuestados(), "experticia") == lde_promedio(i.data.getEncuestados(), "experticia"):
                    #Comparacion del numero de encuestados de las preguntas para el segundo desempate. Si en este caso todavía
                    #hay empate, se toma la pregunta mas a la izquierda (key) como la que tiene mayor promedio.
                    if List_Size(key) >= List_Size(i):
                        i=i.next
                    else:
                        if i.next:
                            key=i
                        else:
                            return List_Insert_End(lde(i), lde_promedio(i.data.getEncuestados(), "opinion"))   
            i=i.next

        if i:
            key=i
        else:
            return List_Insert_End(lde(key), lde_promedio(key.data.getEncuestados(), "opinion"))   
    return List_Insert_End(lde(key), lde_promedio(key.data.getEncuestados(), "opinion"))   

#Es necesario llamar la funcion con una deep copy de la encuesta, ya que si no, se enviaría la encuesta como referencia,
#asi que cualquier cambio que le haga a encuesta_lde en la funcion tambien modificaría la encuesta_lde original y me dañaría los otros puntos.
lde_punto5 = punto5_LDE(copy.deepcopy(encuesta_lde))

print("Pregunta de la encuesta con mayor promedio:",
       "["f"{lde_punto5.next.data}""]" ,lde_punto5.data.data.getNombre())

#Punto 6

def punto6_LDE():
     print("#################################")

#Punto 8

def punto8_LDE():
     pass

#Punto 9

def punto9_LDE():
     pass

#Punto 10

def punto10_LDE():
     print("#################################")

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

def punto12_LDE():
     pass
