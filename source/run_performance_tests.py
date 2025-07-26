import time
import csv
import os
import sys
from pathlib import Path

# Agregar el directorio actual al path para importar módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from LDE_utils import *
from data import *

def contar_encuestados_y_preguntas(archivo_prueba):
    """Cuenta el número de encuestados y preguntas en un archivo de prueba"""
    try:
        with open(archivo_prueba, 'r', encoding='utf-8') as f:
            contenido = f.read()
        
        # Contar líneas que contienen encuestados (tienen "Experticia:")
        encuestados = sum(1 for linea in contenido.split('\n') if 'Experticia:' in linea)
        
        # Contar preguntas (líneas que contienen "Tema" y luego grupos de números)
        preguntas = 0
        lineas = contenido.split('\n')
        for i, linea in enumerate(lineas):
            if linea.startswith('Tema'):
                # Contar grupos de números después de cada tema
                j = i + 1
                while j < len(lineas) and lineas[j].strip() and not lineas[j].startswith('Tema'):
                    if lineas[j].strip().startswith('{') and lineas[j].strip().endswith('}'):
                        preguntas += 1
                    j += 1
        
        return encuestados, preguntas
    except Exception as e:
        print(f"Error al contar en {archivo_prueba}: {e}")
        return 0, 0

def medir_tiempo_punto4(archivo_prueba, repeticiones=5):
    """Mide el tiempo de ejecución del Punto 4 (Merge Sort)"""
    tiempos = []
    
    for _ in range(repeticiones):
        # Reinicializar datos
        global encuesta
        encuesta = Texto_a_Encuesta(os.path.basename(archivo_prueba))
        
        # Medir tiempo
        inicio = time.perf_counter()
        punto4_LDE()
        fin = time.perf_counter()
        
        tiempo_ms = (fin - inicio) * 1000
        tiempos.append(tiempo_ms)
    
    return tiempos

def medir_tiempo_punto8(archivo_prueba, repeticiones=5):
    """Mide el tiempo de ejecución del Punto 8 (Insertion Sort para mediana)"""
    tiempos = []
    
    for _ in range(repeticiones):
        # Reinicializar datos
        global encuesta
        encuesta = Texto_a_Encuesta(os.path.basename(archivo_prueba))
        
        # Medir tiempo
        inicio = time.perf_counter()
        punto8_LDE()
        fin = time.perf_counter()
        
        tiempo_ms = (fin - inicio) * 1000
        tiempos.append(tiempo_ms)
    
    return tiempos

def medir_tiempo_punto12(archivo_prueba, repeticiones=5):
    """Mide el tiempo de ejecución del Punto 12 (Insertion Sort para consenso)"""
    tiempos = []
    
    for _ in range(repeticiones):
        # Reinicializar datos
        global encuesta
        encuesta = Texto_a_Encuesta(os.path.basename(archivo_prueba))
        
        # Medir tiempo
        inicio = time.perf_counter()
        punto12_LDE()
        fin = time.perf_counter()
        
        tiempo_ms = (fin - inicio) * 1000
        tiempos.append(tiempo_ms)
    
    return tiempos

def calcular_estadisticas(tiempos):
    """Calcula estadísticas de los tiempos de ejecución"""
    if not tiempos:
        return 0, 0
    
    tiempo_promedio = sum(tiempos) / len(tiempos)
    
    # Calcular desviación estándar
    if len(tiempos) > 1:
        varianza = sum((t - tiempo_promedio) ** 2 for t in tiempos) / (len(tiempos) - 1)
        desv_estandar = varianza ** 0.5
    else:
        desv_estandar = 0
    
    return tiempo_promedio, desv_estandar

def ejecutar_pruebas_rendimiento():
    """Ejecuta todas las pruebas de rendimiento y genera archivos CSV"""
    
    # Obtener lista de archivos de prueba
    archivos_prueba = []
    for archivo in os.listdir("tests"):
        if archivo.endswith(".txt"):
            archivos_prueba.append(os.path.join("tests", archivo))
    
    # Ordenar archivos por tamaño (número en el nombre)
    archivos_prueba.sort(key=lambda x: int(''.join(filter(str.isdigit, os.path.basename(x)))) if any(c.isdigit() for c in os.path.basename(x)) else 0)
    
    print(f"Ejecutando pruebas de rendimiento para {len(archivos_prueba)} archivos...")
    
    # Datos para CSV
    datos_punto4 = []
    datos_punto8 = []
    datos_punto12 = []
    
    for archivo in archivos_prueba:
        print(f"\nProcesando: {os.path.basename(archivo)}")
        
        # Contar encuestados y preguntas
        num_encuestados, num_preguntas = contar_encuestados_y_preguntas(archivo)
        
        if num_encuestados == 0 or num_preguntas == 0:
            print(f"  Saltando {archivo} - datos inválidos")
            continue
        
        print(f"  Encuestados: {num_encuestados}, Preguntas: {num_preguntas}")
        
        # Medir Punto 4 (Merge Sort)
        print("  Probando Punto 4...")
        tiempos_p4 = medir_tiempo_punto4(archivo)
        tiempo_p4, desv_p4 = calcular_estadisticas(tiempos_p4)
        datos_punto4.append([num_encuestados, tiempo_p4, desv_p4])
        
        # Medir Punto 8 (Insertion Sort para mediana)
        print("  Probando Punto 8...")
        tiempos_p8 = medir_tiempo_punto8(archivo)
        tiempo_p8, desv_p8 = calcular_estadisticas(tiempos_p8)
        datos_punto8.append([num_preguntas, tiempo_p8, desv_p8])
        
        # Medir Punto 12 (Insertion Sort para consenso)
        print("  Probando Punto 12...")
        tiempos_p12 = medir_tiempo_punto12(archivo)
        tiempo_p12, desv_p12 = calcular_estadisticas(tiempos_p12)
        datos_punto12.append([num_preguntas, tiempo_p12, desv_p12])
        
        print(f"  Tiempos: P4={tiempo_p4:.3f}ms, P8={tiempo_p8:.3f}ms, P12={tiempo_p12:.3f}ms")
    
    # Crear directorio para resultados si no existe
    os.makedirs("resultados", exist_ok=True)
    
    # Guardar datos Punto 4 (Merge Sort)
    with open("resultados/punto4_merge_sort.csv", 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Num_Encuestados', 'Tiempo_ms', 'Desv_Estandar'])
        for fila in datos_punto4:
            writer.writerow(fila)
    
    # Guardar datos Punto 8 (Insertion Sort para mediana)
    with open("resultados/punto8_insertion_sort.csv", 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Num_Preguntas', 'Tiempo_ms', 'Desv_Estandar'])
        for fila in datos_punto8:
            writer.writerow(fila)
    
    # Guardar datos Punto 12 (Insertion Sort para consenso)
    with open("resultados/punto12_insertion_sort.csv", 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Num_Preguntas', 'Tiempo_ms', 'Desv_Estandar'])
        for fila in datos_punto12:
            writer.writerow(fila)
    
    print(f"\n¡Pruebas completadas!")
    print(f"Archivos CSV generados en directorio 'resultados':")
    print(f"  - punto4_merge_sort.csv")
    print(f"  - punto8_insertion_sort.csv")
    print(f"  - punto12_insertion_sort.csv")

if __name__ == "__main__":
    ejecutar_pruebas_rendimiento() 