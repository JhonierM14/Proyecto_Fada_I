from source.controlador_LDE import *

#Punto 1: Ordenar encuestados de la pregunta ascendentemente segun su opinion.

#Insertion sort alreves
lista=[1,2,5,4,5]
for j in range(1, len(lista)):
     key=lista[len(lista)-j-1]
     i=len(lista)-j
     while i<len(lista) and key<lista[i]:
          lista[i-1]=lista[i]
          i=i+1
     lista[i-1]=key

#Se asigna a "lista" el arreglo que se quiere ordenar:
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
print("#################################")