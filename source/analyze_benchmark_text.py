import csv

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

def save_analysis_to_file(data, filename='benchmark_analysis.txt'):
    """Save analysis to a text file"""
    with open(filename, 'w', encoding='utf-8') as f:
        # Redirect print to file
        import sys
        original_stdout = sys.stdout
        sys.stdout = f
        
        print("ANÁLISIS DE RENDIMIENTO: LDE vs ABB")
        print("="*60)
        print(f"Fecha de análisis: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Archivos de prueba analizados: {len(data)}")
        print(f"Rango de tamaños: {min(d['size'] for d in data)} - {max(d['size'] for d in data)}")
        print(f"Total de encuestados procesados: {sum(d['num_encuestados'] for d in data)}")
        
        print_summary_statistics(data)
        create_detailed_table(data)
        
        # Restore stdout
        sys.stdout = original_stdout
    
    print(f"\nAnálisis guardado en '{filename}'")

if __name__ == "__main__":
    try:
        data = read_benchmark_data()
        print_summary_statistics(data)
        create_detailed_table(data)
        save_analysis_to_file(data)
        print(f"\nAnálisis completado exitosamente!")
    except FileNotFoundError:
        print("Error: No se encontró el archivo benchmark_results.csv")
        print("Ejecuta primero el script benchmark.py para generar los datos")
    except Exception as e:
        print(f"Error al analizar los datos: {e}") 