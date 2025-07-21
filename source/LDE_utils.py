from controlador_LDE import *

#Punto 1: Ordenar encuestados de la pregunta ascendentemente segun su opinion
def punto1_LDE():
     #Insertion sort alreves
     lista=[1, 2, 5, 4, 5]
     for j in range(1, len(lista)):
          key=lista[len(lista)-j-1]
          i=len(lista)-j
          while i<len(lista) and key<lista[i]:
               lista[i-1]=lista[i]
               i=i+1
          lista[i-1]=key

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

def punto3_LDE():
     pass

#Punto 4

def punto4_LDE():
     pass

#Punto 5

def punto5_LDE():
     pass

#Punto 6

def punto6_LDE():
     print("#################################")

#Punto 7

def punto7_LDE():
     pass

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

def punto11_LDE():
     pass

#Punto 12

def punto12_LDE():
     pass
