import csv
import matplotlib.pyplot as plt
import numpy as np

def read_benchmark_data(csv_file='benchmark_results.csv'):
    """Read benchmark data from CSV file"""
    data = []
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append({
                'size': int(row['size']),
                'num_encuestados': int(row['num_encuestados']),
                'lde_punto4': float(row['lde_punto4']),
                'lde_punto8': float(row['lde_punto8']),
                'lde_punto12': float(row['lde_punto12']),
                'abb_punto4': float(row['abb_punto4']),
                'abb_punto8': float(row['abb_punto8']),
                'abb_punto12': float(row['abb_punto12'])
            })
    return data

def plot_punto4_comparison(data):
    """Generate detailed plot for Punto 4"""
    sizes = [d['size'] for d in data]
    lde_times = [d['lde_punto4'] for d in data]
    abb_times = [d['abb_punto4'] for d in data]
    
    plt.figure(figsize=(12, 8))
    
    # Main plot
    plt.subplot(2, 2, 1)
    plt.plot(sizes, lde_times, 'o-', label='LDE', linewidth=2, markersize=8, color='blue')
    plt.plot(sizes, abb_times, 's-', label='ABB', linewidth=2, markersize=8, color='red')
    plt.xlabel('Tamaño de entrada')
    plt.ylabel('Tiempo (ms)')
    plt.title('Punto 4: Ordenar encuestados por experticia\nComparación LDE vs ABB')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    # Linear scale plot
    plt.subplot(2, 2, 2)
    plt.plot(sizes, lde_times, 'o-', label='LDE', linewidth=2, markersize=8, color='blue')
    plt.plot(sizes, abb_times, 's-', label='ABB', linewidth=2, markersize=8, color='red')
    plt.xlabel('Tamaño de entrada')
    plt.ylabel('Tiempo (ms)')
    plt.title('Punto 4: Escala Lineal')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Speedup ratio
    plt.subplot(2, 2, 3)
    speedup = [lde/abb for lde, abb in zip(lde_times, abb_times)]
    plt.plot(sizes, speedup, '^-', color='green', linewidth=2, markersize=8)
    plt.xlabel('Tamaño de entrada')
    plt.ylabel('Factor de mejora (LDE/ABB)')
    plt.title('Factor de Mejora: ABB vs LDE')
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.axhline(y=1, color='red', linestyle='--', alpha=0.7, label='Línea base (1x)')
    plt.legend()
    
    # Time difference
    plt.subplot(2, 2, 4)
    time_diff = [lde - abb for lde, abb in zip(lde_times, abb_times)]
    plt.bar(range(len(sizes)), time_diff, color='orange', alpha=0.7)
    plt.xlabel('Índice del archivo de prueba')
    plt.ylabel('Diferencia de tiempo (ms)')
    plt.title('Diferencia: LDE - ABB')
    plt.grid(True, alpha=0.3)
    plt.xticks(range(len(sizes)), [str(s) for s in sizes], rotation=45)
    
    plt.tight_layout()
    plt.savefig('punto4_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_punto8_comparison(data):
    """Generate detailed plot for Punto 8"""
    sizes = [d['size'] for d in data]
    lde_times = [d['lde_punto8'] for d in data]
    abb_times = [d['abb_punto8'] for d in data]
    
    plt.figure(figsize=(12, 8))
    
    # Main plot
    plt.subplot(2, 2, 1)
    plt.plot(sizes, lde_times, 'o-', label='LDE', linewidth=2, markersize=8, color='blue')
    plt.plot(sizes, abb_times, 's-', label='ABB', linewidth=2, markersize=8, color='red')
    plt.xlabel('Tamaño de entrada')
    plt.ylabel('Tiempo (ms)')
    plt.title('Punto 8: Pregunta con menor mediana\nComparación LDE vs ABB')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    # Linear scale plot
    plt.subplot(2, 2, 2)
    plt.plot(sizes, lde_times, 'o-', label='LDE', linewidth=2, markersize=8, color='blue')
    plt.plot(sizes, abb_times, 's-', label='ABB', linewidth=2, markersize=8, color='red')
    plt.xlabel('Tamaño de entrada')
    plt.ylabel('Tiempo (ms)')
    plt.title('Punto 8: Escala Lineal')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Speedup ratio
    plt.subplot(2, 2, 3)
    speedup = [lde/abb for lde, abb in zip(lde_times, abb_times)]
    plt.plot(sizes, speedup, '^-', color='green', linewidth=2, markersize=8)
    plt.xlabel('Tamaño de entrada')
    plt.ylabel('Factor de mejora (LDE/ABB)')
    plt.title('Factor de Mejora: ABB vs LDE')
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.axhline(y=1, color='red', linestyle='--', alpha=0.7, label='Línea base (1x)')
    plt.legend()
    
    # Time difference
    plt.subplot(2, 2, 4)
    time_diff = [lde - abb for lde, abb in zip(lde_times, abb_times)]
    plt.bar(range(len(sizes)), time_diff, color='orange', alpha=0.7)
    plt.xlabel('Índice del archivo de prueba')
    plt.ylabel('Diferencia de tiempo (ms)')
    plt.title('Diferencia: LDE - ABB')
    plt.grid(True, alpha=0.3)
    plt.xticks(range(len(sizes)), [str(s) for s in sizes], rotation=45)
    
    plt.tight_layout()
    plt.savefig('punto8_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_punto12_comparison(data):
    """Generate detailed plot for Punto 12"""
    sizes = [d['size'] for d in data]
    lde_times = [d['lde_punto12'] for d in data]
    abb_times = [d['abb_punto12'] for d in data]
    
    plt.figure(figsize=(12, 8))
    
    # Main plot
    plt.subplot(2, 2, 1)
    plt.plot(sizes, lde_times, 'o-', label='LDE', linewidth=2, markersize=8, color='blue')
    plt.plot(sizes, abb_times, 's-', label='ABB', linewidth=2, markersize=8, color='red')
    plt.xlabel('Tamaño de entrada')
    plt.ylabel('Tiempo (ms)')
    plt.title('Punto 12: Pregunta con mayor consenso\nComparación LDE vs ABB')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    # Linear scale plot
    plt.subplot(2, 2, 2)
    plt.plot(sizes, lde_times, 'o-', label='LDE', linewidth=2, markersize=8, color='blue')
    plt.plot(sizes, abb_times, 's-', label='ABB', linewidth=2, markersize=8, color='red')
    plt.xlabel('Tamaño de entrada')
    plt.ylabel('Tiempo (ms)')
    plt.title('Punto 12: Escala Lineal')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Speedup ratio
    plt.subplot(2, 2, 3)
    speedup = [lde/abb for lde, abb in zip(lde_times, abb_times)]
    plt.plot(sizes, speedup, '^-', color='green', linewidth=2, markersize=8)
    plt.xlabel('Tamaño de entrada')
    plt.ylabel('Factor de mejora (LDE/ABB)')
    plt.title('Factor de Mejora: ABB vs LDE')
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.axhline(y=1, color='red', linestyle='--', alpha=0.7, label='Línea base (1x)')
    plt.legend()
    
    # Time difference
    plt.subplot(2, 2, 4)
    time_diff = [lde - abb for lde, abb in zip(lde_times, abb_times)]
    plt.bar(range(len(sizes)), time_diff, color='orange', alpha=0.7)
    plt.xlabel('Índice del archivo de prueba')
    plt.ylabel('Diferencia de tiempo (ms)')
    plt.title('Diferencia: LDE - ABB')
    plt.grid(True, alpha=0.3)
    plt.xticks(range(len(sizes)), [str(s) for s in sizes], rotation=45)
    
    plt.tight_layout()
    plt.savefig('punto12_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_overall_comparison(data):
    """Generate overall comparison plot"""
    sizes = [d['size'] for d in data]
    lde_avg = [(d['lde_punto4'] + d['lde_punto8'] + d['lde_punto12']) / 3 for d in data]
    abb_avg = [(d['abb_punto4'] + d['abb_punto8'] + d['abb_punto12']) / 3 for d in data]
    
    plt.figure(figsize=(12, 8))
    
    # Main plot
    plt.subplot(2, 2, 1)
    plt.plot(sizes, lde_avg, 'o-', label='LDE (Promedio)', linewidth=2, markersize=8, color='blue')
    plt.plot(sizes, abb_avg, 's-', label='ABB (Promedio)', linewidth=2, markersize=8, color='red')
    plt.xlabel('Tamaño de entrada')
    plt.ylabel('Tiempo promedio (ms)')
    plt.title('Rendimiento Promedio General\nLDE vs ABB')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    # Linear scale plot
    plt.subplot(2, 2, 2)
    plt.plot(sizes, lde_avg, 'o-', label='LDE (Promedio)', linewidth=2, markersize=8, color='blue')
    plt.plot(sizes, abb_avg, 's-', label='ABB (Promedio)', linewidth=2, markersize=8, color='red')
    plt.xlabel('Tamaño de entrada')
    plt.ylabel('Tiempo promedio (ms)')
    plt.title('Rendimiento Promedio: Escala Lineal')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Speedup ratio
    plt.subplot(2, 2, 3)
    speedup = [lde/abb for lde, abb in zip(lde_avg, abb_avg)]
    plt.plot(sizes, speedup, '^-', color='green', linewidth=2, markersize=8)
    plt.xlabel('Tamaño de entrada')
    plt.ylabel('Factor de mejora (LDE/ABB)')
    plt.title('Factor de Mejora Promedio: ABB vs LDE')
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.axhline(y=1, color='red', linestyle='--', alpha=0.7, label='Línea base (1x)')
    plt.legend()
    
    # Time difference
    plt.subplot(2, 2, 4)
    time_diff = [lde - abb for lde, abb in zip(lde_avg, abb_avg)]
    plt.bar(range(len(sizes)), time_diff, color='orange', alpha=0.7)
    plt.xlabel('Índice del archivo de prueba')
    plt.ylabel('Diferencia de tiempo (ms)')
    plt.title('Diferencia Promedio: LDE - ABB')
    plt.grid(True, alpha=0.3)
    plt.xticks(range(len(sizes)), [str(s) for s in sizes], rotation=45)
    
    plt.tight_layout()
    plt.savefig('overall_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    try:
        data = read_benchmark_data()
        
        print("Generando gráficas individuales...")
        plot_punto4_comparison(data)
        print("✓ Gráfica Punto 4 generada: punto4_comparison.png")
        
        plot_punto8_comparison(data)
        print("✓ Gráfica Punto 8 generada: punto8_comparison.png")
        
        plot_punto12_comparison(data)
        print("✓ Gráfica Punto 12 generada: punto12_comparison.png")
        
        plot_overall_comparison(data)
        print("✓ Gráfica general generada: overall_comparison.png")
        
        print("\n¡Todas las gráficas han sido generadas exitosamente!")
        
    except FileNotFoundError:
        print("Error: No se encontró el archivo benchmark_results.csv")
        print("Ejecuta primero el script benchmark.py para generar los datos")
    except Exception as e:
        print(f"Error al generar las gráficas: {e}") 