from controlador_abb import *

#Punto 1

#Punto 1 con ABB:
lista: list = #Ingrese la lista de encuestados

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

def punto5_Abb():
    pass

#Punto 6

def punto6_Abb():
    print("#################################")

#Punto 8

def punto8_Abb():
    pass

#Punto 9

def punto9_Abb():
    pass

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

def punto12_Abb():
    pass
