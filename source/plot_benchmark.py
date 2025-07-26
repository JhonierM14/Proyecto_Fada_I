import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_benchmark_results(csv_file='benchmark_results.csv'):
    """Generate performance comparison plots from benchmark results"""
    
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Set up the plotting style
    plt.style.use('default')
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Comparación de Rendimiento: LDE vs ABB', fontsize=16, fontweight='bold')
    
    # Plot 1: Punto 4 - Ordenar encuestados por experticia
    ax1 = axes[0, 0]
    ax1.plot(df['size'], df['lde_punto4'], 'o-', label='LDE', linewidth=2, markersize=6, color='blue')
    ax1.plot(df['size'], df['abb_punto4'], 's-', label='ABB', linewidth=2, markersize=6, color='red')
    ax1.set_xlabel('Tamaño de entrada')
    ax1.set_ylabel('Tiempo (ms)')
    ax1.set_title('Punto 4: Ordenar encuestados por experticia')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    
    # Plot 2: Punto 8 - Pregunta con menor mediana
    ax2 = axes[0, 1]
    ax2.plot(df['size'], df['lde_punto8'], 'o-', label='LDE', linewidth=2, markersize=6, color='blue')
    ax2.plot(df['size'], df['abb_punto8'], 's-', label='ABB', linewidth=2, markersize=6, color='red')
    ax2.set_xlabel('Tamaño de entrada')
    ax2.set_ylabel('Tiempo (ms)')
    ax2.set_title('Punto 8: Pregunta con menor mediana')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    
    # Plot 3: Punto 12 - Pregunta con mayor consenso
    ax3 = axes[1, 0]
    ax3.plot(df['size'], df['lde_punto12'], 'o-', label='LDE', linewidth=2, markersize=6, color='blue')
    ax3.plot(df['size'], df['abb_punto12'], 's-', label='ABB', linewidth=2, markersize=6, color='red')
    ax3.set_xlabel('Tamaño de entrada')
    ax3.set_ylabel('Tiempo (ms)')
    ax3.set_title('Punto 12: Pregunta con mayor consenso')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    ax3.set_xscale('log')
    ax3.set_yscale('log')
    
    # Plot 4: Comparación general (promedio de los tres puntos)
    ax4 = axes[1, 1]
    lde_avg = (df['lde_punto4'] + df['lde_punto8'] + df['lde_punto12']) / 3
    abb_avg = (df['abb_punto4'] + df['abb_punto8'] + df['abb_punto12']) / 3
    
    ax4.plot(df['size'], lde_avg, 'o-', label='LDE (Promedio)', linewidth=2, markersize=6, color='blue')
    ax4.plot(df['size'], abb_avg, 's-', label='ABB (Promedio)', linewidth=2, markersize=6, color='red')
    ax4.set_xlabel('Tamaño de entrada')
    ax4.set_ylabel('Tiempo promedio (ms)')
    ax4.set_title('Rendimiento Promedio General')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    ax4.set_xscale('log')
    ax4.set_yscale('log')
    
    plt.tight_layout()
    plt.savefig('benchmark_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Print summary statistics
    print("\n" + "="*60)
    print("RESUMEN DE RENDIMIENTO")
    print("="*60)
    
    print(f"\nPunto 4 - Ordenar encuestados por experticia:")
    print(f"  LDE - Promedio: {df['lde_punto4'].mean():.3f}ms, Máximo: {df['lde_punto4'].max():.3f}ms")
    print(f"  ABB - Promedio: {df['abb_punto4'].mean():.3f}ms, Máximo: {df['abb_punto4'].max():.3f}ms")
    print(f"  Mejora ABB vs LDE: {(df['lde_punto4'].mean() / df['abb_punto4'].mean()):.2f}x más rápido")
    
    print(f"\nPunto 8 - Pregunta con menor mediana:")
    print(f"  LDE - Promedio: {df['lde_punto8'].mean():.3f}ms, Máximo: {df['lde_punto8'].max():.3f}ms")
    print(f"  ABB - Promedio: {df['abb_punto8'].mean():.3f}ms, Máximo: {df['abb_punto8'].max():.3f}ms")
    print(f"  Mejora ABB vs LDE: {(df['lde_punto8'].mean() / df['abb_punto8'].mean()):.2f}x más rápido")
    
    print(f"\nPunto 12 - Pregunta con mayor consenso:")
    print(f"  LDE - Promedio: {df['lde_punto12'].mean():.3f}ms, Máximo: {df['lde_punto12'].max():.3f}ms")
    print(f"  ABB - Promedio: {df['abb_punto12'].mean():.3f}ms, Máximo: {df['abb_punto12'].max():.3f}ms")
    print(f"  Mejora ABB vs LDE: {(df['lde_punto12'].mean() / df['abb_punto12'].mean()):.2f}x más rápido")
    
    print(f"\nRendimiento General (Promedio de los 3 puntos):")
    print(f"  LDE - Promedio: {lde_avg.mean():.3f}ms")
    print(f"  ABB - Promedio: {abb_avg.mean():.3f}ms")
    print(f"  Mejora ABB vs LDE: {(lde_avg.mean() / abb_avg.mean()):.2f}x más rápido")

def create_detailed_table(csv_file='benchmark_results.csv'):
    """Create a detailed comparison table"""
    df = pd.read_csv(csv_file)
    
    print("\n" + "="*100)
    print("TABLA DETALLADA DE COMPARACIÓN DE RENDIMIENTO")
    print("="*100)
    
    print(f"{'Tamaño':<8} {'Encuestados':<12} {'LDE P4':<10} {'ABB P4':<10} {'Ratio':<8} {'LDE P8':<10} {'ABB P8':<10} {'Ratio':<8} {'LDE P12':<10} {'ABB P12':<10} {'Ratio':<8}")
    print("-" * 100)
    
    for _, row in df.iterrows():
        ratio_p4 = row['lde_punto4'] / row['abb_punto4']
        ratio_p8 = row['lde_punto8'] / row['abb_punto8']
        ratio_p12 = row['lde_punto12'] / row['abb_punto12']
        
        print(f"{row['size']:<8} {row['num_encuestados']:<12} {row['lde_punto4']:<10.3f} {row['abb_punto4']:<10.3f} {ratio_p4:<8.2f} {row['lde_punto8']:<10.3f} {row['abb_punto8']:<10.3f} {ratio_p8:<8.2f} {row['lde_punto12']:<10.3f} {row['abb_punto12']:<10.3f} {ratio_p12:<8.2f}")

if __name__ == "__main__":
    try:
        plot_benchmark_results()
        create_detailed_table()
        print(f"\nGráfica guardada como 'benchmark_comparison.png'")
    except FileNotFoundError:
        print("Error: No se encontró el archivo benchmark_results.csv")
        print("Ejecuta primero el script benchmark.py para generar los datos")
    except Exception as e:
        print(f"Error al generar las gráficas: {e}") 