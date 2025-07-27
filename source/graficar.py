import matplotlib.pyplot as plt
from LDE_utils import *
from abb_utils import *
from data import *
from generate_data import generar_encuesta_simulada_ABB_determinista, generar_encuesta_simulada_LDE_determinista
import time, random

def generar_entradas_para_grafica_incremental(
    n_muestras=10,              # cuántas entradas se generarán
    k=3,                        # número fijo de temas
    m=4,                        # número fijo de preguntas máximas por tema
    encuestados_min=50,         # cantidad mínima total de encuestados
    encuestados_max=10000,      # cantidad máxima total de encuestados
    nmin=1,                     # mínimo encuestados por pregunta
    # nmax=5                    # máximo encuestados por pregunta
):
    """
    Genera entradas incrementales para evaluar rendimiento.
    :return: Lista de tuplas (encuesta_LDE, encuesta_ABB)
    """

    if generar_encuesta_simulada_LDE_determinista is None or generar_encuesta_simulada_ABB_determinista is None:
        raise ValueError("Funciones generadoras de encuestas no definidas.")

    entradas = []
    incremento = (encuestados_max - encuestados_min) // (n_muestras - 1)

    for i in range(n_muestras):
        total_encuestados = encuestados_min + i * incremento
        nmax = max(5, total_encuestados // (k * m))

        encuesta_LDE = generar_encuesta_simulada_LDE_determinista(k, m, total_encuestados, nmin, nmax)
        encuesta_ABB = generar_encuesta_simulada_ABB_determinista(k, m, total_encuestados, nmin, nmax)

        entradas.append((encuesta_LDE, encuesta_ABB))

    return entradas


def comparar_funciones_y_graficar(funcion1, funcion2, entradas, etiquetas=("LDE", "ABB")):
    """
    Compara dos funciones que acepten una entrada y retornen (tamano_entrada, tiempo)
    y grafica el tiempo en función del tamaño de entrada.

    :param funcion1: función basada en LDE
    :param funcion2: función basada en ABB
    :param entradas: lista de instancias de encuestas de distinto tamaño
    :param etiquetas: etiquetas para el gráfico ("LDE", "ABB")
    """

    tamaños1, tiempos1 = [], []
    tamaños2, tiempos2 = [], []

    for entrada_LDE, entrada_abb in entradas:
        t1, tiempo1 = funcion1(entrada_LDE)
        t2, tiempo2 = funcion2(entrada_abb)
        
        tamaños1.append(t1)
        tiempos1.append(tiempo1)

        tamaños2.append(t2)
        tiempos2.append(tiempo2)

    plt.plot(tamaños1, tiempos1, marker='o', label=etiquetas[0], color='blue')
    plt.plot(tamaños2, tiempos2, marker='o', label=etiquetas[1], color='green')
    plt.xlabel("Tamaño de entrada (cantidad de encuestados)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Comparación de funciones LDE vs ABB")
    plt.grid(True)
    plt.legend()
    plt.show()

entradas = generar_entradas_para_grafica_incremental()

comparar_funciones_y_graficar(punto2_LDE, punto2_Abb, entradas)

