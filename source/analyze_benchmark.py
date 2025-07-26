import csv
import matplotlib.pyplot as plt

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

def plot_benchmark_results(data):
    """Generate performance comparison plots"""
    
    # Extract data for plotting
    sizes = [d['size'] for d in data]
    lde_p4 = [d['lde_punto4'] for d in data]
    abb_p4 = [d['abb_punto4'] for d in data]
    lde_p8 = [d['lde_punto8'] for d in data]
    abb_p8 = [d['abb_punto8'] for d in data]
    lde_p12 = [d['lde_punto12'] for d in data]
    abb_p12 = [d['abb_punto12'] for d in data]
    
    # Create subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Comparación de Rendimiento: LDE vs ABB', fontsize=16, fontweight='bold')
    
    # Plot 1: Punto 4
    ax1 = axes[0, 0]
    ax1.plot(sizes, lde_p4, 'o-', label='LDE', linewidth=2, markersize=6, color='blue')
    ax1.plot(sizes, abb_p4, 's-', label='ABB', linewidth=2, markersize=6, color='red')
    ax1.set_xlabel('Tamaño de entrada')
    ax1.set_ylabel('Tiempo (ms)')
    ax1.set_title('Punto 4: Ordenar encuestados por experticia')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    
    # Plot 2: Punto 8
    ax2 = axes[0, 1]
    ax2.plot(sizes, lde_p8, 'o-', label='LDE', linewidth=2, markersize=6, color='blue')
    ax2.plot(sizes, abb_p8, 's-', label='ABB', linewidth=2, markersize=6, color='red')
    ax2.set_xlabel('Tamaño de entrada')
    ax2.set_ylabel('Tiempo (ms)')
    ax2.set_title('Punto 8: Pregunta con menor mediana')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    
    # Plot 3: Punto 12
    ax3 = axes[1, 0]
    ax3.plot(sizes, lde_p12, 'o-', label='LDE', linewidth=2, markersize=6, color='blue')
    ax3.plot(sizes, abb_p12, 's-', label='ABB', linewidth=2, markersize=6, color='red')
    ax3.set_xlabel('Tamaño de entrada')
    ax3.set_ylabel('Tiempo (ms)')
    ax3.set_title('Punto 12: Pregunta con mayor consenso')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    ax3.set_xscale('log')
    ax3.set_yscale('log')
    
    # Plot 4: Promedio general
    ax4 = axes[1, 1]
    lde_avg = [(lde_p4[i] + lde_p8[i] + lde_p12[i]) / 3 for i in range(len(sizes))]
    abb_avg = [(abb_p4[i] + abb_p8[i] + abb_p12[i]) / 3 for i in range(len(sizes))]
    
    ax4.plot(sizes, lde_avg, 'o-', label='LDE (Promedio)', linewidth=2, markersize=6, color='blue')
    ax4.plot(sizes, abb_avg, 's-', label='ABB (Promedio)', linewidth=2, markersize=6, color='red')
    ax4.set_xlabel('Tamaño de entrada')
    ax4.set_ylabel('Tiempo promedio (ms)')
    ax4.set_title('Rendimiento Promedio General')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    ax4.set_xscale('log')
    ax4.set_yscale('log')
    
    plt.tight_layout()
    plt.savefig('benchmark_comparison.png', dpi=300, bbox_inches='tight')
    # plt.show()  # Comentado para evitar mostrar ventana

def print_summary_statistics(data):
    """Print summary statistics"""
    print("\n" + "="*60)
    print("RESUMEN DE RENDIMIENTO")
    print("="*60)
    
    # Calculate averages
    lde_p4_avg = sum(d['lde_punto4'] for d in data) / len(data)
    abb_p4_avg = sum(d['abb_punto4'] for d in data) / len(data)
    lde_p8_avg = sum(d['lde_punto8'] for d in data) / len(data)
    abb_p8_avg = sum(d['abb_punto8'] for d in data) / len(data)
    lde_p12_avg = sum(d['lde_punto12'] for d in data) / len(data)
    abb_p12_avg = sum(d['abb_punto12'] for d in data) / len(data)
    
    print(f"\nPunto 4 - Ordenar encuestados por experticia:")
    print(f"  LDE - Promedio: {lde_p4_avg:.3f}ms")
    print(f"  ABB - Promedio: {abb_p4_avg:.3f}ms")
    print(f"  Mejora ABB vs LDE: {(lde_p4_avg / abb_p4_avg):.2f}x más rápido")
    
    print(f"\nPunto 8 - Pregunta con menor mediana:")
    print(f"  LDE - Promedio: {lde_p8_avg:.3f}ms")
    print(f"  ABB - Promedio: {abb_p8_avg:.3f}ms")
    print(f"  Mejora ABB vs LDE: {(lde_p8_avg / abb_p8_avg):.2f}x más rápido")
    
    print(f"\nPunto 12 - Pregunta con mayor consenso:")
    print(f"  LDE - Promedio: {lde_p12_avg:.3f}ms")
    print(f"  ABB - Promedio: {abb_p12_avg:.3f}ms")
    print(f"  Mejora ABB vs LDE: {(lde_p12_avg / abb_p12_avg):.2f}x más rápido")
    
    # Overall average
    lde_overall = (lde_p4_avg + lde_p8_avg + lde_p12_avg) / 3
    abb_overall = (abb_p4_avg + abb_p8_avg + abb_p12_avg) / 3
    print(f"\nRendimiento General (Promedio de los 3 puntos):")
    print(f"  LDE - Promedio: {lde_overall:.3f}ms")
    print(f"  ABB - Promedio: {abb_overall:.3f}ms")
    print(f"  Mejora ABB vs LDE: {(lde_overall / abb_overall):.2f}x más rápido")

def create_detailed_table(data):
    """Create a detailed comparison table"""
    print("\n" + "="*100)
    print("TABLA DETALLADA DE COMPARACIÓN DE RENDIMIENTO")
    print("="*100)
    
    print(f"{'Tamaño':<8} {'Encuestados':<12} {'LDE P4':<10} {'ABB P4':<10} {'Ratio':<8} {'LDE P8':<10} {'ABB P8':<10} {'Ratio':<8} {'LDE P12':<10} {'ABB P12':<10} {'Ratio':<8}")
    print("-" * 100)
    
    for row in data:
        ratio_p4 = row['lde_punto4'] / row['abb_punto4']
        ratio_p8 = row['lde_punto8'] / row['abb_punto8']
        ratio_p12 = row['lde_punto12'] / row['abb_punto12']
        
        print(f"{row['size']:<8} {row['num_encuestados']:<12} {row['lde_punto4']:<10.3f} {row['abb_punto4']:<10.3f} {ratio_p4:<8.2f} {row['lde_punto8']:<10.3f} {row['abb_punto8']:<10.3f} {ratio_p8:<8.2f} {row['lde_punto12']:<10.3f} {row['abb_punto12']:<10.3f} {ratio_p12:<8.2f}")

if __name__ == "__main__":
    try:
        data = read_benchmark_data()
        plot_benchmark_results(data)
        print_summary_statistics(data)
        create_detailed_table(data)
        print(f"\nGráfica guardada como 'benchmark_comparison.png'")
    except FileNotFoundError:
        print("Error: No se encontró el archivo benchmark_results.csv")
        print("Ejecuta primero el script benchmark.py para generar los datos")
    except Exception as e:
        print(f"Error al generar las gráficas: {e}") 