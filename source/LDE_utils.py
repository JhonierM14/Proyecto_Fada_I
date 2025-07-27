from controlador_LDE import *
from data_structures.listadoble import *
from data_structures.abb import *
from form.AlgoritmosOrdenamiento.MedidasTenciaCentral import *

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

def punto3_LDE():
     pass

#Punto 4

def punto4_LDE(encuesta):
    """
    Ordenar a todos los encuestados según su experticia (descendente)
    En caso de empate, ordenar por ID (ascendente)
    Retorna un string con la lista ordenada de encuestados
    """    
    # Cargar directamente en la Lista Doblemente Enlazada
    head_lde = None
    
    # Recopilar y cargar encuestados directamente en la LDE
    for tema in encuesta._iterate_temas():
        for pregunta in tema._iterate_preguntas():
            for encuestado in pregunta._iterate_encuestados():
                # Cargar directamente en la LDE sin verificar duplicados
                head_lde = List_Insert_End(head_lde, encuestado)
    
    # Usar el método de ordenamiento de la estructura LDE
    lde_sorter = LDE(None)  # Instancia para usar los métodos
    head_lde = lde_sorter.List_Merge_Sort_Experticia(head_lde)
    
    # Construir el string de salida
    resultado = "Lista de encuestados:\n"
    current = head_lde
    while current:
        enc = current.getData()
        resultado += f" ({enc.getID()}, Nombre:'{enc.getNombre()}', Experticia:{enc.getExperticia()}, Opinión:{enc.getOpinion()})\n"
        current = current.getNext()
    
    resultado += "\n"
    return resultado

#Punto 5

def punto5_LDE():
     pass

#Punto 6

def punto6_LDE():
     pass

#Punto 7

def punto7_LDE():
     pass

#Punto 8

def punto8_LDE(encuesta):
    """
    Pregunta con menor mediana de opiniones
    En caso de empate, se usa la pregunta con menor identificador
    Retorna un string con el resultado
    """

    # Crear una lista doblemente enlazada para almacenar las preguntas con su mediana
    head_preguntas = None
    pregunta_id = 1
    
    # Cargar preguntas directamente en la LDE
    for tema_idx, tema in enumerate(encuesta._iterate_temas(), 1):
        for pregunta_idx, pregunta in enumerate(tema._iterate_preguntas(), 1):
            # Obtener opiniones de la pregunta
            opiniones = pregunta.get_opiniones()
            mediana_pregunta = mediana(opiniones)
            
            # Crear objeto pregunta con mediana para la lista
            pregunta_con_mediana = {
                'pregunta': pregunta,
                'mediana': mediana_pregunta,
                'tema_idx': tema_idx,
                'pregunta_idx': pregunta_idx,
                'id': pregunta_id,
                'nombre_completo': f"Pregunta {tema_idx}.{pregunta_idx}"
            }
            
            # Insertar directamente en lista doblemente enlazada
            head_preguntas = List_Insert_End(head_preguntas, pregunta_con_mediana)
            pregunta_id += 1
    
    # Usar el método de ordenamiento de la estructura LDE
    lde_sorter = LDE(None)  # Instancia para usar los métodos
    head_preguntas = lde_sorter.List_Insertion_Sort_Mediana(head_preguntas)
    
    # La primera pregunta en la lista ordenada tiene la menor mediana
    menor_mediana = head_preguntas.getData()
    return f"Pregunta con menor mediana de opinion: [{int(menor_mediana['mediana'])}] Pregunta: {menor_mediana['nombre_completo']}"

#Punto 9

def punto9_LDE():
     pass

#Punto 10

def punto10_LDE():
     pass

#Punto 11

def punto11_LDE():
     pass

#Punto 12

def punto12_LDE(encuesta):
    """
    Pregunta con mayor consenso, donde consenso se define como el porcentaje 
    de los encuestados en la pregunta que tiene la opinión moda o la más frecuente
    En caso de empate, se usa la pregunta con menor identificador
    Retorna un string con el resultado
    """    
    # Crear una lista doblemente enlazada para almacenar las preguntas con su consenso
    head_preguntas = None
    pregunta_id = 1
    
    # Cargar preguntas directamente en la LDE
    for tema_idx, tema in enumerate(encuesta._iterate_temas(), 1):
        for pregunta_idx, pregunta in enumerate(tema._iterate_preguntas(), 1):
            # Obtener opiniones de la pregunta
            opiniones = pregunta.get_opiniones()
            moda_pregunta = moda(opiniones)
            consenso_pregunta = consenso(opiniones)
            
            # Crear objeto pregunta con consenso para la lista
            pregunta_con_consenso = {
                'pregunta': pregunta,
                'consenso': consenso_pregunta,
                'moda': moda_pregunta,
                'tema_idx': tema_idx,
                'pregunta_idx': pregunta_idx,
                'id': pregunta_id,
                'nombre_completo': f"Pregunta {tema_idx}.{pregunta_idx}"
            }
            
            # Insertar directamente en lista doblemente enlazada
            head_preguntas = List_Insert_End(head_preguntas, pregunta_con_consenso)
            pregunta_id += 1
    
    # Usar el método de ordenamiento de la estructura LDE
    lde_sorter = LDE(None)  # Instancia para usar los métodos
    head_preguntas = lde_sorter.List_Insertion_Sort_Consenso(head_preguntas)
    
    # La primera pregunta en la lista ordenada tiene el mayor consenso
    mayor_consenso = head_preguntas.getData()
    return f"Pregunta con mayor consenso: [{mayor_consenso['consenso']:.2f}] Pregunta: {mayor_consenso['nombre_completo']}"


