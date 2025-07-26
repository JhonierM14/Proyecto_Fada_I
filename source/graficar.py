import matplotlib.pyplot as plt
from LDE_utils import *
from abb_utils import *
from data import *
import time

entradas = [Texto_a_Encuesta("Test1.txt"), Texto_a_Encuesta("Test2.txt"), Texto_a_Encuesta("Test3.txt")]

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
    plt.xlabel("Tamaño de entrada (cantidad de preguntas o nodos)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Comparación de funciones LDE vs ABB")
    plt.grid(True)
    plt.legend()
    plt.show()

comparar_funciones_y_graficar(punto6_LDE, punto6_Abb, entradas)