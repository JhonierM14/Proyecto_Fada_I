from data_structures.abb import *
from form.encuestado import Encuestado
from form.MedidasTenciaCentral import promedio
from data_structures.abb import abb_mediana
from form.MedidasTenciaCentral import mediana
import time
import copy

#---------------------------------------------- PUNTO 3 ----------------------------------------------

#Punto 1 con abb:
encuestado1 = Encuestado(1, "Sofía", 1, 6)
encuestado2 = Encuestado(2, "Alejandro", 7, 10)
encuestado3 = Encuestado(3, "Valentina", 9, 0)
encuestado4 = Encuestado(4, "Juan", 10, 1)
encuestado5 = Encuestado(5, "Martina", 7, 0)
encuestado6 = Encuestado(6, "Sebastián", 8, 9)
encuestado7 = Encuestado(7, "Camila", 2, 7)
encuestado8 = Encuestado(8, "Mateo", 4, 7)
encuestado9 = Encuestado(9, "Isabella", 7, 5)
encuestado10 = Encuestado(10, "Daniel", 2, 9)
encuestado11 = Encuestado(11, "Luciana", 1, 7)
encuestado12 = Encuestado(12, "Lucas", 6, 8)

lista: list = [encuestado1, encuestado2, encuestado3, encuestado4, encuestado5, encuestado6, encuestado7, encuestado8, encuestado9, encuestado10, encuestado11, encuestado12]

#Funcion propia que reemplaza el len de python
def cant(lst):
    a=0
    while lst:
        a=a+1
        lst.pop(0)
    return a 

#Funcion que retorna el abb con los encuestados ya ordenados
def abb_encuestados(lst):
    i=1
    root=abb(lst[0])
    while i<cant(copy.copy(lst)):
        abb_insert_encuestados(root, lst[i])
        i=i+1
    return root

#Insertar los encuestados en un abb segun su opinion, o experticia en caso de empate
def abb_insert_encuestados(root, key):
    if root is None:
        return abb(key)
    
    if root.val.getOpinion()>key.getOpinion():
        if root.left == None:
            root.left = abb(key)
        else:
           abb_insert_encuestados(root.left, key) 
     
    if root.val.getOpinion()==key.getOpinion():
        if root.val.getExperticia()>=key.getExperticia():
            if root.left == None:
                root.left = abb(key)
            else:
               abb_insert_encuestados(root.left, key) 
        else:
           if root.right == None:
               root.right = abb(key)
           else:
               abb_insert_encuestados(root.right, key)  
    
    if root.val.getOpinion()<key.getOpinion():
        if root.right == None:
            root.right = abb(key)
        else:
            abb_insert_encuestados(root.right, key)

#Sirve para imprimir la id de los encuestados en orden descendente segun su opinion
def inorder_encuestados(root):
    if root is None:
        return root
    inorder_encuestados(root.right)
    print(root.val.getID(), end=" ")
    inorder_encuestados(root.left)

root = abb_encuestados(lista)
print("Encuestados de la pregunta 1 (con abb): ")
inorder_encuestados(root)
print(" ")
#---------------------------------------------- PUNTO 2 ----------------------------------------------

#---------------------------------------------- PUNTO 3 ----------------------------------------------

# A esta función se le pasa el árbol binario de búsqueda con los encuestados
def Suma_Raices(arbol, metodo):
    if arbol is None:
        return 0
    return metodo(arbol.val) + Suma_Raices(arbol.left, metodo) + Suma_Raices(arbol.right, metodo)

# A esta función se le pasa el árbol binario de búsqueda con los encuestados
def Promedio_Pregunta(arbol):
    if arbol is None:
        return 0
    total_encuestados = Arb_Size(arbol)
    suma_opiniones = Suma_Raices(arbol, lambda x: x.getOpinion())
    return round(suma_opiniones/total_encuestados, 2)

# A esta función se le pasa el árbol binario de búsqueda con las preguntas
def Promedio_Preguntas(arbol):
    if arbol is None:
        return 0
    total_preguntas = Arb_Size(arbol)
    suma_preguntas = Suma_Raices(arbol, lambda x: Promedio_Pregunta(x.getEncuestados()))
    return round(suma_preguntas/total_preguntas, 2)

# A esta función se le pasa el árbol vinario de busqueda con los temas
def Temas_Print(nodo):
    if nodo is None:
        return ""
    resultado = ""
    resultado = resultado + Temas_Print(nodo.right)
    resultado = resultado + "[" + str(Promedio_Preguntas(nodo.val.getPreguntas())) + "] " + "Tema " + str(nodo.val.getNombre()) + ":\n"
    resultado = resultado + Temas_Print(nodo.left)
    return resultado

# A esta funcion se le pasa el árbol binario de búsqueda con los temas
def Ordenar_Tema_Por_Promedio(arbol):
    inicio = time.time()
    actual = arbol  # Obtenemos el árbol de temas
    arbol_temas = abb(actual.val) # Guardamos el primer tema como base

    while actual.right: # Mientras hayan temas
        actual = actual.right # Avanzar al siguiente tema
        arbol_temas = Arb_Insert(arbol_temas, actual.val, lambda e: Promedio_Preguntas(e.getPreguntas()))

    resultado = Temas_Print(arbol_temas) # Guardamos el print del resultado de ordenar los temas
    final = time.time()
    print("Ordenar temas " + f"{1000*(final - inicio):.10f}")
    return resultado
#---------------------------------------------- PUNTO 4 ----------------------------------------------

#---------------------------------------------- PUNTO 5 ----------------------------------------------

def abb_promedios(preguntas):
    encuestados = []
    abb_to_array(encuestados, preguntas[0].getEncuestados())
    preguntas[0].setEncuestados(encuestados)
    root= abb(preguntas[0])    
    i=1
    while i<cant(copy.copy(preguntas)):
        encuestados = []
        abb_to_array(encuestados, preguntas[i].getEncuestados())
        preguntas[i].setEncuestados(encuestados)
        abb_insert_promedios(root, abb(preguntas[i]))
        i=i+1
    return root

def abb_insert_promedios(root, pregunta):
    prom_root = promedio(root.val.getOpiniones())
    prom2 = promedio(pregunta.val.getOpiniones())
    exp_root = promedio(root.val.getExperticias())
    exp2 = promedio(pregunta.val.getExperticias())
    
    if prom_root < prom2:
        if root.right == None:
            root.right = pregunta
        else:
            abb_insert_promedios(root.right, pregunta)
    elif prom_root == prom2:
        if exp_root < exp2:
            if root.right == None:
                root.right = pregunta
            else:
                abb_insert_promedios(root.right, pregunta)
        elif exp_root>=exp2:
                if root.left == None:
                    root.left= pregunta
                else:
                    abb_insert_promedios(root.left, pregunta)
        else:
            if cant(copy.copy(root.val.encuestados)) >= cant(copy.copy(pregunta.val.encuestados)):
                if root.left == None:
                    root.left = pregunta
                else:
                    abb_insert_promedios(root.left, pregunta)
            else:
                if root.right == None:
                    root.right= pregunta
                else:
                    abb_insert_promedios(root.right, pregunta)
    else:
        if root.left == None:
            root.left= pregunta
        else:
            abb_insert_promedios(root.left, pregunta)

def abb_mayor_promedio(encuesta):
    temas=[]
    copy.copy(abb_to_array(temas, encuesta.Temas))
    preguntas=[]
    i=0
    while i<cant(copy.copy(temas)):
        aux=[]
        abb_to_array(aux, temas[i].getPreguntas())
        preguntas = preguntas + aux
        i=i+1
    root=abb_promedios(preguntas)

    while root.right:
        root=root.right
    return "Pregunta con mayor promedio de opinion: ["+ f"{round(promedio(root.val.getOpiniones()), 2)}" + "] Pregunta: " + root.val.nombre + "\n"

#---------------------------------------------- PUNTO 6 ----------------------------------------------

def buscar_en_temas(nodo_tema, menor):
    if nodo_tema is None or nodo_tema.val is None:
        return menor

    menor = buscar_en_temas(nodo_tema.left, menor)
    tema = nodo_tema.val
    menor = buscar_pregunta_menor_promedio(tema.preguntas, menor)
    menor = buscar_en_temas(nodo_tema.right, menor)
    return menor

def punto6_Abb(encuesta):
    """
    Pregunta con menor promedio de opiniones
    """
    tiempo_inicio = time.time()

    pregunta_menor_prom = buscar_en_temas(encuesta.Temas, None)

    if pregunta_menor_prom:
        resultado = f"Pregunta con menor promedio de opinion: [{round(pregunta_menor_prom.promedio_opinion(), 2)}] Pregunta: {pregunta_menor_prom.getNombre()}\n"
    else:
        print("No se encontró ninguna pregunta.")

    tiempo_final = time.time()
    
    return resultado

#---------------------------------------------- PUNTO 7 ----------------------------------------------

# A esta función se le pasa el arbol de temas
def Mayor_X_Pregunta(arbol, K, M, dato):
    inicio = time.time()
    if arbol is None:
        return 0
    tema_actual = arbol # Obtenemos el arbol de temas
    temas = K # Obtenemos los temas totales
    preguntas_actuales = tema_actual.val.getPreguntas()
    mayor = preguntas_actuales # Obtenemos el extremismo de la primera pregunta del primer tema como base

    while temas > 0: # Mientras hayan temas
        preguntas = M # Reiniciar el contador de preguntas

        while preguntas > 0: # Mientras hayan preguntas

            if dato == "extremismo":
                posible_mayor = Extremismo_Pregunta(preguntas_actuales.val.getEncuestados())/Arb_Size(preguntas_actuales.val.getEncuestados())
                if Extremismo_Pregunta(mayor.val.getEncuestados())/Arb_Size(mayor.val.getEncuestados()) < posible_mayor: # Si el posible es mayor, será el nuevo extremismo
                    mayor = preguntas_actuales
            if dato == "mediana":
                posible_mayor = Arb_Median(preguntas_actuales.val.getEncuestados(), lambda e: e.getOpinion())
                if Arb_Median(mayor.val.getEncuestados(), lambda e: e.getOpinion()).getOpinion() < posible_mayor.getOpinion():
                    mayor = preguntas_actuales

            preguntas_actuales = preguntas_actuales.right # Avanzamos a la siguiente pregunta
            preguntas -= 1

        tema_actual = tema_actual.right # Avanzamos al siguiente tema
        if tema_actual is not None:
            preguntas_actuales = tema_actual.val.getPreguntas() # Cambiamos a las preguntas del siguiente tema
        temas -= 1

    if dato == "extremismo":
        final = time.time()
        extremismo = round(Extremismo_Pregunta(mayor.val.getEncuestados())/Arb_Size(mayor.val.getEncuestados()), 2)
        resultado = "Pregunta con mayor extremismo: [" + str(extremismo) + "] Pregunta: " + mayor.val.getNombre() + "\n"
        print("extremismo: " +  f"{1000*(final - inicio):.10f}")
        return resultado
    if dato == "mediana":
        final = time.time()
        mediana = Arb_Median(mayor.val.getEncuestados(), lambda e: e.getOpinion()).getOpinion()
        resultado = "Pregunta con mayor mediana de opinión: [" + str(mediana) + "] Pregunta: " + mayor.val.getNombre() + "\n"
        print("mediana: " + f"{1000*(final - inicio):.10f}")
        return resultado
    
#---------------------------------------------- PUNTO 8 ----------------------------------------------

def punto8_Abb(encuesta):
    """
    Pregunta con menor mediana de opiniones
    En caso de empate, se usa la pregunta con menor identificador
    Retorna un string con el resultado
    """
    
    # Crear ABB y cargar preguntas directamente
    root_mediana = None
    pregunta_id = 1
    
    # Cargar preguntas directamente en el ABB
    for tema_idx, tema in enumerate(encuesta._iterate_temas(), 1):
        for pregunta_idx, pregunta in enumerate(tema._iterate_preguntas(), 1):
            # Obtener opiniones de la pregunta
            opiniones = pregunta.get_opiniones()
            mediana_pregunta = mediana(opiniones)
            
            # Crear objeto pregunta con mediana
            pregunta_con_mediana = {
                'pregunta': pregunta,
                'mediana': mediana_pregunta,
                'tema_idx': tema_idx,
                'pregunta_idx': pregunta_idx,
                'id': pregunta_id,
                'nombre_completo': f"Pregunta {tema_idx}.{pregunta_idx}"
            }
            
            # Cargar directamente en el ABB sin estructura auxiliar
            if root_mediana is None:
                root_mediana = abb_mediana(pregunta_con_mediana)
            else:
                root_mediana.insert_mediana(pregunta_con_mediana)
            pregunta_id += 1
    
    # Encontrar la pregunta con menor mediana
    menor_mediana = root_mediana.find_min_mediana()
    return f"Pregunta con menor mediana de opinion: [{int(menor_mediana['mediana'])}] Pregunta: {menor_mediana['nombre_completo']}"

#---------------------------------------------- PUNTO 9 ----------------------------------------------

def abb_moda(opiniones):
    map_moda = []  
    while opiniones:
        key=opiniones[0]
        i=1
        a=1
        length = cant(copy.copy(opiniones))
        while i< length:
            if key==opiniones[i]:
                a=a+1
                opiniones.pop(i)
                length=length-1
                i=i-1
            i=i+1
        map_moda.append([key, a])
        opiniones.pop(0)

    while map_moda:
        key=map_moda[0]
        i=1
        length = cant(copy.copy(map_moda))
        while i < length and key[1] >= map_moda[i][1]:
            if key[1] == map_moda[i][1]:
                if key[0] <= map_moda[i][0]:
                    i=i+1
                else:
                    key=map_moda[i]
            else:
                i=i+1
        if i<length:
            map_moda.pop(0)
        else:
            return key
    return key
        
def abb_modas(preguntas):
    encuestados = []
    abb_to_array(encuestados, preguntas[0].getEncuestados())
    preguntas[0].setEncuestados(encuestados)
    root = abb(preguntas[0])
    i=1
    while i<cant(copy.copy(preguntas)):
        encuestados = []
        abb_to_array(encuestados, preguntas[i].getEncuestados())
        preguntas[i].setEncuestados(encuestados)
        abb_insert_moda(root, abb(preguntas[i]))
        i=i+1
    return root

def abb_insert_moda(root, pregunta):
    moda_root = abb_moda(root.val.getOpiniones())[0]
    moda2= abb_moda(pregunta.val.getOpiniones())[0]
    
    if moda_root < moda2:
        if root.right == None:
            root.right = pregunta
        else:
            abb_insert_moda(root.right, pregunta)

    elif moda_root == moda2:
        if root.val.nombre <= pregunta.val.nombre:
                if root.left == None:
                    root.left = pregunta
                else:
                    abb_insert_moda(root.left, pregunta)

        else:
            if root.right == None:
                root.right = pregunta
            else:
                abb_insert_moda(root.right, pregunta)
    else:
        if root.left == None:
            root.left = pregunta
        else:
            abb_insert_moda(root.left, pregunta)

def abb_mayor_moda(encuesta):
    temas=[]
    abb_to_array(temas, encuesta.Temas)
    preguntas=[]
    i=0
    while i<cant(copy.copy(temas)):
        aux=[]
        abb_to_array(aux, temas[i].getPreguntas())
        preguntas = preguntas + aux
        i=i+1
    root=abb_modas(preguntas)

    while root.right:
        root=root.right
    return "Pregunta con mayor moda de opinion: " + "[" + f"{abb_moda(root.val.getOpiniones())[0]}" + "] Pregunta: " + root.val.nombre + "\n"

#---------------------------------------------- PUNTO 10 ----------------------------------------------

def contar_encuestados_encuesta_ABB(raiz_temas):
    """
    Retorna el número total de encuestados en toda la encuesta (estructura ABB).
    """
    total = 0

    def recorrer_temas(nodo_tema):
        nonlocal total
        if nodo_tema is None or nodo_tema.val is None:
            return
        recorrer_temas(nodo_tema.left)

        tema = nodo_tema.val
        recorrer_preguntas(tema.preguntas)

        recorrer_temas(nodo_tema.right)

    def recorrer_preguntas(nodo_pregunta):
        nonlocal total
        if nodo_pregunta is None or nodo_pregunta.val is None:
            return
        recorrer_preguntas(nodo_pregunta.left)

        pregunta = nodo_pregunta.val
        recorrer_encuestados(pregunta.encuestados)

        recorrer_preguntas(nodo_pregunta.right)

    def recorrer_encuestados(nodo_enc):
        nonlocal total
        if nodo_enc is None or nodo_enc.val is None:
            return
        recorrer_encuestados(nodo_enc.left)
        total += 1
        recorrer_encuestados(nodo_enc.right)

    recorrer_temas(raiz_temas)
    return total

def buscar_en_temas_10(nodo_tema, menor):
    if nodo_tema is None or nodo_tema.val is None:
        return menor

    menor = buscar_en_temas_10(nodo_tema.left, menor)
    tema = nodo_tema.val
    menor = buscar_pregunta_menor_moda(tema.preguntas, menor)
    menor = buscar_en_temas_10(nodo_tema.right, menor)
    return menor

def moda_opinion(pregunta):
    frecuencias = [0] * 11  # Opiniones entre 0 y 10
    def recorrer(nodo):
        if nodo is None or nodo.val is None:
            return
        recorrer(nodo.left)
        frecuencias[nodo.val.opinion] += 1
        recorrer(nodo.right)

    recorrer(pregunta.encuestados)
    max_frec = max(frecuencias)
    for i in range(11):
        if frecuencias[i] == max_frec:
            return i  # Retorna la menor moda (en caso de empate)
        
def punto10_Abb(encuesta):
    """
    Encuentra y muestra la pregunta con el menor valor de moda de opiniones
    en toda la encuesta, recorriendo todos los temas y preguntas.
    """
    tiempo_inicio = time.time()

    pregunta_menor_moda = buscar_en_temas(encuesta.Temas, None)

    if pregunta_menor_moda:
        moda = moda_opinion(pregunta_menor_moda)
        resultado = f"Pregunta con menor moda de opinion: [{moda}] Pregunta: {pregunta_menor_moda.getNombre()}\n"
    else:
        print("No se encontró ninguna pregunta.")

    tiempo_final = time.time()
    
    return resultado
        
#---------------------------------------------- PUNTO 11 ----------------------------------------------

# A esta función se le pasa el arbol de encuestados
def Extremismo_Pregunta(arbol):
    if arbol is None:
        return 0
    if arbol.val.getOpinion() == 0 or arbol.val.getOpinion() == 10: # Si el encuestado tiene una opinion de 0 o 10
        return 1 + Extremismo_Pregunta(arbol.left) + Extremismo_Pregunta(arbol.right) # Retornamos 1 + el extremismo de las ramas iquierda y derecha
    else: # De lo contrario
        return Extremismo_Pregunta(arbol.left) + Extremismo_Pregunta(arbol.right) # Retornamos el extremismo de las ramas iquierda y derecha
    
#---------------------------------------------- PUNTO 12 ----------------------------------------------

def abb_consensos(preguntas):
    encuestados = []
    abb_to_array(encuestados, preguntas[0].getEncuestados())
    preguntas[0].setEncuestados(encuestados)
    root = abb(preguntas[0])
    i=1
    while i<cant(copy.copy(preguntas)):
        encuestados = []
        abb_to_array(encuestados, preguntas[i].getEncuestados())
        preguntas[i].setEncuestados(encuestados)
        abb_insert_consenso(root, abb(preguntas[i]))
        i=i+1
    return root

def abb_insert_consenso(root, pregunta):
    cons_root = abb_moda(root.val.getOpiniones())[1]/cant(copy.deepcopy(root.val.getEncuestados()))
    cons2 = abb_moda(pregunta.val.getOpiniones())[1]/cant(copy.deepcopy(pregunta.val.getEncuestados()))
    
    if cons_root > cons2:
        if root.left == None:
            root.left = pregunta
        else:
            abb_insert_consenso(root.left, pregunta)

    elif cons_root == cons2:
        if root.val.getNombre() <= pregunta.val.getNombre():
                if root.left == None:
                    root.left = pregunta
                else:
                    abb_insert_consenso(root.left, pregunta)

        else:
            if root.right == None:
                root.right = pregunta
            else:
                abb_insert_consenso(root.right, pregunta)

    else:
        if root.right == None:
            root.right = pregunta
        else:
            abb_insert_consenso(root.right, pregunta)

def abb_mayor_consenso(encuesta):
    temas=[]
    abb_to_array(temas, encuesta.getTemas())
    preguntas=[]
    i=0
    while i<cant(copy.copy(temas)):
        aux=[]
        abb_to_array(aux, temas[i].getPreguntas())
        preguntas = preguntas + aux
        i=i+1

    root=abb_consensos(preguntas)
    
    while root.right:
        root=root.right
    consenso = abb_moda(root.val.getOpiniones())[1]/cant(copy.deepcopy(root.val.getEncuestados()))
    return "Pregunta con mayor consenso: " + "[" + f"{round(consenso, 2)}" + "] Pregunta: " + f"{root.val.getNombre()}"