import time
import csv
import os
from data import Texto_a_Encuesta
from LDE_utils import punto4_LDE, punto8_LDE, punto12_LDE
from abb_utils import punto4_Abb, punto8_Abb, punto12_Abb

def medir_tiempo(func, *args, **kwargs):
    """Mide el tiempo de ejecución de una función en milisegundos"""
    inicio = time.time()
    resultado = func(*args, **kwargs)
    fin = time.time()
    return (fin - inicio) * 1000, resultado

def ejecutar_benchmark():
    """Ejecuta el benchmark para todos los archivos de prueba"""
    
    # Lista de archivos de prueba ordenados por tamaño
    archivos_prueba = [
        "Test_50.txt", "Test_64.txt", "Test_100.txt", "Test_128.txt", 
        "Test_200.txt", "Test_256.txt", "Test_400.txt", "Test_512.txt",
        "Test_800.txt", "Test_1024.txt", "Test_2048.txt", "Test_4096.txt", 
        "Test_8192.txt"
    ]
    
    resultados = []
    
    for archivo in archivos_prueba:
        print(f"Procesando {archivo}...")
        
        try:
            # Cargar datos del archivo
            global encuesta
            encuesta = Texto_a_Encuesta(archivo)
            
            # Calcular tamaño total de datos
            total_encuestados = 0
            total_preguntas = 0
            for tema in encuesta._iterate_temas():
                for pregunta in tema._iterate_preguntas():
                    total_preguntas += 1
                    for encuestado in pregunta._iterate_encuestados():
                        total_encuestados += 1
            
            # Medir tiempo para Listas Doblemente Enlazadas
            tiempo_p4_lde, _ = medir_tiempo(punto4_LDE)
            tiempo_p8_lde, _ = medir_tiempo(punto8_LDE)
            tiempo_p12_lde, _ = medir_tiempo(punto12_LDE)
            
            # Medir tiempo para Árboles Binarios de Búsqueda
            tiempo_p4_abb, _ = medir_tiempo(punto4_Abb)
            tiempo_p8_abb, _ = medir_tiempo(punto8_Abb)
            tiempo_p12_abb, _ = medir_tiempo(punto12_Abb)
            
            # Guardar resultados
            resultado = {
                'archivo': archivo,
                'tamaño_entrada': total_encuestados,
                'total_preguntas': total_preguntas,
                'tiempo_p4_lde_ms': round(tiempo_p4_lde, 3),
                'tiempo_p8_lde_ms': round(tiempo_p8_lde, 3),
                'tiempo_p12_lde_ms': round(tiempo_p12_lde, 3),
                'tiempo_p4_abb_ms': round(tiempo_p4_abb, 3),
                'tiempo_p8_abb_ms': round(tiempo_p8_abb, 3),
                'tiempo_p12_abb_ms': round(tiempo_p12_abb, 3)
            }
            
            resultados.append(resultado)
            print(f"  ✓ Completado: {total_encuestados} encuestados, {total_preguntas} preguntas")
            
        except Exception as e:
            print(f"  ✗ Error procesando {archivo}: {str(e)}")
            continue
    
    return resultados

def guardar_csv(resultados, nombre_archivo="benchmark_resultados.csv"):
    """Guarda los resultados en un archivo CSV"""
    
    if not resultados:
        print("No hay resultados para guardar")
        return
    
    campos = [
        'archivo', 'tamaño_entrada', 'total_preguntas',
        'tiempo_p4_lde_ms', 'tiempo_p8_lde_ms', 'tiempo_p12_lde_ms',
        'tiempo_p4_abb_ms', 'tiempo_p8_abb_ms', 'tiempo_p12_abb_ms'
    ]
    
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
        writer = csv.DictWriter(archivo_csv, fieldnames=campos)
        writer.writeheader()
        writer.writerows(resultados)
    
    print(f"\nResultados guardados en: {nombre_archivo}")

def mostrar_resumen(resultados):
    """Muestra un resumen de los resultados"""
    
    if not resultados:
        print("No hay resultados para mostrar")
        return
    
    print("\n" + "="*80)
    print("RESUMEN DE BENCHMARK")
    print("="*80)
    print(f"{'Archivo':<15} {'Tamaño':<8} {'P4_LDE':<10} {'P8_LDE':<10} {'P12_LDE':<10} {'P4_ABB':<10} {'P8_ABB':<10} {'P12_ABB':<10}")
    print("-"*80)
    
    for resultado in resultados:
        print(f"{resultado['archivo']:<15} {resultado['tamaño_entrada']:<8} "
              f"{resultado['tiempo_p4_lde_ms']:<10.3f} {resultado['tiempo_p8_lde_ms']:<10.3f} "
              f"{resultado['tiempo_p12_lde_ms']:<10.3f} {resultado['tiempo_p4_abb_ms']:<10.3f} "
              f"{resultado['tiempo_p8_abb_ms']:<10.3f} {resultado['tiempo_p12_abb_ms']:<10.3f}")

if __name__ == "__main__":
    print("Iniciando benchmark de rendimiento...")
    print("Comparando Listas Doblemente Enlazadas vs Árboles Binarios de Búsqueda")
    print("="*80)
    
    # Ejecutar benchmark
    resultados = ejecutar_benchmark()
    
    # Mostrar resumen
    mostrar_resumen(resultados)
    
    # Guardar en CSV
    guardar_csv(resultados)
    
    print("\n¡Benchmark completado!") 