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

def punto3_Abb():
    pass
#Punto 4

def punto4_Abb():
    pass
#Punto 5

def punto5_Abb():
    pass

#Punto 6

def punto6_Abb():
    print("#################################")

#Punto 7

def punto7_Abb():
    pass

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

def punto11_Abb():
    pass

#Punto 12

def punto12_Abb():
    pass
