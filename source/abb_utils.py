import time

from data_structures.abb import Arb_Insert, Arb_Median, Arb_Size, abb, buscar_pregunta_menor_moda, buscar_pregunta_menor_promedio, insertar_pregunta_arbol, promedio_opinion

#Punto 1
#Funcion propia que reemplaza el len de python
def cant(lst):
    a=0
    while lst:
        a=a+1
        lst.pop(0)
    return a 

def abb_encuestados(arb):
    i=1
    arr=[]
    abb_to_array(arr, arb)
    #root sera la raiz del nuevo arbol ordenado por la opinion
    root=abb(arr[0])
    while i<cant(copy.copy(arr)):
        abb_insert_encuestados(root, arr[i])
        i=i+1
    return root

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

#Sirve para crear un arreglo con la id de todos los elementos del arbol en orden descendiente
def inorder_encuestados(root, arr):
    if root is None:
        return root
    inorder_encuestados(root.right, arr)
    arr.append(root.val.getID())
    inorder_encuestados(root.left, arr)
    return arr

#Sirve para crear un string "str" que tiene la informacion necesaria para la primer parte de la salida
def abb_escribir_opiniones(encuesta):
    str=""
    temas = encuesta.getTemas()
    while temas:
        str = str + "Tema "+f"{temas.val.getNombre()}: " + "\n"
        preguntas = temas.val.getPreguntas()
        while preguntas:
            arr = []
            encuestados = preguntas.val.getEncuestados()
            root = abb_encuestados(encuestados)
            str = str + "Pregunta " + f"{preguntas.val.getNombre()}: " + f"{inorder_encuestados(root, arr)}" + "\n"
            preguntas=preguntas.right
        temas = temas.right
    return str

#Salida del abb
# abb_print=abb_escribir_opiniones(encuesta_abb)

#Punto 2

def recorrer_temas(nodo_tema):
    if nodo_tema is None or nodo_tema.val is None:
        return
    recorrer_temas(nodo_tema.left)

    tema = nodo_tema.val
    print(f"[{round(promedio_tema(tema), 2)}] Tema {tema.nombre}:")
    recorrer_preguntas_ordenadas_por_promedio(tema.preguntas)

    recorrer_temas(nodo_tema.right)

def recorrer_preguntas_ordenadas_por_promedio(raiz_preguntas):
    # Creamos un nuevo árbol ordenado por promedio de opinión
    nuevo_arbol = abb()

    def insertar_todas(nodo):
        if nodo is None or nodo.val is None:
            return
        insertar_todas(nodo.left)
        insertar_pregunta_arbol(nuevo_arbol, nodo.val)
        insertar_todas(nodo.right)

    insertar_todas(raiz_preguntas)

    def imprimir_en_orden(nodo):
        if nodo is None or nodo.val is None:
            return
        imprimir_en_orden(nodo.left)
        preg = nodo.val
        ids = obtener_ids_pregunta(preg)
        prom = round(preg.promedio_opinion(), 2)
        print(f"[{prom}] Pregunta {preg.nombre}: ({', '.join(map(str, ids))})")
        imprimir_en_orden(nodo.right)

    imprimir_en_orden(nuevo_arbol)

def promedio_tema(tema):
        suma = 0
        count = 0

        def acumular_promedios(nodo: abb): # preguntas
            nonlocal suma, count
            if nodo is None or nodo.val is None:
                return
            acumular_promedios(nodo.left)
            pregunta = nodo.val
            suma += promedio_opinion(pregunta)
            count += 1
            acumular_promedios(nodo.right)

        acumular_promedios(tema.preguntas)
        return suma / count if count > 0 else 0

def obtener_ids_pregunta(pregunta):
    ids = []

    def recorrer_encuestados(nodo):
        if nodo is None or nodo.val is None:
            return
        recorrer_encuestados(nodo.left)
        ids.append(nodo.val.id)
        recorrer_encuestados(nodo.right)

    recorrer_encuestados(pregunta.encuestados)
    return ids

def mostrar_ids_encuesta_completa(raiz_temas):
    """
    Muestra en una única línea los IDs de todos los encuestados de toda la encuesta (ABB).
    """
    def recorrer_temas(nodo_tema):
        if nodo_tema is None or nodo_tema.val is None:
            return
        recorrer_temas(nodo_tema.left)

        tema = nodo_tema.val
        recorrer_preguntas(tema.preguntas)

        recorrer_temas(nodo_tema.right)

    def recorrer_preguntas(nodo_pregunta):
        if nodo_pregunta is None or nodo_pregunta.val is None:
            return
        recorrer_preguntas(nodo_pregunta.left)

        pregunta = nodo_pregunta.val
        imprimir_ids_encuestados_abb(pregunta.encuestados)

        recorrer_preguntas(nodo_pregunta.right)

    recorrer_temas(raiz_temas)
    print()  # salto de línea final

def imprimir_ids_encuestados_abb(nodo):
    """
    Imprime los IDs de un ABB de encuestados en una misma línea, sin usar estructuras auxiliares.
    """
    if nodo is None or nodo.val is None:
        return
    imprimir_ids_encuestados_abb(nodo.left)
    print(nodo.val.id, end=" ")
    imprimir_ids_encuestados_abb(nodo.right)

def punto2_Abb(encuesta):
    """
    Por cada tema, se busca que las preguntas estén ordenadas 
    descendentemente según su promedio del valor de opinión.
    La salida se imprime por tema y por pregunta, mostrando sus promedios.
    """
    tiempo_inicio = time.time()

    # Ejecutar recorrido
    recorrer_temas(encuesta.Temas)

    mostrar_ids_encuesta_completa(encuesta.Temas)

    tiempo_final = time.time()
    print(f"\nTiempo usado: {tiempo_final - tiempo_inicio:.4f} segundos")

    return Arb_Size(encuesta.Temas), tiempo_final

#Punto 3

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
    actual = arbol  # Obtenemos el árbol de temas
    arbol_temas = abb(actual.val) # Guardamos el primer tema como base

    while actual.right: # Mientras hayan temas
        actual = actual.right # Avanzar al siguiente tema
        arbol_temas = Arb_Insert(arbol_temas, actual.val, lambda e: Promedio_Preguntas(e.getPreguntas()))

    resultado = Temas_Print(arbol_temas) # Guardamos el print del resultado de ordenar los temas
    print(resultado) 
    return resultado
    
#Punto 4

def punto4_Abb():
    pass


#Punto 5
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
    return "Pregunta de la encuesta con mayor promedio: ["+ f"{promedio(root.val.obtener_opiniones())}" + "] Pregunta: " + root.val.nombre 

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
    prom_root = promedio(root.val.obtener_opiniones())
    prom2 = promedio(pregunta.val.obtener_opiniones())
    exp_root = promedio(root.val.obtener_experticias())
    exp2 = promedio(pregunta.val.obtener_experticias())
    
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

# abb_punto5 = abb_mayor_promedio(copy.deepcopy(encuesta_abb))

#Punto 6

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
        print(f"La pregunta con menor promedio es la '{pregunta_menor_prom.getNombre()}' con promedio {round(pregunta_menor_prom.promedio_opinion(), 2)}")
    else:
        print("No se encontró ninguna pregunta.")

    tiempo_final = time.time()
    print(f"Tiempo usado: {tiempo_final - tiempo_inicio}")

#Punto 8

def punto8_Abb():
    pass

#Punto 9

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
    return "Pregunta con mayor moda de opinion: " + "[" + f"{abb_moda(root.val.obtener_opiniones())[0]}" + "] Pregunta: " + root.val.nombre
        
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
    moda_root = abb_moda(root.val.obtener_opiniones())[0]
    moda2= abb_moda(pregunta.val.obtener_opiniones())[0]
    
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

# abb_punto9 = abb_mayor_moda(copy.deepcopy(encuesta_abb))

#Punto 10

def buscar_en_temas_10(nodo_tema, menor):
    if nodo_tema is None or nodo_tema.val is None:
        return menor

    menor = buscar_en_temas_10(nodo_tema.left, menor)
    tema = nodo_tema.val
    menor = buscar_pregunta_menor_moda(tema.preguntas, menor)
    menor = buscar_en_temas_10(nodo_tema.right, menor)
    return menor

def punto10_Abb(encuesta):
    """
    Encuentra y muestra la pregunta con el menor valor de moda de opiniones
    en toda la encuesta, recorriendo todos los temas y preguntas.
    """
    tiempo_inicio = time.time()

    pregunta_menor_moda = buscar_en_temas(encuesta.Temas, None)

    if pregunta_menor_moda:
        moda = moda_opinion(pregunta_menor_moda)
        print(f"La pregunta con menor moda es '{pregunta_menor_moda.getNombre()}' con moda {moda}")
    else:
        print("No se encontró ninguna pregunta.")

    tiempo_final = time.time()
    print(f"Tiempo usado: {tiempo_final - tiempo_inicio:.4f} segundos")

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

#Punto 11

# A esta función se le pasa el arbol de encuestados
def Extremismo_Pregunta(arbol):
    if arbol is None:
        return 0
    if arbol.val.getOpinion() == 0 or arbol.val.getOpinion() == 10: # Si el encuestado tiene una opinion de 0 o 10
        return 1 + Extremismo_Pregunta(arbol.left) + Extremismo_Pregunta(arbol.right) # Retornamos 1 + el extremismo de las ramas iquierda y derecha
    else: # De lo contrario
        return Extremismo_Pregunta(arbol.left) + Extremismo_Pregunta(arbol.right) # Retornamos el extremismo de las ramas iquierda y derecha

# A esta función se le pasa el arbol de temas
def Mayor_X_Pregunta(arbol, K, M, dato):
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
        extremismo = round(Extremismo_Pregunta(mayor.val.getEncuestados())/Arb_Size(mayor.val.getEncuestados()), 2)
        resultado = "Pregunta con mayor extremismo: [" + str(extremismo) + "] Pregunta: " + mayor.val.getNombre() + "\n"
        print(resultado)
        return resultado
    if dato == "mediana":
        mediana = Arb_Median(mayor.val.getEncuestados(), lambda e: e.getOpinion()).getOpinion()
        resultado = "Pregunta con mayor mediana de opinión: [" + str(mediana) + "] Pregunta: " + mayor.val.getNombre() + "\n"
        print(resultado)
        return resultado

#Punto 12

def abb_mayor_consenso(encuesta):
    temas=[]
    abb_to_array(temas, encuesta.Temas)
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
    consenso = abb_moda(root.val.obtener_opiniones())[1]/cant(copy.deepcopy(root.val.encuestados))
    return "Pregunta con mayor consenso: " + "[" + f"{round(consenso, 2)}" + "] Pregunta: " + f"{root.val.nombre}"

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
    cons_root = abb_moda(root.val.obtener_opiniones())[1]/cant(copy.deepcopy(root.val.encuestados))
    cons2 = abb_moda(pregunta.val.obtener_opiniones())[1]/cant(copy.deepcopy(pregunta.val.encuestados))
    
    if cons_root >= cons2:
        if root.left == None:
            root.left = pregunta
        else:
            abb_insert_consenso(root.left, pregunta)
    else:
        if root.right == None:
            root.right = pregunta
        else:
            abb_insert_consenso(root.right, pregunta)

# abb_punto12 = abb_mayor_consenso(encuesta_abb)


def seleccionarFuncionAbb(metodo: int):
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
            return punto2_Abb
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            return punto6_Abb
        case 7:
            pass
        case 8:
            pass
        case 9:
            pass
        case 10:
            return punto10_Abb
        case 11:
            pass
        case 12:
            pass
        case _:
            raise ValueError("funcion no implementada.")        
