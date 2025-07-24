from data_structures.listadoble import *
from data_structures.abb import abb, Arb_Insert

from form.encuestado import Encuestado
from form.pregunta import Pregunta
from form.tema import Tema
from form.encuesta import Encuesta


# id, nombre, experticia, opinion.
Persona   = Encuestado(1,  "Sofia García",         1, 6)
Persona2  = Encuestado(2,  "Alejandro Torres",     7, 10)
Persona3  = Encuestado(3,  "Valentina Rodriguez",  9, 0)
Persona4  = Encuestado(4,  "Juan Lopéz",          10, 1)
Persona5  = Encuestado(5,  "Martina Martinez",     7, 0)
Persona6  = Encuestado(6,  "Sebastián Pérez",      8, 9)
Persona7  = Encuestado(7,  "Camila Fernández",     2, 7)
Persona8  = Encuestado(8,  "Mateo González",       4, 7)
Persona9  = Encuestado(9,  "Isabella Díaz",        7, 5)
Persona10 = Encuestado(10, "Daniel Ruiz",          2, 9)
Persona11 = Encuestado(11, "Luciana Sánchez",      1, 7)
Persona12 = Encuestado(12, "Lucas Vásquez",        6, 8)

# nombre, encuestados
pregunta1_1 = Pregunta("Pregunta 1.1", [Persona10, Persona2])
pregunta1_2 = Pregunta("Pregunta 1.2", [Persona, Persona9, Persona12, Persona6])
pregunta2_1 = Pregunta("Pregunta 2.1", [Persona11, Persona8, Persona7])
pregunta2_2 = Pregunta("Pregunta 2.2", [Persona3, Persona4, Persona5])

# nombre, preguntas
tema1 = Tema("Tema 1", [pregunta1_1, pregunta1_2])
tema2 = Tema("Tema 2", [pregunta2_1, pregunta2_2])

# numero de temas, numero de preguntas, cantidad minima de encuestados, cantidad maxima de encuestados, temas
prueba = Encuesta(2, 2, 2, 4, [tema1, tema2])

def Encuestado_a_Objeto(texto, id):
    partes = texto.split(',') # Separa el texto del nombre, experticia y opinion en una lista
    nombre = partes[0] # Obtiene el primer elemento de la lista (el nombre)
    experiencia = partes[1].split(': ')[1] # Separa el segundo elemento en otra lista (separa en [experticia, x]) y obtenemos el valor
    opinion = partes[2].split(': ')[1] # Separa el tercer elemento en otra lista (separa en [opinion, x]) y obtenemos el valor
    
    return Encuestado(id, nombre, int(experiencia), int(opinion)) 

def Pregunta_a_Objeto(texto, nombre, lista_todos_encuestados):
    partes = texto.strip('{}')
    partes = partes.split(', ')
    lista_encuestados_pregunta = None
    arbol_encuestados_pregunta = abb(None)

    for e in partes:
        encuestado = lista_todos_encuestados[int(e)-1]
        encuestado_obj = Encuestado_a_Objeto(encuestado, int(e))
        lista_encuestados_pregunta = List_Insert_End(lista_encuestados_pregunta, encuestado_obj)
        arbol_encuestados_pregunta = Arb_Insert(arbol_encuestados_pregunta, encuestado_obj, lambda e: e.getID())

    return Pregunta(nombre, lista_encuestados_pregunta), Pregunta(nombre, arbol_encuestados_pregunta)

def Texto_a_Encuesta(archivo):
    with open("source/tests/" + archivo, "r", encoding='utf-8') as documento:
        texto = documento.read() # Leer todo el contenido del archivo
        parrafos = texto.split("\n\n") # Dividir en párrafos
        encuestados = texto.split("\n\n")[0].split("\n") # El primer parrafo (los encuestados y sus datos)

        lista_encuestados = []
        lista_temas = None
        arbol_temas = abb(None)

        K = len(parrafos)-1 # Cantidad de temas
        M = len(parrafos[1].split("\n"))-1 # Cantidad de preguntas por tema

        for i in range(0, K+1):
            if i == 0:
                for e in encuestados:
                    lista_encuestados.append(e)
                Nmin = len(lista_encuestados) # Número como caso base
                Nmax = 1 #Número como caso base
            else:
                lista_preguntas = None
                arbol_preguntas = abb(None)

                for j in range(1, M+1):
                    texto_pregunta = parrafos[i].split("\n")[j]
                    nombre_pregunta = str(i+j*0.1)
                    pregunta_lista, pregunta_arbol = Pregunta_a_Objeto(texto_pregunta, nombre_pregunta, lista_encuestados)

                    lista_preguntas = List_Insert_End(lista_preguntas, pregunta_lista)
                    arbol_preguntas = Arb_Insert(arbol_preguntas, pregunta_arbol, lambda e: e.getNombre())

                    if Nmin > List_Size(pregunta_lista.getEncuestados()):
                        Nmin = List_Size(pregunta_lista.getEncuestados())
                    if Nmax < List_Size(pregunta_lista.getEncuestados()):
                        Nmax = List_Size(pregunta_lista.getEncuestados())

                tema_lista = Tema(i, lista_preguntas)
                tema_arbol = Tema(i, arbol_preguntas)

                lista_temas = List_Insert_End(lista_temas, tema_lista)
                arbol_temas = Arb_Insert(arbol_temas, tema_arbol, lambda e: e.getNombre())

    return Encuesta(K, M, Nmin, Nmax, lista_temas), Encuesta(K, M, Nmin, Nmax, arbol_temas)

def Resultados_a_Texto(nombre, encuesta, tipo):
    # Creamos un nuevo archivo en la carpeta de Resultados
    f = open("source/results/" + nombre, "x", encoding='utf-8')

    # Lo abrimos y escribimos en él
    with open("source/results/" + nombre, "a", encoding='utf-8'):

        if tipo == "listas entrelazadas":
            f.write("Resultados de la encuesta:\n")
            f.write(Ordenar_Tema_Listas(encuesta.getTemas(), encuesta.getM()))
            f.write("\nResultados:\n")
            f.write(Mayor_Listas(encuesta.getTemas(), encuesta.getK(), encuesta.getM(), "extremismo"))
            f.write(Mayor_Listas(encuesta.getTemas(), encuesta.getK(), encuesta.getM(), "mediana"))

        else:
            f.write("Resultados de la encuesta:\n")
            f.write(Ordenar_Tema_Arboles(encuesta.getTemas()))
            f.write("\nResultados:\n")
            f.write(Mayor_Arboles(encuesta.getTemas(), encuesta.getK(), encuesta.getM(), "extremismo"))
            f.write(Mayor_Arboles(encuesta.getTemas(), encuesta.getK(), encuesta.getM(), "mediana"))

    return f

encuesta = Texto_a_Encuesta("Test3.txt")
