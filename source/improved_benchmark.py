import time
import csv
import random
import math
from data_structures.listadoble import *
from data_structures.abb import *
from form.encuestado import Encuestado
from form.pregunta import Pregunta
from form.tema import Tema
from form.encuesta import Encuesta
from form.AlgoritmosOrdenamiento.MedidasTenciaCentral import *

def generate_synthetic_data(size):
    """Generate synthetic data with controlled distribution"""
    encuestados = []
    
    # Generate encuestados with varied experticia and opinion
    for i in range(size):
        experticia = random.randint(1, 10)
        opinion = random.randint(0, 10)
        nombre = f"Encuestado_{i+1}"
        encuestado = Encuestado(i+1, nombre, experticia, opinion)
        encuestados.append(encuestado)
    
    # Create preguntas with different distributions
    preguntas = []
    preguntas_per_tema = max(1, size // 100)  # Scale preguntas with size
    
    for j in range(preguntas_per_tema):
        # Randomly select encuestados for this pregunta
        num_encuestados_pregunta = random.randint(max(1, size//10), size//2)
        encuestados_pregunta = random.sample(encuestados, num_encuestados_pregunta)
        
        pregunta = Pregunta(f"Pregunta_{j+1}", encuestados_pregunta)
        preguntas.append(pregunta)
    
    # Create tema
    tema = Tema("Tema 1", preguntas)
    
    # Create encuesta
    encuesta = Encuesta(1, len(preguntas), min(len(p.getIDS()) for p in preguntas), 
                       max(len(p.getIDS()) for p in preguntas), [tema])
    
    return encuesta

def benchmark_lde_functions(encuesta, num_runs=5):
    """Benchmark LDE functions with multiple runs"""
    from LDE_utils import punto4_LDE, punto8_LDE, punto12_LDE
    
    # Temporarily replace global encuesta
    import data
    original_encuesta = data.encuesta
    data.encuesta = encuesta
    
    times = {'punto4': [], 'punto8': [], 'punto12': []}
    
    for _ in range(num_runs):
        # Measure punto4_LDE
        start_time = time.time()
        punto4_LDE()
        end_time = time.time()
        times['punto4'].append((end_time - start_time) * 1000)
        
        # Measure punto8_LDE
        start_time = time.time()
        punto8_LDE()
        end_time = time.time()
        times['punto8'].append((end_time - start_time) * 1000)
        
        # Measure punto12_LDE
        start_time = time.time()
        punto12_LDE()
        end_time = time.time()
        times['punto12'].append((end_time - start_time) * 1000)
    
    # Restore original encuesta
    data.encuesta = original_encuesta
    
    # Return average times
    return {
        'punto4': sum(times['punto4']) / len(times['punto4']),
        'punto8': sum(times['punto8']) / len(times['punto8']),
        'punto12': sum(times['punto12']) / len(times['punto12'])
    }

def benchmark_abb_functions(encuesta, num_runs=5):
    """Benchmark ABB functions with multiple runs"""
    from abb_utils import punto4_Abb, punto8_Abb, punto12_Abb
    
    # Temporarily replace global encuesta
    import data
    original_encuesta = data.encuesta
    data.encuesta = encuesta
    
    times = {'punto4': [], 'punto8': [], 'punto12': []}
    
    for _ in range(num_runs):
        # Measure punto4_Abb
        start_time = time.time()
        punto4_Abb()
        end_time = time.time()
        times['punto4'].append((end_time - start_time) * 1000)
        
        # Measure punto8_Abb
        start_time = time.time()
        punto8_Abb()
        end_time = time.time()
        times['punto8'].append((end_time - start_time) * 1000)
        
        # Measure punto12_Abb
        start_time = time.time()
        punto12_Abb()
        end_time = time.time()
        times['punto12'].append((end_time - start_time) * 1000)
    
    # Restore original encuesta
    data.encuesta = original_encuesta
    
    # Return average times
    return {
        'punto4': sum(times['punto4']) / len(times['punto4']),
        'punto8': sum(times['punto8']) / len(times['punto8']),
        'punto12': sum(times['punto12']) / len(times['punto12'])
    }

def theoretical_complexity(n, algorithm_type):
    """Calculate theoretical complexity for comparison"""
    if algorithm_type == "lde_punto4":
        # LDE merge sort: O(n log n)
        return n * math.log2(n) * 0.001  # Scaled for comparison
    elif algorithm_type == "abb_punto4":
        # ABB insertion: O(n log n) average case
        return n * math.log2(n) * 0.0005  # ABB should be faster
    elif algorithm_type in ["lde_punto8", "lde_punto12", "abb_punto8", "abb_punto12"]:
        # These involve sorting and searching: O(n log n)
        return n * math.log2(n) * 0.0001
    else:
        return 0

def run_improved_benchmarks():
    """Run improved benchmarks with synthetic data"""
    # Generate sizes from 100 to 100,000 in logarithmic steps
    sizes = []
    current = 100
    while current <= 100000:
        sizes.append(current)
        current = int(current * 1.5)  # Logarithmic growth
    
    print(f"Ejecutando benchmark mejorado con {len(sizes)} tamaños de datos...")
    print(f"Tamaños: {sizes}")
    
    results = []
    
    for i, size in enumerate(sizes):
        print(f"Procesando tamaño {size} ({i+1}/{len(sizes)})...")
        
        # Generate synthetic data
        encuesta = generate_synthetic_data(size)
        
        # Count total encuestados
        total_encuestados = 0
        for tema in encuesta._iterate_temas():
            for pregunta in tema._iterate_preguntas():
                total_encuestados += len(pregunta.getIDS())
        
        # Benchmark LDE
        print(f"  Ejecutando LDE...")
        lde_times = benchmark_lde_functions(encuesta, num_runs=3)
        
        # Benchmark ABB
        print(f"  Ejecutando ABB...")
        abb_times = benchmark_abb_functions(encuesta, num_runs=3)
        
        # Calculate theoretical complexities
        theo_lde_p4 = theoretical_complexity(total_encuestados, "lde_punto4")
        theo_abb_p4 = theoretical_complexity(total_encuestados, "abb_punto4")
        theo_lde_p8 = theoretical_complexity(total_encuestados, "lde_punto8")
        theo_abb_p8 = theoretical_complexity(total_encuestados, "abb_punto8")
        theo_lde_p12 = theoretical_complexity(total_encuestados, "lde_punto12")
        theo_abb_p12 = theoretical_complexity(total_encuestados, "abb_punto12")
        
        # Store results
        result = {
            'size': size,
            'num_encuestados': total_encuestados,
            'lde_punto4': lde_times['punto4'],
            'lde_punto8': lde_times['punto8'],
            'lde_punto12': lde_times['punto12'],
            'abb_punto4': abb_times['punto4'],
            'abb_punto8': abb_times['punto8'],
            'abb_punto12': abb_times['punto12'],
            'theo_lde_p4': theo_lde_p4,
            'theo_abb_p4': theo_abb_p4,
            'theo_lde_p8': theo_lde_p8,
            'theo_abb_p8': theo_abb_p8,
            'theo_lde_p12': theo_lde_p12,
            'theo_abb_p12': theo_abb_p12
        }
        
        results.append(result)
        print(f"  Completado: {size} encuestados")
    
    return results

def save_improved_results(results, filename='improved_benchmark_results.csv'):
    """Save improved benchmark results to CSV"""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'size', 'num_encuestados',
            'lde_punto4', 'lde_punto8', 'lde_punto12',
            'abb_punto4', 'abb_punto8', 'abb_punto12',
            'theo_lde_p4', 'theo_abb_p4', 'theo_lde_p8', 'theo_abb_p8',
            'theo_lde_p12', 'theo_abb_p12'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for result in results:
            writer.writerow(result)
    
    print(f"Resultados guardados en {filename}")

def analyze_complexity(results):
    """Analyze if results match theoretical complexity"""
    print("\n" + "="*60)
    print("ANÁLISIS DE COMPLEJIDAD TEÓRICA")
    print("="*60)
    
    for result in results[-5:]:  # Analyze last 5 results (largest sizes)
        size = result['size']
        n = result['num_encuestados']
        
        print(f"\nTamaño: {size}, Encuestados: {n}")
        
        # Punto 4 analysis
        lde_actual = result['lde_punto4']
        abb_actual = result['abb_punto4']
        lde_theo = result['theo_lde_p4']
        abb_theo = result['theo_abb_p4']
        
        print(f"  Punto 4 - LDE: Actual={lde_actual:.3f}ms, Teórico={lde_theo:.3f}ms, Ratio={lde_actual/lde_theo:.2f}")
        print(f"  Punto 4 - ABB: Actual={abb_actual:.3f}ms, Teórico={abb_theo:.3f}ms, Ratio={abb_actual/abb_theo:.2f}")
        
        # Check if ratios are reasonable (should be close to 1 for good fit)
        if 0.1 < lde_actual/lde_theo < 10:
            print(f"    ✓ LDE muestra complejidad O(n log n) esperada")
        else:
            print(f"    ⚠ LDE puede no seguir O(n log n)")
            
        if 0.1 < abb_actual/abb_theo < 10:
            print(f"    ✓ ABB muestra complejidad O(n log n) esperada")
        else:
            print(f"    ⚠ ABB puede no seguir O(n log n)")

if __name__ == "__main__":
    print("Iniciando benchmark mejorado...")
    print("Este benchmark generará datos sintéticos para un análisis más preciso de la complejidad.")
    print("="*60)
    
    results = run_improved_benchmarks()
    
    if results:
        save_improved_results(results)
        analyze_complexity(results)
        
        print("\nBenchmark Summary:")
        print("="*60)
        for result in results:
            print(f"Size: {result['size']}, Encuestados: {result['num_encuestados']}")
            print(f"  LDE - P4: {result['lde_punto4']:.2f}ms, P8: {result['lde_punto8']:.2f}ms, P12: {result['lde_punto12']:.2f}ms")
            print(f"  ABB - P4: {result['abb_punto4']:.2f}ms, P8: {result['abb_punto8']:.2f}ms, P12: {result['abb_punto12']:.2f}ms")
            print()
    else:
        print("No se generaron resultados. Verificar errores.") 