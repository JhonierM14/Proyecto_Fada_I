from controlador_abb import *

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
abb_print=abb_escribir_opiniones(encuesta_abb)

#Punto 2

def punto2_Abb():
    print("#################################")

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

abb_punto5 = abb_mayor_promedio(copy.deepcopy(encuesta_abb))

#Punto 6

def punto6_Abb():
    print("#################################")

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

abb_punto9 = abb_mayor_moda(copy.deepcopy(encuesta_abb))

#Punto 10

def punto10_Abb():
    print("#################################")

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

abb_punto12 = abb_mayor_consenso(encuesta_abb)
