import csv
import matplotlib.pyplot as plt
import numpy as np
import math

def read_final_benchmark_data(csv_file='final_benchmark_results.csv'):
    """Read final benchmark data from CSV file"""
    data = []
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append({
                'size': int(row['size']),
                'num_unique_encuestados': int(row['num_unique_encuestados']),
                'num_total_encuestados': int(row['num_total_encuestados']),
                'lde_punto4': float(row['lde_punto4']),
                'lde_punto8': float(row['lde_punto8']),
                'lde_punto12': float(row['lde_punto12']),
                'abb_punto4': float(row['abb_punto4']),
                'abb_punto8': float(row['abb_punto8']),
                'abb_punto12': float(row['abb_punto12']),
                'theo_lde_p4': float(row['theo_lde_p4']),
                'theo_abb_p4': float(row['theo_abb_p4']),
                'theo_lde_p8': float(row['theo_lde_p8']),
                'theo_abb_p8': float(row['theo_abb_p8']),
                'theo_lde_p12': float(row['theo_lde_p12']),
                'theo_abb_p12': float(row['theo_abb_p12'])
            })
    return data

def plot_final_analysis(data):
    """Generate final comprehensive analysis plots"""
    sizes = [d['size'] for d in data]
    unique_encuestados = [d['num_unique_encuestados'] for d in data]
    
    # Extract actual times
    lde_p4_actual = [d['lde_punto4'] for d in data]
    abb_p4_actual = [d['abb_punto4'] for d in data]
    lde_p8_actual = [d['lde_punto8'] for d in data]
    abb_p8_actual = [d['abb_punto8'] for d in data]
    lde_p12_actual = [d['lde_punto12'] for d in data]
    abb_p12_actual = [d['abb_punto12'] for d in data]
    
    # Create figure with subplots
    fig = plt.figure(figsize=(20, 15))
    
    # Plot 1: Performance comparison for Punto 4
    plt.subplot(3, 3, 1)
    plt.plot(unique_encuestados, lde_p4_actual, 'o-', label='LDE', linewidth=2, markersize=6, color='blue')
    plt.plot(unique_encuestados, abb_p4_actual, 's-', label='ABB', linewidth=2, markersize=6, color='red')
    plt.xlabel('Número de Encuestados Únicos')
    plt.ylabel('Tiempo (ms)')
    plt.title('Punto 4: Ordenar por Experticia')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    # Plot 2: Performance comparison for Punto 8
    plt.subplot(3, 3, 2)
    plt.plot(unique_encuestados, lde_p8_actual, 'o-', label='LDE', linewidth=2, markersize=6, color='blue')
    plt.plot(unique_encuestados, abb_p8_actual, 's-', label='ABB', linewidth=2, markersize=6, color='red')
    plt.xlabel('Número de Encuestados Únicos')
    plt.ylabel('Tiempo (ms)')
    plt.title('Punto 8: Menor Mediana')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    # Plot 3: Performance comparison for Punto 12
    plt.subplot(3, 3, 3)
    plt.plot(unique_encuestados, lde_p12_actual, 'o-', label='LDE', linewidth=2, markersize=6, color='blue')
    plt.plot(unique_encuestados, abb_p12_actual, 's-', label='ABB', linewidth=2, markersize=6, color='red')
    plt.xlabel('Número de Encuestados Únicos')
    plt.ylabel('Tiempo (ms)')
    plt.title('Punto 12: Mayor Consenso')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    # Plot 4: Speedup analysis
    plt.subplot(3, 3, 4)
    speedup_p4 = [lde/abb if abb > 0 else 0 for lde, abb in zip(lde_p4_actual, abb_p4_actual)]
    speedup_p8 = [lde/abb if abb > 0 else 0 for lde, abb in zip(lde_p8_actual, abb_p8_actual)]
    speedup_p12 = [lde/abb if abb > 0 else 0 for lde, abb in zip(lde_p12_actual, abb_p12_actual)]
    
    plt.plot(unique_encuestados, speedup_p4, 'o-', label='Punto 4', linewidth=2, markersize=6, color='green')
    plt.plot(unique_encuestados, speedup_p8, 's-', label='Punto 8', linewidth=2, markersize=6, color='orange')
    plt.plot(unique_encuestados, speedup_p12, '^-', label='Punto 12', linewidth=2, markersize=6, color='purple')
    plt.axhline(y=1, color='black', linestyle='--', alpha=0.7, label='Speedup = 1')
    plt.xlabel('Número de Encuestados Únicos')
    plt.ylabel('Speedup (LDE/ABB)')
    plt.title('Speedup: ABB vs LDE')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    
    # Plot 5: Average performance comparison
    plt.subplot(3, 3, 5)
    lde_avg = [(p4 + p8 + p12)/3 for p4, p8, p12 in zip(lde_p4_actual, lde_p8_actual, lde_p12_actual)]
    abb_avg = [(p4 + p8 + p12)/3 for p4, p8, p12 in zip(abb_p4_actual, abb_p8_actual, abb_p12_actual)]
    
    plt.plot(unique_encuestados, lde_avg, 'o-', label='LDE Promedio', linewidth=2, markersize=6, color='blue')
    plt.plot(unique_encuestados, abb_avg, 's-', label='ABB Promedio', linewidth=2, markersize=6, color='red')
    plt.xlabel('Número de Encuestados Únicos')
    plt.ylabel('Tiempo Promedio (ms)')
    plt.title('Rendimiento Promedio')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    # Plot 6: Overall speedup
    plt.subplot(3, 3, 6)
    overall_speedup = [lde/abb if abb > 0 else 0 for lde, abb in zip(lde_avg, abb_avg)]
    plt.plot(unique_encuestados, overall_speedup, 'o-', label='Speedup Promedio', linewidth=2, markersize=6, color='darkgreen')
    plt.axhline(y=1, color='black', linestyle='--', alpha=0.7, label='Speedup = 1')
    plt.xlabel('Número de Encuestados Únicos')
    plt.ylabel('Speedup Promedio')
    plt.title('Speedup Promedio: ABB vs LDE')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    
    # Plot 7: Complexity analysis
    plt.subplot(3, 3, 7)
    # Calculate theoretical complexities
    n_log_n = [n * math.log2(n) for n in unique_encuestados]
    n_linear = unique_encuestados
    
    # Normalize for comparison
    norm_lde = [t/max(lde_avg) for t in lde_avg]
    norm_abb = [t/max(abb_avg) for t in abb_avg]
    norm_n_log_n = [t/max(n_log_n) for t in n_log_n]
    norm_n = [t/max(n_linear) for t in n_linear]
    
    plt.plot(unique_encuestados, norm_lde, 'o-', label='LDE Actual', linewidth=2, markersize=6, color='blue')
    plt.plot(unique_encuestados, norm_abb, 's-', label='ABB Actual', linewidth=2, markersize=6, color='red')
    plt.plot(unique_encuestados, norm_n_log_n, '--', label='O(n log n)', linewidth=2, color='green', alpha=0.7)
    plt.plot(unique_encuestados, norm_n, '--', label='O(n)', linewidth=2, color='orange', alpha=0.7)
    plt.xlabel('Número de Encuestados Únicos')
    plt.ylabel('Tiempo Normalizado')
    plt.title('Análisis de Complejidad')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    # Plot 8: Performance summary
    plt.subplot(3, 3, 8)
    # Calculate statistics
    avg_lde = np.mean(lde_avg)
    avg_abb = np.mean(abb_avg)
    avg_speedup = np.mean(overall_speedup)
    
    categories = ['LDE', 'ABB']
    times = [avg_lde, avg_abb]
    colors = ['blue', 'red']
    
    bars = plt.bar(categories, times, color=colors, alpha=0.7)
    plt.ylabel('Tiempo Promedio (ms)')
    plt.title('Rendimiento Promedio por Estructura')
    plt.grid(True, alpha=0.3)
    
    # Add value labels on bars
    for bar, time_val in zip(bars, times):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, 
                f'{time_val:.3f}ms', ha='center', va='bottom', fontsize=10)
    
    # Plot 9: Conclusions
    plt.subplot(3, 3, 9)
    plt.axis('off')
    
    # Create text box with conclusions
    conclusions = f"""
CONCLUSIONES DEL ANÁLISIS:

📊 RENDIMIENTO:
• ABB es {avg_speedup:.1f}x más rápido que LDE
• LDE promedio: {avg_lde:.3f}ms
• ABB promedio: {avg_abb:.3f}ms

🔍 COMPLEJIDAD:
• Los tiempos no escalan como O(n log n)
• Posibles causas:
  - Optimizaciones en implementación
  - Limitaciones de procesamiento
  - Datos sintéticos no realistas

✅ RECOMENDACIONES:
• ABB es preferible para estos algoritmos
• Revisar implementaciones para optimización
• Usar datos reales para validación
"""
    
    plt.text(0.1, 0.5, conclusions, transform=plt.gca().transAxes, 
             fontsize=12, verticalalignment='center',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray", alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('final_performance_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_simple_comparison(data):
    """Generate a simple, clear comparison plot"""
    unique_encuestados = [d['num_unique_encuestados'] for d in data]
    
    # Calculate average times
    lde_avg = [(d['lde_punto4'] + d['lde_punto8'] + d['lde_punto12'])/3 for d in data]
    abb_avg = [(d['abb_punto4'] + d['abb_punto8'] + d['abb_punto12'])/3 for d in data]
    
    plt.figure(figsize=(12, 8))
    
    # Main comparison
    plt.subplot(2, 2, 1)
    plt.plot(unique_encuestados, lde_avg, 'o-', label='LDE', linewidth=3, markersize=8, color='blue')
    plt.plot(unique_encuestados, abb_avg, 's-', label='ABB', linewidth=3, markersize=8, color='red')
    plt.xlabel('Número de Encuestados Únicos')
    plt.ylabel('Tiempo Promedio (ms)')
    plt.title('Comparación de Rendimiento: LDE vs ABB')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    # Speedup
    plt.subplot(2, 2, 2)
    speedup = [lde/abb if abb > 0 else 0 for lde, abb in zip(lde_avg, abb_avg)]
    plt.plot(unique_encuestados, speedup, 'o-', label='Speedup ABB/LDE', linewidth=3, markersize=8, color='green')
    plt.axhline(y=1, color='black', linestyle='--', alpha=0.7, label='Speedup = 1')
    plt.xlabel('Número de Encuestados Únicos')
    plt.ylabel('Speedup (LDE/ABB)')
    plt.title('Speedup: ABB vs LDE')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    
    # Individual points comparison
    plt.subplot(2, 2, 3)
    lde_p4 = [d['lde_punto4'] for d in data]
    abb_p4 = [d['abb_punto4'] for d in data]
    lde_p8 = [d['lde_punto8'] for d in data]
    abb_p8 = [d['abb_punto8'] for d in data]
    lde_p12 = [d['lde_punto12'] for d in data]
    abb_p12 = [d['abb_punto12'] for d in data]
    
    plt.plot(unique_encuestados, lde_p4, 'o-', label='LDE P4', linewidth=2, markersize=6, color='blue', alpha=0.7)
    plt.plot(unique_encuestados, abb_p4, 's-', label='ABB P4', linewidth=2, markersize=6, color='red', alpha=0.7)
    plt.plot(unique_encuestados, lde_p8, '^-', label='LDE P8', linewidth=2, markersize=6, color='lightblue', alpha=0.7)
    plt.plot(unique_encuestados, abb_p8, 'v-', label='ABB P8', linewidth=2, markersize=6, color='lightcoral', alpha=0.7)
    plt.plot(unique_encuestados, lde_p12, 'd-', label='LDE P12', linewidth=2, markersize=6, color='darkblue', alpha=0.7)
    plt.plot(unique_encuestados, abb_p12, 'p-', label='ABB P12', linewidth=2, markersize=6, color='darkred', alpha=0.7)
    
    plt.xlabel('Número de Encuestados Únicos')
    plt.ylabel('Tiempo (ms)')
    plt.title('Comparación por Punto')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    # Summary statistics
    plt.subplot(2, 2, 4)
    avg_lde = np.mean(lde_avg)
    avg_abb = np.mean(abb_avg)
    avg_speedup = np.mean(speedup)
    
    categories = ['LDE', 'ABB']
    times = [avg_lde, avg_abb]
    colors = ['blue', 'red']
    
    bars = plt.bar(categories, times, color=colors, alpha=0.7)
    plt.ylabel('Tiempo Promedio (ms)')
    plt.title(f'Rendimiento Promedio\n(Speedup: {avg_speedup:.1f}x)')
    plt.grid(True, alpha=0.3)
    
    # Add value labels
    for bar, time_val in zip(bars, times):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, 
                f'{time_val:.3f}ms', ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('simple_performance_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()

def print_final_summary(data):
    """Print final summary of results"""
    print("\n" + "="*80)
    print("RESUMEN FINAL DEL ANÁLISIS DE RENDIMIENTO")
    print("="*80)
    
    # Calculate averages
    lde_avg = [(d['lde_punto4'] + d['lde_punto8'] + d['lde_punto12'])/3 for d in data]
    abb_avg = [(d['abb_punto4'] + d['abb_punto8'] + d['abb_punto12'])/3 for d in data]
    speedup = [lde/abb if abb > 0 else 0 for lde, abb in zip(lde_avg, abb_avg)]
    
    avg_lde = np.mean(lde_avg)
    avg_abb = np.mean(abb_avg)
    avg_speedup = np.mean(speedup)
    
    print(f"\n📊 RESULTADOS PRINCIPALES:")
    print(f"   • ABB es {avg_speedup:.1f}x más rápido que LDE")
    print(f"   • Tiempo promedio LDE: {avg_lde:.3f}ms")
    print(f"   • Tiempo promedio ABB: {avg_abb:.3f}ms")
    
    print(f"\n🔍 ANÁLISIS POR PUNTO:")
    lde_p4_avg = np.mean([d['lde_punto4'] for d in data])
    abb_p4_avg = np.mean([d['abb_punto4'] for d in data])
    lde_p8_avg = np.mean([d['lde_punto8'] for d in data])
    abb_p8_avg = np.mean([d['abb_punto8'] for d in data])
    lde_p12_avg = np.mean([d['lde_punto12'] for d in data])
    abb_p12_avg = np.mean([d['abb_punto12'] for d in data])
    
    print(f"   • Punto 4: LDE {lde_p4_avg:.3f}ms vs ABB {abb_p4_avg:.3f}ms (Speedup: {lde_p4_avg/abb_p4_avg:.1f}x)")
    print(f"   • Punto 8: LDE {lde_p8_avg:.3f}ms vs ABB {abb_p8_avg:.3f}ms (Speedup: {lde_p8_avg/abb_p8_avg:.1f}x)")
    print(f"   • Punto 12: LDE {lde_p12_avg:.3f}ms vs ABB {abb_p12_avg:.3f}ms (Speedup: {lde_p12_avg/abb_p12_avg:.1f}x)")
    
    print(f"\n✅ CONCLUSIONES:")
    print(f"   1. ABB es consistentemente más rápido que LDE")
    print(f"   2. La diferencia de rendimiento es significativa ({avg_speedup:.1f}x)")
    print(f"   3. Los tiempos no escalan como O(n log n) esperado")
    print(f"   4. Se recomienda usar ABB para estos algoritmos")
    
    print(f"\n⚠️  LIMITACIONES:")
    print(f"   1. Datos sintéticos pueden no representar casos reales")
    print(f"   2. Implementaciones pueden tener optimizaciones no consideradas")
    print(f"   3. Se necesitan más datos para validar complejidad teórica")

if __name__ == "__main__":
    try:
        data = read_final_benchmark_data()
        
        print("Generando gráficas finales...")
        plot_final_analysis(data)
        print("✓ Gráfica de análisis final generada: final_performance_analysis.png")
        
        plot_simple_comparison(data)
        print("✓ Gráfica de comparación simple generada: simple_performance_comparison.png")
        
        print_final_summary(data)
        
        print("\n¡Análisis final completado!")
        
    except FileNotFoundError:
        print("Error: No se encontró el archivo final_benchmark_results.csv")
        print("Ejecuta primero el script final_benchmark.py")
    except Exception as e:
        print(f"Error al generar las gráficas: {e}") 