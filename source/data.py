from data_structures.listadoble import *
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
    partes = texto.split(',')
    nombre = partes[0]
    experiencia = partes[1].split(': ')[1]
    opinion = partes[2].split(': ')[1]
    return Encuestado(id, nombre, int(experiencia), int(opinion))

def Pregunta_a_Objeto(texto, nombre, encuestados_total):
    partes = texto.strip('{}')
    partes = partes.split(', ')
    encuestados_pregunta = None
    for e in partes:
        encuestados_pregunta = List_Insert_End(encuestados_pregunta, encuestados_total[int(e)])
    return Pregunta(nombre, encuestados_pregunta)

# Pregunta_a_Objeto("{10, 3, 2}", id)

# print(Encuestado_a_Objeto("Sofía García, Experticia: 1, Opinión: 6", 1).getID())
# print(Encuestado_a_Objeto("Sofía García, Experticia: 1, Opinión: 6", 1).getNombre())
# print(Encuestado_a_Objeto("Sofía García, Experticia: 1, Opinión: 6", 1).getExperticia())
# print(Encuestado_a_Objeto("Sofía García, Experticia: 1, Opinión: 6", 1).getOpinion())

def Texto_a_Encuesta(archivo):
    with open("Proyecto_FADA_I/Pruebas/" + archivo, "r", encoding='utf-8') as documento:
        texto = documento.read()
        parrafos = texto.split("\n\n")
        encuestados = texto.split("\n\n")[0].split("\n")
        sada = []
        contador_encuestados = 1
        lista_encuestados = None
        lista_temas = None

        for i in range(0, len(parrafos)):
            if i == 0:
                for e in encuestados:
                    sada.append(e)
                    lista_encuestados = List_Insert_End(lista_encuestados, e)
                    contador_encuestados += 1
                    #lista_encuestados = List_Insert_End(lista_encuestados, Encuestado_a_Objeto(e, contador_encuestados))
            else:
                lista_preguntas = None
                for j in range(1, len(parrafos[i].split("\n"))):
                    #print(parrafos[i].split("\n")[j])
                    print("Pregunta: " + str(i+j*0.1))
                #print(parrafos[i].split("\n"))
                tema = Tema("Tema " + str(i), [])
                lista_temas = List_Insert_End(lista_temas, tema)

    #return Encuesta(len(parrafos)-1, len(parrafos[i].split("\n"))-1, 1, 1, lista_temas)

Texto_a_Encuesta("Test2.txt")
    #print(sada)
    #encuesta = Encuesta(1, 1, 1, 1, [])

    # print(texto.split("\n\n")[1].split("\n"))
    # print(texto.split("\n\n")[2].split("\n"))
    
    #List_Print(lista_encuestados)

    # encuestados = None
    # temas = None
    # preguntas = None
    # for x in texto:
    #     linea = texto.readline()
    #     print(linea)
    #     if linea.startswith('{'):
    #         preguntas = List_Insert(preguntas, linea.strip())
    #     else:
    #         encuestados = List_Insert_End(encuestados, linea.strip())
    # List_Print(encuestados)
