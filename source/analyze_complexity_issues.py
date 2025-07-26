import csv
import matplotlib.pyplot as plt
import numpy as np
import math

def read_improved_benchmark_data(csv_file='improved_benchmark_results.csv'):
    """Read improved benchmark data from CSV file"""
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
                'abb_punto12': float(row['abb_punto12']),
                'theo_lde_p4': float(row['theo_lde_p4']),
                'theo_abb_p4': float(row['theo_abb_p4']),
                'theo_lde_p8': float(row['theo_lde_p8']),
                'theo_abb_p8': float(row['theo_abb_p8']),
                'theo_lde_p12': float(row['theo_lde_p12']),
                'theo_abb_p12': float(row['theo_abb_p12'])
            })
    return data

def plot_complexity_analysis(data):
    """Generate comprehensive complexity analysis plots"""
    sizes = [d['size'] for d in data]
    encuestados = [d['num_encuestados'] for d in data]
    
    # Extract actual times
    lde_p4_actual = [d['lde_punto4'] for d in data]
    abb_p4_actual = [d['abb_punto4'] for d in data]
    lde_p8_actual = [d['lde_punto8'] for d in data]
    abb_p8_actual = [d['abb_punto8'] for d in data]
    lde_p12_actual = [d['lde_punto12'] for d in data]
    abb_p12_actual = [d['abb_punto12'] for d in data]
    
    # Extract theoretical times
    lde_p4_theo = [d['theo_lde_p4'] for d in data]
    abb_p4_theo = [d['theo_abb_p4'] for d in data]
    lde_p8_theo = [d['theo_lde_p8'] for d in data]
    abb_p8_theo = [d['theo_abb_p8'] for d in data]
    lde_p12_theo = [d['theo_lde_p12'] for d in data]
    abb_p12_theo = [d['theo_abb_p12'] for d in data]
    
    # Create figure with subplots
    fig = plt.figure(figsize=(20, 16))
    
    # Plot 1: Actual vs Theoretical for Punto 4
    plt.subplot(3, 3, 1)
    plt.plot(encuestados, lde_p4_actual, 'o-', label='LDE Actual', linewidth=2, markersize=6, color='blue')
    plt.plot(encuestados, abb_p4_actual, 's-', label='ABB Actual', linewidth=2, markersize=6, color='red')
    plt.plot(encuestados, lde_p4_theo, '--', label='LDE Teórico', linewidth=2, color='lightblue', alpha=0.7)
    plt.plot(encuestados, abb_p4_theo, '--', label='ABB Teórico', linewidth=2, color='lightcoral', alpha=0.7)
    plt.xlabel('Número de Encuestados')
    plt.ylabel('Tiempo (ms)')
    plt.title('Punto 4: Actual vs Teórico')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    # Plot 2: Actual vs Theoretical for Punto 8
    plt.subplot(3, 3, 2)
    plt.plot(encuestados, lde_p8_actual, 'o-', label='LDE Actual', linewidth=2, markersize=6, color='blue')
    plt.plot(encuestados, abb_p8_actual, 's-', label='ABB Actual', linewidth=2, markersize=6, color='red')
    plt.plot(encuestados, lde_p8_theo, '--', label='LDE Teórico', linewidth=2, color='lightblue', alpha=0.7)
    plt.plot(encuestados, abb_p8_theo, '--', label='ABB Teórico', linewidth=2, color='lightcoral', alpha=0.7)
    plt.xlabel('Número de Encuestados')
    plt.ylabel('Tiempo (ms)')
    plt.title('Punto 8: Actual vs Teórico')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    # Plot 3: Actual vs Theoretical for Punto 12
    plt.subplot(3, 3, 3)
    plt.plot(encuestados, lde_p12_actual, 'o-', label='LDE Actual', linewidth=2, markersize=6, color='blue')
    plt.plot(encuestados, abb_p12_actual, 's-', label='ABB Actual', linewidth=2, markersize=6, color='red')
    plt.plot(encuestados, lde_p12_theo, '--', label='LDE Teórico', linewidth=2, color='lightblue', alpha=0.7)
    plt.plot(encuestados, abb_p12_theo, '--', label='ABB Teórico', linewidth=2, color='lightcoral', alpha=0.7)
    plt.xlabel('Número de Encuestados')
    plt.ylabel('Tiempo (ms)')
    plt.title('Punto 12: Actual vs Teórico')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    # Plot 4: Ratio Actual/Teórico for Punto 4
    plt.subplot(3, 3, 4)
    ratio_lde_p4 = [actual/theo if theo > 0 else 0 for actual, theo in zip(lde_p4_actual, lde_p4_theo)]
    ratio_abb_p4 = [actual/theo if theo > 0 else 0 for actual, theo in zip(abb_p4_actual, abb_p4_theo)]
    plt.plot(encuestados, ratio_lde_p4, 'o-', label='LDE', linewidth=2, markersize=6, color='blue')
    plt.plot(encuestados, ratio_abb_p4, 's-', label='ABB', linewidth=2, markersize=6, color='red')
    plt.axhline(y=1, color='black', linestyle='--', alpha=0.7, label='Ratio = 1')
    plt.xlabel('Número de Encuestados')
    plt.ylabel('Ratio Actual/Teórico')
    plt.title('Punto 4: Ratio Actual/Teórico')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    # Plot 5: Ratio Actual/Teórico for Punto 8
    plt.subplot(3, 3, 5)
    ratio_lde_p8 = [actual/theo if theo > 0 else 0 for actual, theo in zip(lde_p8_actual, lde_p8_theo)]
    ratio_abb_p8 = [actual/theo if theo > 0 else 0 for actual, theo in zip(abb_p8_actual, abb_p8_theo)]
    plt.plot(encuestados, ratio_lde_p8, 'o-', label='LDE', linewidth=2, markersize=6, color='blue')
    plt.plot(encuestados, ratio_abb_p8, 's-', label='ABB', linewidth=2, markersize=6, color='red')
    plt.axhline(y=1, color='black', linestyle='--', alpha=0.7, label='Ratio = 1')
    plt.xlabel('Número de Encuestados')
    plt.ylabel('Ratio Actual/Teórico')
    plt.title('Punto 8: Ratio Actual/Teórico')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    # Plot 6: Ratio Actual/Teórico for Punto 12
    plt.subplot(3, 3, 6)
    ratio_lde_p12 = [actual/theo if theo > 0 else 0 for actual, theo in zip(lde_p12_actual, lde_p12_theo)]
    ratio_abb_p12 = [actual/theo if theo > 0 else 0 for actual, theo in zip(abb_p12_actual, abb_p12_theo)]
    plt.plot(encuestados, ratio_lde_p12, 'o-', label='LDE', linewidth=2, markersize=6, color='blue')
    plt.plot(encuestados, ratio_abb_p12, 's-', label='ABB', linewidth=2, markersize=6, color='red')
    plt.axhline(y=1, color='black', linestyle='--', alpha=0.7, label='Ratio = 1')
    plt.xlabel('Número de Encuestados')
    plt.ylabel('Ratio Actual/Teórico')
    plt.title('Punto 12: Ratio Actual/Teórico')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    # Plot 7: Speedup comparison (LDE/ABB)
    plt.subplot(3, 3, 7)
    speedup_p4 = [lde/abb if abb > 0 else 0 for lde, abb in zip(lde_p4_actual, abb_p4_actual)]
    speedup_p8 = [lde/abb if abb > 0 else 0 for lde, abb in zip(lde_p8_actual, abb_p8_actual)]
    speedup_p12 = [lde/abb if abb > 0 else 0 for lde, abb in zip(lde_p12_actual, abb_p12_actual)]
    plt.plot(encuestados, speedup_p4, 'o-', label='Punto 4', linewidth=2, markersize=6, color='green')
    plt.plot(encuestados, speedup_p8, 's-', label='Punto 8', linewidth=2, markersize=6, color='orange')
    plt.plot(encuestados, speedup_p12, '^-', label='Punto 12', linewidth=2, markersize=6, color='purple')
    plt.axhline(y=1, color='black', linestyle='--', alpha=0.7, label='Speedup = 1')
    plt.xlabel('Número de Encuestados')
    plt.ylabel('Speedup (LDE/ABB)')
    plt.title('Speedup: LDE vs ABB')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    
    # Plot 8: Time complexity analysis
    plt.subplot(3, 3, 8)
    # Calculate slopes for different complexity classes
    log_n = [math.log2(n) for n in encuestados]
    n_log_n = [n * math.log2(n) for n in encuestados]
    n_squared = [n**2 for n in encuestados]
    
    # Normalize actual times to compare slopes
    norm_lde_p4 = [t/max(lde_p4_actual) for t in lde_p4_actual]
    norm_abb_p4 = [t/max(abb_p4_actual) for t in abb_p4_actual]
    norm_n_log_n = [t/max(n_log_n) for t in n_log_n]
    norm_n = [t/max(encuestados) for t in encuestados]
    
    plt.plot(encuestados, norm_lde_p4, 'o-', label='LDE P4 Actual', linewidth=2, markersize=6, color='blue')
    plt.plot(encuestados, norm_abb_p4, 's-', label='ABB P4 Actual', linewidth=2, markersize=6, color='red')
    plt.plot(encuestados, norm_n_log_n, '--', label='O(n log n)', linewidth=2, color='green', alpha=0.7)
    plt.plot(encuestados, norm_n, '--', label='O(n)', linewidth=2, color='orange', alpha=0.7)
    plt.xlabel('Número de Encuestados')
    plt.ylabel('Tiempo Normalizado')
    plt.title('Análisis de Complejidad')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')
    
    # Plot 9: Summary statistics
    plt.subplot(3, 3, 9)
    # Calculate average ratios
    avg_ratio_lde = np.mean([np.mean(ratio_lde_p4), np.mean(ratio_lde_p8), np.mean(ratio_lde_p12)])
    avg_ratio_abb = np.mean([np.mean(ratio_abb_p4), np.mean(ratio_abb_p8), np.mean(ratio_abb_p12)])
    
    categories = ['LDE', 'ABB']
    ratios = [avg_ratio_lde, avg_ratio_abb]
    colors = ['blue', 'red']
    
    bars = plt.bar(categories, ratios, color=colors, alpha=0.7)
    plt.ylabel('Ratio Promedio Actual/Teórico')
    plt.title('Ratio Promedio por Estructura')
    plt.grid(True, alpha=0.3)
    
    # Add value labels on bars
    for bar, ratio in zip(bars, ratios):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.0001, 
                f'{ratio:.6f}', ha='center', va='bottom', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('complexity_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()

def print_complexity_analysis(data):
    """Print detailed complexity analysis"""
    print("\n" + "="*80)
    print("ANÁLISIS DETALLADO DE COMPLEJIDAD")
    print("="*80)
    
    print("\nPROBLEMAS IDENTIFICADOS:")
    print("-" * 40)
    
    # Calculate average ratios
    ratios_lde_p4 = [d['lde_punto4']/d['theo_lde_p4'] if d['theo_lde_p4'] > 0 else 0 for d in data]
    ratios_abb_p4 = [d['abb_punto4']/d['theo_abb_p4'] if d['theo_abb_p4'] > 0 else 0 for d in data]
    
    avg_ratio_lde = np.mean(ratios_lde_p4)
    avg_ratio_abb = np.mean(ratios_abb_p4)
    
    print(f"1. Ratio promedio LDE Actual/Teórico: {avg_ratio_lde:.8f}")
    print(f"2. Ratio promedio ABB Actual/Teórico: {avg_ratio_abb:.8f}")
    print(f"3. Los tiempos reales son {1/avg_ratio_lde:.0f}x más pequeños que los teóricos")
    
    print("\nPOSIBLES CAUSAS:")
    print("-" * 40)
    print("1. Las implementaciones no procesan todos los encuestados")
    print("2. Hay optimizaciones no consideradas en el análisis teórico")
    print("3. Los algoritmos usan estructuras de datos más eficientes")
    print("4. La medición de tiempo no incluye todo el procesamiento")
    print("5. Los datos sintéticos no representan casos reales")
    
    print("\nRECOMENDACIONES:")
    print("-" * 40)
    print("1. Revisar las implementaciones de punto4_LDE y punto4_Abb")
    print("2. Verificar que se procesen todos los encuestados")
    print("3. Analizar la complejidad real de los algoritmos implementados")
    print("4. Usar datos de prueba más realistas")
    print("5. Implementar mediciones más precisas")
    
    print("\nANÁLISIS POR TAMAÑO:")
    print("-" * 40)
    for i, d in enumerate(data[-5:]):  # Last 5 results
        print(f"\nTamaño {d['size']} ({d['num_encuestados']} encuestados):")
        print(f"  LDE P4: {d['lde_punto4']:.3f}ms (teórico: {d['theo_lde_p4']:.1f}ms)")
        print(f"  ABB P4: {d['abb_punto4']:.3f}ms (teórico: {d['theo_abb_p4']:.1f}ms)")
        print(f"  Ratio LDE: {d['lde_punto4']/d['theo_lde_p4']:.8f}")
        print(f"  Ratio ABB: {d['abb_punto4']/d['theo_abb_p4']:.8f}")

def save_analysis_report(data, filename='complexity_analysis_report.txt'):
    """Save analysis report to text file"""
    with open(filename, 'w', encoding='utf-8') as f:
        import sys
        original_stdout = sys.stdout
        sys.stdout = f
        
        print("REPORTE DE ANÁLISIS DE COMPLEJIDAD")
        print("="*60)
        print(f"Fecha: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Archivo de datos: improved_benchmark_results.csv")
        print(f"Número de muestras: {len(data)}")
        
        print_complexity_analysis(data)
        
        print("\nDATOS COMPLETOS:")
        print("-" * 60)
        print(f"{'Size':<8} {'Encuestados':<12} {'LDE P4':<10} {'ABB P4':<10} {'Ratio LDE':<12} {'Ratio ABB':<12}")
        print("-" * 60)
        
        for d in data:
            ratio_lde = d['lde_punto4']/d['theo_lde_p4'] if d['theo_lde_p4'] > 0 else 0
            ratio_abb = d['abb_punto4']/d['theo_abb_p4'] if d['theo_abb_p4'] > 0 else 0
            print(f"{d['size']:<8} {d['num_encuestados']:<12} {d['lde_punto4']:<10.3f} {d['abb_punto4']:<10.3f} {ratio_lde:<12.8f} {ratio_abb:<12.8f}")
        
        sys.stdout = original_stdout
    
    print(f"\nReporte guardado en '{filename}'")

if __name__ == "__main__":
    try:
        data = read_improved_benchmark_data()
        
        print("Analizando problemas de complejidad...")
        plot_complexity_analysis(data)
        print("✓ Gráfica de análisis de complejidad generada: complexity_analysis.png")
        
        print_complexity_analysis(data)
        save_analysis_report(data)
        
        print("\n¡Análisis completado!")
        
    except FileNotFoundError:
        print("Error: No se encontró el archivo improved_benchmark_results.csv")
        print("Ejecuta primero el script improved_benchmark.py")
    except Exception as e:
        print(f"Error al analizar los datos: {e}") 