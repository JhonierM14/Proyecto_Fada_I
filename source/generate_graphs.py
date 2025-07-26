import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib import rcParams

# Configurar estilo para gráficas similares a las del informe
plt.style.use('default')
rcParams['font.size'] = 12
rcParams['axes.titlesize'] = 16
rcParams['axes.labelsize'] = 14
rcParams['legend.fontsize'] = 12
rcParams['figure.titlesize'] = 18

def generar_grafica_punto4():
    """Genera gráfica para Punto 4: Merge Sort vs Complejidad Teórica O(n log n)"""
    
    # Leer datos CSV
    df = pd.read_csv('resultados/punto4_merge_sort.csv')
    
    # Crear figura
    fig, ax = plt.subplots(figsize=(15, 11))
    
    # Datos experimentales
    x_exp = df['Num_Encuestados'].values
    y_exp = df['Tiempo_ms'].values
    
    # Curva teórica O(n log n)
    x_teorico = np.linspace(min(x_exp), max(x_exp), 100)
    # Ajustar constante para que la curva teórica se ajuste a los datos
    constante = np.max(y_exp) / (np.max(x_exp) * np.log(np.max(x_exp)))
    y_teorico = constante * x_teorico * np.log(x_teorico)
    
    # Graficar datos experimentales
    ax.plot(x_exp, y_exp, 'o-', color='blue', linewidth=2, markersize=6, 
            label='Tiempo Experimental', markeredgecolor='black', markeredgewidth=0.5)
    
    # Graficar curva teórica
    ax.plot(x_teorico, y_teorico, '--', color='red', linewidth=2, 
            label='Curva Teórica O(n log n)')
    
    # Configurar ejes
    ax.set_xlabel('Número de Encuestados (n)', fontsize=14)
    ax.set_ylabel('Tiempo de Ejecución (ms)', fontsize=14)
    ax.set_title('Punto 4: Rendimiento Merge Sort vs Complejidad Teórica', fontsize=16, fontweight='bold')
    
    # Configurar grid
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_axisbelow(True)
    
    # Configurar leyenda
    ax.legend(loc='upper left', fontsize=12)
    
    # Ajustar límites
    ax.set_xlim(0, max(x_exp) * 1.1)
    ax.set_ylim(0, max(y_exp) * 1.1)
    
    # Guardar gráfica
    plt.tight_layout()
    plt.savefig('resultados/grafica_punto4.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Gráfica Punto 4 generada: resultado/grafica_punto4.png")

def generar_grafica_punto8():
    """Genera gráfica para Punto 8: Insertion Sort vs Complejidad Teórica O(p²)"""
    
    # Leer datos CSV
    df = pd.read_csv('resultados/punto8_insertion_sort.csv')
    
    # Crear figura
    fig, ax = plt.subplots(figsize=(15, 11))
    
    # Datos experimentales
    x_exp = df['Num_Preguntas'].values
    y_exp = df['Tiempo_ms'].values
    
    # Curva teórica O(p²)
    x_teorico = np.linspace(min(x_exp), max(x_exp), 100)
    # Ajustar constante para que la curva teórica se ajuste a los datos
    constante = np.max(y_exp) / (np.max(x_exp) ** 2)
    y_teorico = constante * x_teorico ** 2
    
    # Graficar datos experimentales
    ax.plot(x_exp, y_exp, 's-', color='green', linewidth=2, markersize=6, 
            label='Tiempo Experimental', markeredgecolor='black', markeredgewidth=0.5)
    
    # Graficar curva teórica
    ax.plot(x_teorico, y_teorico, '--', color='red', linewidth=2, 
            label='Curva Teórica O(p²)')
    
    # Configurar ejes
    ax.set_xlabel('Número de Preguntas (p)', fontsize=14)
    ax.set_ylabel('Tiempo de Ejecución (ms)', fontsize=14)
    ax.set_title('Punto 8: Rendimiento Insertion Sort vs Complejidad Teórica', fontsize=16, fontweight='bold')
    
    # Configurar grid
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_axisbelow(True)
    
    # Configurar leyenda
    ax.legend(loc='upper left', fontsize=12)
    
    # Ajustar límites
    ax.set_xlim(0, max(x_exp) * 1.1)
    ax.set_ylim(0, max(y_exp) * 1.1)
    
    # Guardar gráfica
    plt.tight_layout()
    plt.savefig('resultados/grafica_punto8.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Gráfica Punto 8 generada: resultado/grafica_punto8.png")

def generar_grafica_punto12():
    """Genera gráfica para Punto 12: Insertion Sort vs Complejidad Teórica O(p²)"""
    
    # Leer datos CSV
    df = pd.read_csv('resultados/punto12_insertion_sort.csv')
    
    # Crear figura
    fig, ax = plt.subplots(figsize=(15, 11))
    
    # Datos experimentales
    x_exp = df['Num_Preguntas'].values
    y_exp = df['Tiempo_ms'].values
    
    # Curva teórica O(p²)
    x_teorico = np.linspace(min(x_exp), max(x_exp), 100)
    # Ajustar constante para que la curva teórica se ajuste a los datos
    constante = np.max(y_exp) / (np.max(x_exp) ** 2)
    y_teorico = constante * x_teorico ** 2
    
    # Graficar datos experimentales
    ax.plot(x_exp, y_exp, '^-', color='purple', linewidth=2, markersize=6, 
            label='Tiempo Experimental', markeredgecolor='black', markeredgewidth=0.5)
    
    # Graficar curva teórica
    ax.plot(x_teorico, y_teorico, '--', color='red', linewidth=2, 
            label='Curva Teórica O(p²)')
    
    # Configurar ejes
    ax.set_xlabel('Número de Preguntas (p)', fontsize=14)
    ax.set_ylabel('Tiempo de Ejecución (ms)', fontsize=14)
    ax.set_title('Punto 12: Rendimiento vs Complejidad Teórica', fontsize=16, fontweight='bold')
    
    # Configurar grid
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_axisbelow(True)
    
    # Configurar leyenda
    ax.legend(loc='upper left', fontsize=12)
    
    # Ajustar límites
    ax.set_xlim(0, max(x_exp) * 1.1)
    ax.set_ylim(0, max(y_exp) * 1.1)
    
    # Guardar gráfica
    plt.tight_layout()
    plt.savefig('resultados/grafica_punto12.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Gráfica Punto 12 generada: resultado/grafica_punto12.png")

def generar_grafica_comparativa():
    """Genera gráfica comparativa de los tres algoritmos"""
    
    # Leer datos CSV
    df_p4 = pd.read_csv('resultados/punto4_merge_sort.csv')
    df_p8 = pd.read_csv('resultados/punto8_insertion_sort.csv')
    df_p12 = pd.read_csv('resultados/punto12_insertion_sort.csv')
    
    # Crear figura
    fig, ax = plt.subplots(figsize=(16, 12))
    
    # Datos experimentales
    x_p4 = df_p4['Num_Encuestados'].values
    y_p4 = df_p4['Tiempo_ms'].values
    
    x_p8 = df_p8['Num_Preguntas'].values
    y_p8 = df_p8['Tiempo_ms'].values
    
    x_p12 = df_p12['Num_Preguntas'].values
    y_p12 = df_p12['Tiempo_ms'].values
    
    # Graficar datos experimentales
    ax.plot(x_p4, y_p4, 'o-', color='blue', linewidth=2, markersize=6, 
            label='Punto 4: Merge Sort O(n log n)', markeredgecolor='black', markeredgewidth=0.5)
    
    ax.plot(x_p8, y_p8, 's-', color='green', linewidth=2, markersize=6, 
            label='Punto 8: Insertion Sort O(p² + p·m²)', markeredgecolor='black', markeredgewidth=0.5)
    
    ax.plot(x_p12, y_p12, '^-', color='purple', linewidth=2, markersize=6, 
            label='Punto 12: Insertion Sort O(p² + p·m)', markeredgecolor='black', markeredgewidth=0.5)
    
    # Configurar ejes
    ax.set_xlabel('Tamaño del Conjunto de Datos', fontsize=14)
    ax.set_ylabel('Tiempo de Ejecución (ms)', fontsize=14)
    ax.set_title('Comparación de Complejidad: Tres Estrategias Algorítmicas', fontsize=16, fontweight='bold')
    
    # Configurar escala logarítmica en Y
    ax.set_yscale('log')
    
    # Configurar grid
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_axisbelow(True)
    
    # Configurar leyenda
    ax.legend(loc='upper left', fontsize=12)
    
    # Ajustar límites
    max_x = max(max(x_p4), max(x_p8), max(x_p12))
    ax.set_xlim(0, max_x * 1.1)
    
    # Guardar gráfica
    plt.tight_layout()
    plt.savefig('resultados/grafica_comparativa.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Gráfica Comparativa generada: resultado/grafica_comparativa.png")

def generar_todas_graficas():
    """Genera todas las gráficas de análisis"""
    
    print("Generando gráficas de análisis de complejidad...")
    
    # Verificar que existen los archivos CSV
    archivos_csv = [
        'resultados/punto4_merge_sort.csv',
        'resultados/punto8_insertion_sort.csv',
        'resultados/punto12_insertion_sort.csv'
    ]
    
    for archivo in archivos_csv:
        if not os.path.exists(archivo):
            print(f"Error: No se encontró el archivo {archivo}")
            print("Ejecuta primero run_performance_tests.py para generar los datos CSV")
            return
    
    # Generar gráficas individuales
    generar_grafica_punto4()
    generar_grafica_punto8()
    generar_grafica_punto12()
    generar_grafica_comparativa()
    
    print("\n¡Todas las gráficas han sido generadas exitosamente!")
    print("Archivos generados en el directorio 'resultados':")
    print("  - grafica_punto4.png")
    print("  - grafica_punto8.png")
    print("  - grafica_punto12.png")
    print("  - grafica_comparativa.png")

if __name__ == "__main__":
    generar_todas_graficas() 