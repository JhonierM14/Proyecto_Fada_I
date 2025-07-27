from data_structures.listadoble import List_Insert_End
from math import ceil
from faker import Faker

from form.encuestado import Encuestado
from form.pregunta import Pregunta
from form.tema import Tema
from form.encuesta import Encuesta
from data_structures.abb import abb
import random

fake = Faker()

def generar_encuesta_simulada_LDE_determinista(
    k_temas: int,
    max_preguntas_por_tema: int,
    total_encuestados: int,
    nmin: int,
    nmax: int
):
    from math import ceil
    encuestado_id = 1
    pregunta_id = 1
    tema_id = 1
    encuestados_disponibles = []

    # se crean los encuestados
    for _ in range(total_encuestados):
        nombre = fake.name()
        experticia = random.randint(0, 10)
        opinion = random.randint(0, 10)
        encuestados_disponibles.append(Encuestado(encuestado_id, nombre, experticia, opinion))
        encuestado_id += 1

    random.shuffle(encuestados_disponibles)

    # se calcula el número total de preguntas
    total_preguntas = k_temas * max_preguntas_por_tema
    encuestados_por_pregunta = ceil(total_encuestados / total_preguntas)

    encuestados_por_pregunta = min(encuestados_por_pregunta, nmax)

    encuestado_index = 0
    temas_lde = None

    for t in range(1, k_temas + 1):
        nombre_tema = f"{t}"
        preguntas_lde = None

        for p in range(1, max_preguntas_por_tema + 1):
            nombre_pregunta = f"{t}.{p}"
            encuestados_lde = None
            cantidad = encuestados_por_pregunta

            restante = total_encuestados - encuestado_index
            if restante <= 0:
                break
            if cantidad > restante:
                cantidad = restante

            for _ in range(cantidad):
                enc = encuestados_disponibles[encuestado_index]
                encuestado_index += 1
                encuestados_lde = List_Insert_End(encuestados_lde, enc)

            pregunta = Pregunta(pregunta_id, nombre_pregunta, encuestados_lde)
            preguntas_lde = List_Insert_End(preguntas_lde, pregunta)
            pregunta_id += 1

        tema = Tema(tema_id, nombre_tema, preguntas_lde)
        temas_lde = List_Insert_End(temas_lde, tema)
        tema_id += 1

    return Encuesta(
        K=k_temas,
        M=max_preguntas_por_tema,
        Nmin=nmin,
        Nmax=nmax,
        Temas=temas_lde
    )

def insertar_abb(raiz, nodo):
    if raiz is None:
        return abb(nodo)
    if nodo.id < raiz.val.id:
        raiz.left = insertar_abb(raiz.left, nodo)
    else:
        raiz.right = insertar_abb(raiz.right, nodo)
    return raiz

def insertar_tema_abb(raiz, tema):
    if raiz is None:
        return abb(tema)
    if tema.id < raiz.val.id:
        raiz.left = insertar_tema_abb(raiz.left, tema)
    else:
        raiz.right = insertar_tema_abb(raiz.right, tema)
    return raiz

def insertar_pregunta_abb(raiz, pregunta):
    if raiz is None:
        return abb(pregunta)
    if pregunta.id < raiz.val.id:
        raiz.left = insertar_pregunta_abb(raiz.left, pregunta)
    else:
        raiz.right = insertar_pregunta_abb(raiz.right, pregunta)
    return raiz

def generar_encuesta_simulada_ABB_determinista(
    k_temas: int,
    max_preguntas_por_tema: int,
    total_encuestados: int,
    nmin: int,
    nmax: int
):
    
    encuestado_id = 1
    pregunta_id = 1
    tema_id = 1
    encuestados_disponibles = []

    # se crena encuestados
    for _ in range(total_encuestados):
        nombre = fake.name()
        experticia = random.randint(0, 10)
        opinion = random.randint(0, 10)
        encuestados_disponibles.append(Encuestado(encuestado_id, nombre, experticia, opinion))
        encuestado_id += 1

    random.shuffle(encuestados_disponibles)

    # se calcula una distribución para cada pregunta
    total_preguntas = k_temas * max_preguntas_por_tema
    encuestados_por_pregunta = ceil(total_encuestados / total_preguntas)
    encuestados_por_pregunta = min(encuestados_por_pregunta, nmax)

    encuestado_index = 0
    temas_abb = None

    for t in range(1, k_temas + 1):
        nombre_tema = f"{t}"
        preguntas_abb = None

        for p in range(1, max_preguntas_por_tema + 1):
            nombre_pregunta = f"{t}.{p}"

            cantidad = encuestados_por_pregunta
            restante = total_encuestados - encuestado_index
            if restante <= 0:
                break
            if cantidad > restante:
                cantidad = restante

            encuestados_abb = None
            for _ in range(cantidad):
                enc = encuestados_disponibles[encuestado_index]
                encuestado_index += 1
                encuestados_abb = insertar_abb(encuestados_abb, enc)

            pregunta = Pregunta(pregunta_id, nombre_pregunta, encuestados_abb)
            preguntas_abb = insertar_pregunta_abb(preguntas_abb, pregunta)
            pregunta_id += 1

        tema = Tema(tema_id, nombre_tema, preguntas_abb)
        temas_abb = insertar_tema_abb(temas_abb, tema)
        tema_id += 1

    return Encuesta(K=k_temas, M=max_preguntas_por_tema, Nmin=nmin, Nmax=nmax, Temas=temas_abb)
