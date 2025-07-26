import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def cargar_datos():
    """Carga los datos del archivo CSV"""
    try:
        df = pd.read_csv('benchmark_resultados.csv')
        return df
    except FileNotFoundError:
        print("Error: No se encontró el archivo benchmark_resultados.csv")
        return None

def crear_graficas(df):
    """Crea las gráficas de comparación de rendimiento"""
    
    # Configurar el estilo de las gráficas
    plt.style.use('default')
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Comparación de Rendimiento: Listas Doblemente Enlazadas vs Árboles Binarios de Búsqueda', 
                 fontsize=16, fontweight='bold')
    
    # Colores para las líneas
    colores_lde = ['#1f77b4', '#ff7f0e', '#2ca02c']
    colores_abb = ['#d62728', '#9467bd', '#8c564b']
    
    # Gráfica 1: Punto 4 - Ordenar encuestados por experticia
    ax1 = axes[0, 0]
    ax1.plot(df['tamaño_entrada'], df['tiempo_p4_lde_ms'], 
             marker='o', linewidth=2, markersize=6, color=colores_lde[0], 
             label='Lista Doblemente Enlazada')
    ax1.plot(df['tamaño_entrada'], df['tiempo_p4_abb_ms'], 
             marker='s', linewidth=2, markersize=6, color=colores_abb[0], 
             label='Árbol Binario de Búsqueda')
    ax1.set_xlabel('Tamaño de Entrada (Número de Encuestados)')
    ax1.set_ylabel('Tiempo (ms)')
    ax1.set_title('Punto 4: Ordenar Encuestados por Experticia')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    
    # Gráfica 2: Punto 8 - Pregunta con menor mediana
    ax2 = axes[0, 1]
    ax2.plot(df['tamaño_entrada'], df['tiempo_p8_lde_ms'], 
             marker='o', linewidth=2, markersize=6, color=colores_lde[1], 
             label='Lista Doblemente Enlazada')
    ax2.plot(df['tamaño_entrada'], df['tiempo_p8_abb_ms'], 
             marker='s', linewidth=2, markersize=6, color=colores_abb[1], 
             label='Árbol Binario de Búsqueda')
    ax2.set_xlabel('Tamaño de Entrada (Número de Encuestados)')
    ax2.set_ylabel('Tiempo (ms)')
    ax2.set_title('Punto 8: Pregunta con Menor Mediana')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    
    # Gráfica 3: Punto 12 - Pregunta con mayor consenso
    ax3 = axes[1, 0]
    ax3.plot(df['tamaño_entrada'], df['tiempo_p12_lde_ms'], 
             marker='o', linewidth=2, markersize=6, color=colores_lde[2], 
             label='Lista Doblemente Enlazada')
    ax3.plot(df['tamaño_entrada'], df['tiempo_p12_abb_ms'], 
             marker='s', linewidth=2, markersize=6, color=colores_abb[2], 
             label='Árbol Binario de Búsqueda')
    ax3.set_xlabel('Tamaño de Entrada (Número de Encuestados)')
    ax3.set_ylabel('Tiempo (ms)')
    ax3.set_title('Punto 12: Pregunta con Mayor Consenso')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    ax3.set_xscale('log')
    ax3.set_yscale('log')
    
    # Gráfica 4: Comparación general (promedio de los 3 puntos)
    ax4 = axes[1, 1]
    tiempo_promedio_lde = (df['tiempo_p4_lde_ms'] + df['tiempo_p8_lde_ms'] + df['tiempo_p12_lde_ms']) / 3
    tiempo_promedio_abb = (df['tiempo_p4_abb_ms'] + df['tiempo_p8_abb_ms'] + df['tiempo_p12_abb_ms']) / 3
    
    ax4.plot(df['tamaño_entrada'], tiempo_promedio_lde, 
             marker='o', linewidth=2, markersize=6, color='#1f77b4', 
             label='Lista Doblemente Enlazada (Promedio)')
    ax4.plot(df['tamaño_entrada'], tiempo_promedio_abb, 
             marker='s', linewidth=2, markersize=6, color='#d62728', 
             label='Árbol Binario de Búsqueda (Promedio)')
    ax4.set_xlabel('Tamaño de Entrada (Número de Encuestados)')
    ax4.set_ylabel('Tiempo Promedio (ms)')
    ax4.set_title('Comparación General (Promedio de los 3 Puntos)')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    ax4.set_xscale('log')
    ax4.set_yscale('log')
    
    plt.tight_layout()
    plt.savefig('benchmark_graficas.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return fig

def generar_tabla_resumen(df):
    """Genera una tabla resumen de los resultados"""
    
    print("\n" + "="*100)
    print("TABLA RESUMEN DE RENDIMIENTO")
    print("="*100)
    
    # Calcular estadísticas
    stats = {
        'Punto 4 - LDE': {
            'Promedio': df['tiempo_p4_lde_ms'].mean(),
            'Mínimo': df['tiempo_p4_lde_ms'].min(),
            'Máximo': df['tiempo_p4_lde_ms'].max(),
            'Desv. Est.': df['tiempo_p4_lde_ms'].std()
        },
        'Punto 4 - ABB': {
            'Promedio': df['tiempo_p4_abb_ms'].mean(),
            'Mínimo': df['tiempo_p4_abb_ms'].min(),
            'Máximo': df['tiempo_p4_abb_ms'].max(),
            'Desv. Est.': df['tiempo_p4_abb_ms'].std()
        },
        'Punto 8 - LDE': {
            'Promedio': df['tiempo_p8_lde_ms'].mean(),
            'Mínimo': df['tiempo_p8_lde_ms'].min(),
            'Máximo': df['tiempo_p8_lde_ms'].max(),
            'Desv. Est.': df['tiempo_p8_lde_ms'].std()
        },
        'Punto 8 - ABB': {
            'Promedio': df['tiempo_p8_abb_ms'].mean(),
            'Mínimo': df['tiempo_p8_abb_ms'].min(),
            'Máximo': df['tiempo_p8_abb_ms'].max(),
            'Desv. Est.': df['tiempo_p8_abb_ms'].std()
        },
        'Punto 12 - LDE': {
            'Promedio': df['tiempo_p12_lde_ms'].mean(),
            'Mínimo': df['tiempo_p12_lde_ms'].min(),
            'Máximo': df['tiempo_p12_lde_ms'].max(),
            'Desv. Est.': df['tiempo_p12_lde_ms'].std()
        },
        'Punto 12 - ABB': {
            'Promedio': df['tiempo_p12_abb_ms'].mean(),
            'Mínimo': df['tiempo_p12_abb_ms'].min(),
            'Máximo': df['tiempo_p12_abb_ms'].max(),
            'Desv. Est.': df['tiempo_p12_abb_ms'].std()
        }
    }
    
    # Imprimir tabla
    print(f"{'Métrica':<20} {'Promedio (ms)':<15} {'Mínimo (ms)':<15} {'Máximo (ms)':<15} {'Desv. Est.':<15}")
    print("-" * 100)
    
    for metrica, valores in stats.items():
        print(f"{metrica:<20} {valores['Promedio']:<15.3f} {valores['Mínimo']:<15.3f} "
              f"{valores['Máximo']:<15.3f} {valores['Desv. Est.']:<15.3f}")
    
    # Análisis de rendimiento
    print("\n" + "="*100)
    print("ANÁLISIS DE RENDIMIENTO")
    print("="*100)
    
    # Comparar promedios
    print("Comparación de Promedios (ms):")
    print(f"  Punto 4:  LDE = {stats['Punto 4 - LDE']['Promedio']:.3f} vs ABB = {stats['Punto 4 - ABB']['Promedio']:.3f}")
    print(f"  Punto 8:  LDE = {stats['Punto 8 - LDE']['Promedio']:.3f} vs ABB = {stats['Punto 8 - ABB']['Promedio']:.3f}")
    print(f"  Punto 12: LDE = {stats['Punto 12 - LDE']['Promedio']:.3f} vs ABB = {stats['Punto 12 - ABB']['Promedio']:.3f}")
    
    # Determinar cuál es más rápido en cada punto
    print("\nEstructura más rápida por punto:")
    if stats['Punto 4 - LDE']['Promedio'] < stats['Punto 4 - ABB']['Promedio']:
        print("  Punto 4: Lista Doblemente Enlazada")
    else:
        print("  Punto 4: Árbol Binario de Búsqueda")
    
    if stats['Punto 8 - LDE']['Promedio'] < stats['Punto 8 - ABB']['Promedio']:
        print("  Punto 8: Lista Doblemente Enlazada")
    else:
        print("  Punto 8: Árbol Binario de Búsqueda")
    
    if stats['Punto 12 - LDE']['Promedio'] < stats['Punto 12 - ABB']['Promedio']:
        print("  Punto 12: Lista Doblemente Enlazada")
    else:
        print("  Punto 12: Árbol Binario de Búsqueda")

def main():
    """Función principal"""
    print("Generando gráficas de benchmark...")
    
    # Cargar datos
    df = cargar_datos()
    if df is None:
        return
    
    # Crear gráficas
    fig = crear_graficas(df)
    
    # Generar tabla resumen
    generar_tabla_resumen(df)
    
    print(f"\nGráficas guardadas en: benchmark_graficas.png")
    print("¡Análisis completado!")

if __name__ == "__main__":
    main() 