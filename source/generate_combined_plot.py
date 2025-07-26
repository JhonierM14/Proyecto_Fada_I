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

def plot_combined_analysis(data):
    """Generate a comprehensive combined plot"""
    sizes = [d['size'] for d in data]
    lde_p4 = [d['lde_punto4'] for d in data]
    abb_p4 = [d['abb_punto4'] for d in data]
    lde_p8 = [d['lde_punto8'] for d in data]
    abb_p8 = [d['abb_punto8'] for d in data]
    lde_p12 = [d['lde_punto12'] for d in data]
    abb_p12 = [d['abb_punto12'] for d in data]
    
    # Create figure with subplots
    fig = plt.figure(figsize=(20, 16))
    
    # Main comparison plots (log scale)
    plt.subplot(3, 3, 1)
    plt.plot(sizes, lde_p4, 'o-', label='LDE', linewidth=2, markersize=6, color='blue')
    plt.plot(sizes, abb_p4, 's-', label='ABB', linewidth=2, markersize=6, color='red')
    plt.xlabel('Tamaño de entrada')
    plt.ylabel('Tiempo (ms)')
    plt.title('Punto 4: Ordenar encuestados\n(Log-Log)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    plt.subplot(3, 3, 2)
    plt.plot(sizes, lde_p8, 'o-', label='LDE', linewidth=2, markersize=6, color='blue')
    plt.plot(sizes, abb_p8, 's-', label='ABB', linewidth=2, markersize=6, color='red')
    plt.xlabel('Tamaño de entrada')
    plt.ylabel('Tiempo (ms)')
    plt.title('Punto 8: Menor mediana\n(Log-Log)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    plt.subplot(3, 3, 3)
    plt.plot(sizes, lde_p12, 'o-', label='LDE', linewidth=2, markersize=6, color='blue')
    plt.plot(sizes, abb_p12, 's-', label='ABB', linewidth=2, markersize=6, color='red')
    plt.xlabel('Tamaño de entrada')
    plt.ylabel('Tiempo (ms)')
    plt.title('Punto 12: Mayor consenso\n(Log-Log)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    # Linear scale plots
    plt.subplot(3, 3, 4)
    plt.plot(sizes, lde_p4, 'o-', label='LDE', linewidth=2, markersize=6, color='blue')
    plt.plot(sizes, abb_p4, 's-', label='ABB', linewidth=2, markersize=6, color='red')
    plt.xlabel('Tamaño de entrada')
    plt.ylabel('Tiempo (ms)')
    plt.title('Punto 4: Ordenar encuestados\n(Lineal)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.subplot(3, 3, 5)
    plt.plot(sizes, lde_p8, 'o-', label='LDE', linewidth=2, markersize=6, color='blue')
    plt.plot(sizes, abb_p8, 's-', label='ABB', linewidth=2, markersize=6, color='red')
    plt.xlabel('Tamaño de entrada')
    plt.ylabel('Tiempo (ms)')
    plt.title('Punto 8: Menor mediana\n(Lineal)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.subplot(3, 3, 6)
    plt.plot(sizes, lde_p12, 'o-', label='LDE', linewidth=2, markersize=6, color='blue')
    plt.plot(sizes, abb_p12, 's-', label='ABB', linewidth=2, markersize=6, color='red')
    plt.xlabel('Tamaño de entrada')
    plt.ylabel('Tiempo (ms)')
    plt.title('Punto 12: Mayor consenso\n(Lineal)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Speedup ratios
    speedup_p4 = [lde/abb for lde, abb in zip(lde_p4, abb_p4)]
    speedup_p8 = [lde/abb for lde, abb in zip(lde_p8, abb_p8)]
    speedup_p12 = [lde/abb for lde, abb in zip(lde_p12, abb_p12)]
    
    plt.subplot(3, 3, 7)
    plt.plot(sizes, speedup_p4, '^-', color='green', linewidth=2, markersize=6)
    plt.xlabel('Tamaño de entrada')
    plt.ylabel('Factor de mejora')
    plt.title('Factor de Mejora P4\n(ABB vs LDE)')
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.axhline(y=1, color='red', linestyle='--', alpha=0.7)
    
    plt.subplot(3, 3, 8)
    plt.plot(sizes, speedup_p8, '^-', color='green', linewidth=2, markersize=6)
    plt.xlabel('Tamaño de entrada')
    plt.ylabel('Factor de mejora')
    plt.title('Factor de Mejora P8\n(ABB vs LDE)')
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.axhline(y=1, color='red', linestyle='--', alpha=0.7)
    
    plt.subplot(3, 3, 9)
    plt.plot(sizes, speedup_p12, '^-', color='green', linewidth=2, markersize=6)
    plt.xlabel('Tamaño de entrada')
    plt.ylabel('Factor de mejora')
    plt.title('Factor de Mejora P12\n(ABB vs LDE)')
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.axhline(y=1, color='red', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig('combined_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_performance_summary(data):
    """Generate a performance summary plot"""
    sizes = [d['size'] for d in data]
    lde_avg = [(d['lde_punto4'] + d['lde_punto8'] + d['lde_punto12']) / 3 for d in data]
    abb_avg = [(d['abb_punto4'] + d['abb_punto8'] + d['abb_punto12']) / 3 for d in data]
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Resumen de Rendimiento: LDE vs ABB', fontsize=16, fontweight='bold')
    
    # Overall comparison
    ax1 = axes[0, 0]
    ax1.plot(sizes, lde_avg, 'o-', label='LDE (Promedio)', linewidth=3, markersize=8, color='blue')
    ax1.plot(sizes, abb_avg, 's-', label='ABB (Promedio)', linewidth=3, markersize=8, color='red')
    ax1.set_xlabel('Tamaño de entrada')
    ax1.set_ylabel('Tiempo promedio (ms)')
    ax1.set_title('Rendimiento Promedio General')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    
    # Speedup over size
    ax2 = axes[0, 1]
    speedup = [lde/abb for lde, abb in zip(lde_avg, abb_avg)]
    ax2.plot(sizes, speedup, '^-', color='green', linewidth=3, markersize=8)
    ax2.set_xlabel('Tamaño de entrada')
    ax2.set_ylabel('Factor de mejora (LDE/ABB)')
    ax2.set_title('Factor de Mejora Promedio')
    ax2.grid(True, alpha=0.3)
    ax2.set_xscale('log')
    ax2.axhline(y=1, color='red', linestyle='--', alpha=0.7, label='Línea base (1x)')
    ax2.legend()
    
    # Bar chart comparison
    ax3 = axes[1, 0]
    x = np.arange(len(sizes))
    width = 0.35
    ax3.bar(x - width/2, lde_avg, width, label='LDE', color='blue', alpha=0.7)
    ax3.bar(x + width/2, abb_avg, width, label='ABB', color='red', alpha=0.7)
    ax3.set_xlabel('Archivo de prueba')
    ax3.set_ylabel('Tiempo promedio (ms)')
    ax3.set_title('Comparación por Archivo de Prueba')
    ax3.set_xticks(x)
    ax3.set_xticklabels([str(s) for s in sizes], rotation=45)
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Time savings
    ax4 = axes[1, 1]
    time_savings = [(lde - abb) / lde * 100 for lde, abb in zip(lde_avg, abb_avg)]
    ax4.bar(x, time_savings, color='orange', alpha=0.7)
    ax4.set_xlabel('Archivo de prueba')
    ax4.set_ylabel('Ahorro de tiempo (%)')
    ax4.set_title('Porcentaje de Ahorro de Tiempo\n(ABB vs LDE)')
    ax4.set_xticks(x)
    ax4.set_xticklabels([str(s) for s in sizes], rotation=45)
    ax4.grid(True, alpha=0.3)
    ax4.axhline(y=0, color='black', linestyle='-', alpha=0.5)
    
    plt.tight_layout()
    plt.savefig('performance_summary.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    try:
        data = read_benchmark_data()
        
        print("Generando gráficas combinadas...")
        plot_combined_analysis(data)
        print("✓ Gráfica combinada generada: combined_analysis.png")
        
        plot_performance_summary(data)
        print("✓ Resumen de rendimiento generado: performance_summary.png")
        
        print("\n¡Gráficas combinadas generadas exitosamente!")
        
    except FileNotFoundError:
        print("Error: No se encontró el archivo benchmark_results.csv")
        print("Ejecuta primero el script benchmark.py para generar los datos")
    except Exception as e:
        print(f"Error al generar las gráficas: {e}") 