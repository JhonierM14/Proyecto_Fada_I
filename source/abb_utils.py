from controlador_abb import *

#Punto 1

#Punto 3

def punto3_Abb():
     pass

#Punto 4

def punto4_Abb(encuesta):
    """
    Ordenar a todos los encuestados según su experticia (descendente)
    En caso de empate, ordenar por ID (descendente - mayor ID)
    Retorna un string con la lista ordenada de encuestados
    """
    from data_structures.abb import abb_experticia
    
    # Crear ABB y cargar encuestados directamente
    root_experticia = None
    
    # Recopilar y cargar encuestados directamente en el ABB
    for tema in encuesta._iterate_temas():
        for pregunta in tema._iterate_preguntas():
            for encuestado in pregunta._iterate_encuestados():
                # Cargar directamente en el ABB sin verificar duplicados
                if root_experticia is None:
                    root_experticia = abb_experticia(encuestado)
                else:
                    root_experticia.insert_experticia(encuestado)
    
    # Construir el string de salida
    resultado = "Lista de encuestados:\n"
    if root_experticia:
        # Crear una función auxiliar para construir el string
        def inorder_to_string(node, result):
            if node.left:
                inorder_to_string(node.left, result)
            
            enc = node.encuestado
            result.append(f" ({enc.getID()}, Nombre:'{enc.getNombre()}', Experticia:{enc.getExperticia()}, Opinión:{enc.getOpinion()})")
            
            if node.right:
                inorder_to_string(node.right, result)
        
        encuestados_list = []
        inorder_to_string(root_experticia, encuestados_list)
        resultado += "\n".join(encuestados_list)
    
    resultado += "\n\n"
    return resultado

#Punto 5

def punto5_Abb():
     pass

#Punto 6

def punto6_Abb():
     pass

#Punto 7

def punto7_Abb():
     pass

#Punto 8

def punto8_Abb(encuesta):
    """
    Pregunta con menor mediana de opiniones
    En caso de empate, se usa la pregunta con menor identificador
    Retorna un string con el resultado
    """
    from data_structures.abb import abb_mediana
    from form.AlgoritmosOrdenamiento.MedidasTenciaCentral import mediana
    
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

#Punto 9

def punto9_Abb():
     pass

#Punto 10

def punto10_Abb():
     pass

#Punto 11

def punto11_Abb():
     pass

#Punto 12

def punto12_Abb(encuesta):
    """
    Pregunta con mayor consenso, donde consenso se define como el porcentaje 
    de los encuestados en la pregunta que tiene la opinión moda o la más frecuente
    En caso de empate, se usa la pregunta con menor identificador
    Retorna un string con el resultado
    """
    from data_structures.abb import abb_consenso
    from form.AlgoritmosOrdenamiento.MedidasTenciaCentral import moda, consenso
    
    # Crear ABB y cargar preguntas directamente
    root_consenso = None
    pregunta_id = 1
    
    # Cargar preguntas directamente en el ABB
    for tema_idx, tema in enumerate(encuesta._iterate_temas(), 1):
        for pregunta_idx, pregunta in enumerate(tema._iterate_preguntas(), 1):
            # Obtener opiniones de la pregunta
            opiniones = pregunta.get_opiniones()
            moda_pregunta = moda(opiniones)
            consenso_pregunta = consenso(opiniones)
            
            # Crear objeto pregunta con consenso
            pregunta_con_consenso = {
                'pregunta': pregunta,
                'consenso': consenso_pregunta,
                'moda': moda_pregunta,
                'tema_idx': tema_idx,
                'pregunta_idx': pregunta_idx,
                'id': pregunta_id,
                'nombre_completo': f"Pregunta {tema_idx}.{pregunta_idx}"
            }
            
            # Cargar directamente en el ABB sin estructura auxiliar
            if root_consenso is None:
                root_consenso = abb_consenso(pregunta_con_consenso)
            else:
                root_consenso.insert_consenso(pregunta_con_consenso)
            pregunta_id += 1
    
    # Encontrar la pregunta con mayor consenso
    mayor_consenso = root_consenso.find_max_consenso()
    return f"Pregunta con mayor consenso: [{mayor_consenso['consenso']:.2f}] Pregunta: {mayor_consenso['nombre_completo']}"