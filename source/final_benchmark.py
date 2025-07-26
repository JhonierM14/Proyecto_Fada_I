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

def generate_unique_encuestados(size):
    """Generate unique encuestados with controlled distribution"""
    encuestados = []
    
    # Generate unique encuestados
    for i in range(size):
        experticia = random.randint(1, 10)
        opinion = random.randint(0, 10)
        nombre = f"Encuestado_{i+1}"
        encuestado = Encuestado(i+1, nombre, experticia, opinion)
        encuestados.append(encuestado)
    
    return encuestados

def create_realistic_encuesta(encuestados, num_preguntas=10):
    """Create a realistic encuesta with unique encuestados distributed across preguntas"""
    preguntas = []
    
    # Distribute encuestados across preguntas (some overlap is realistic)
    encuestados_per_pregunta = max(1, len(encuestados) // num_preguntas)
    
    for j in range(num_preguntas):
        # Select a subset of encuestados for this pregunta
        start_idx = (j * encuestados_per_pregunta) % len(encuestados)
        end_idx = min(start_idx + encuestados_per_pregunta, len(encuestados))
        
        # Add some overlap with previous pregunta for realism
        if j > 0 and random.random() < 0.3:  # 30% chance of overlap
            overlap_size = random.randint(1, encuestados_per_pregunta // 3)
            start_idx = max(0, start_idx - overlap_size)
        
        pregunta_encuestados = encuestados[start_idx:end_idx]
        
        # Ensure we have some encuestados
        if not pregunta_encuestados:
            pregunta_encuestados = encuestados[:min(5, len(encuestados))]
        
        pregunta = Pregunta(f"Pregunta_{j+1}", pregunta_encuestados)
        preguntas.append(pregunta)
    
    # Create tema
    tema = Tema("Tema 1", preguntas)
    
    # Create encuesta
    encuesta = Encuesta(1, len(preguntas), min(len(p.getIDS()) for p in preguntas), 
                       max(len(p.getIDS()) for p in preguntas), [tema])
    
    return encuesta

def benchmark_with_warmup(func, *args, num_warmup=3, num_runs=5):
    """Benchmark function with warmup runs to avoid cold start effects"""
    # Warmup runs
    for _ in range(num_warmup):
        func(*args)
    
    # Actual measurement runs
    times = []
    for _ in range(num_runs):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        times.append((end_time - start_time) * 1000)  # Convert to milliseconds
    
    # Return average time, excluding outliers
    times.sort()
    # Remove fastest and slowest runs to reduce noise
    if len(times) >= 3:
        times = times[1:-1]
    
    return sum(times) / len(times)

def benchmark_lde_functions(encuesta, num_unique_encuestados):
    """Benchmark LDE functions with proper warmup"""
    from LDE_utils import punto4_LDE, punto8_LDE, punto12_LDE
    
    # Temporarily replace global encuesta
    import data
    original_encuesta = data.encuesta
    data.encuesta = encuesta
    
    try:
        # Benchmark each function
        lde_p4_time = benchmark_with_warmup(punto4_LDE)
        lde_p8_time = benchmark_with_warmup(punto8_LDE)
        lde_p12_time = benchmark_with_warmup(punto12_LDE)
        
        return {
            'punto4': lde_p4_time,
            'punto8': lde_p8_time,
            'punto12': lde_p12_time
        }
    finally:
        # Restore original encuesta
        data.encuesta = original_encuesta

def benchmark_abb_functions(encuesta, num_unique_encuestados):
    """Benchmark ABB functions with proper warmup"""
    from abb_utils import punto4_Abb, punto8_Abb, punto12_Abb
    
    # Temporarily replace global encuesta
    import data
    original_encuesta = data.encuesta
    data.encuesta = encuesta
    
    try:
        # Benchmark each function
        abb_p4_time = benchmark_with_warmup(punto4_Abb)
        abb_p8_time = benchmark_with_warmup(punto8_Abb)
        abb_p12_time = benchmark_with_warmup(punto12_Abb)
        
        return {
            'punto4': abb_p4_time,
            'punto8': abb_p8_time,
            'punto12': abb_p12_time
        }
    finally:
        # Restore original encuesta
        data.encuesta = original_encuesta

def theoretical_complexity_improved(n, algorithm_type):
    """Calculate theoretical complexity with more realistic constants"""
    if algorithm_type == "lde_punto4":
        # LDE merge sort: O(n log n) with realistic constant
        return n * math.log2(n) * 0.0001  # More realistic constant
    elif algorithm_type == "abb_punto4":
        # ABB insertion: O(n log n) average case
        return n * math.log2(n) * 0.00005  # ABB should be faster
    elif algorithm_type in ["lde_punto8", "lde_punto12", "abb_punto8", "abb_punto12"]:
        # These involve sorting and searching: O(n log n)
        return n * math.log2(n) * 0.00001
    else:
        return 0

def run_final_benchmarks():
    """Run final benchmarks with unique encuestados"""
    # Generate sizes from 100 to 50,000 in logarithmic steps
    sizes = []
    current = 100
    while current <= 50000:
        sizes.append(current)
        current = int(current * 1.5)  # Logarithmic growth
    
    print(f"Ejecutando benchmark final con {len(sizes)} tamaños de datos...")
    print(f"Tamaños: {sizes}")
    print("Este benchmark usa encuestados únicos para un análisis más preciso.")
    print("="*60)
    
    results = []
    
    for i, size in enumerate(sizes):
        print(f"Procesando tamaño {size} ({i+1}/{len(sizes)})...")
        
        # Generate unique encuestados
        encuestados = generate_unique_encuestados(size)
        
        # Create realistic encuesta
        encuesta = create_realistic_encuesta(encuestados, num_preguntas=max(5, size//100))
        
        # Count total unique encuestados (this is the real n for complexity analysis)
        total_unique_encuestados = len(encuestados)
        
        # Count total encuestados across all preguntas (may include duplicates)
        total_encuestados_in_preguntas = 0
        for tema in encuesta._iterate_temas():
            for pregunta in tema._iterate_preguntas():
                total_encuestados_in_preguntas += len(pregunta.getIDS())
        
        print(f"  Encuestados únicos: {total_unique_encuestados}")
        print(f"  Total en preguntas: {total_encuestados_in_preguntas}")
        
        # Benchmark LDE
        print(f"  Ejecutando LDE...")
        lde_times = benchmark_lde_functions(encuesta, total_unique_encuestados)
        
        # Benchmark ABB
        print(f"  Ejecutando ABB...")
        abb_times = benchmark_abb_functions(encuesta, total_unique_encuestados)
        
        # Calculate theoretical complexities based on unique encuestados
        theo_lde_p4 = theoretical_complexity_improved(total_unique_encuestados, "lde_punto4")
        theo_abb_p4 = theoretical_complexity_improved(total_unique_encuestados, "abb_punto4")
        theo_lde_p8 = theoretical_complexity_improved(total_unique_encuestados, "lde_punto8")
        theo_abb_p8 = theoretical_complexity_improved(total_unique_encuestados, "abb_punto8")
        theo_lde_p12 = theoretical_complexity_improved(total_unique_encuestados, "lde_punto12")
        theo_abb_p12 = theoretical_complexity_improved(total_unique_encuestados, "abb_punto12")
        
        # Store results
        result = {
            'size': size,
            'num_unique_encuestados': total_unique_encuestados,
            'num_total_encuestados': total_encuestados_in_preguntas,
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
        print(f"  Completado: {size} encuestados únicos")
        print(f"  LDE P4: {lde_times['punto4']:.3f}ms, ABB P4: {abb_times['punto4']:.3f}ms")
        print()
    
    return results

def save_final_results(results, filename='final_benchmark_results.csv'):
    """Save final benchmark results to CSV"""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'size', 'num_unique_encuestados', 'num_total_encuestados',
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

def analyze_final_results(results):
    """Analyze final benchmark results"""
    print("\n" + "="*60)
    print("ANÁLISIS DE RESULTADOS FINALES")
    print("="*60)
    
    # Calculate ratios for the largest sizes
    large_results = results[-5:]
    
    print("\nANÁLISIS DE COMPLEJIDAD (últimos 5 tamaños):")
    print("-" * 50)
    
    for result in large_results:
        n = result['num_unique_encuestados']
        lde_actual = result['lde_punto4']
        abb_actual = result['abb_punto4']
        lde_theo = result['theo_lde_p4']
        abb_theo = result['theo_abb_p4']
        
        ratio_lde = lde_actual / lde_theo if lde_theo > 0 else 0
        ratio_abb = abb_actual / abb_theo if abb_theo > 0 else 0
        
        print(f"\nTamaño {result['size']} ({n} encuestados únicos):")
        print(f"  LDE P4: {lde_actual:.3f}ms (teórico: {lde_theo:.3f}ms, ratio: {ratio_lde:.3f})")
        print(f"  ABB P4: {abb_actual:.3f}ms (teórico: {abb_theo:.3f}ms, ratio: {ratio_abb:.3f})")
        
        # Check if ratios are reasonable (should be close to 1 for good fit)
        if 0.1 < ratio_lde < 10:
            print(f"    ✓ LDE muestra complejidad O(n log n) esperada")
        else:
            print(f"    ⚠ LDE puede no seguir O(n log n)")
            
        if 0.1 < ratio_abb < 10:
            print(f"    ✓ ABB muestra complejidad O(n log n) esperada")
        else:
            print(f"    ⚠ ABB puede no seguir O(n log n)")
    
    # Calculate average speedup
    speedups = []
    for result in results:
        if result['abb_punto4'] > 0:
            speedup = result['lde_punto4'] / result['abb_punto4']
            speedups.append(speedup)
    
    avg_speedup = sum(speedups) / len(speedups)
    print(f"\nSpeedup promedio ABB vs LDE: {avg_speedup:.2f}x")

if __name__ == "__main__":
    print("Iniciando benchmark final...")
    print("Este benchmark usa encuestados únicos para un análisis más preciso de la complejidad.")
    print("="*60)
    
    results = run_final_benchmarks()
    
    if results:
        save_final_results(results)
        analyze_final_results(results)
        
        print("\nBenchmark Summary:")
        print("="*60)
        for result in results:
            print(f"Size: {result['size']}, Únicos: {result['num_unique_encuestados']}, Total: {result['num_total_encuestados']}")
            print(f"  LDE - P4: {result['lde_punto4']:.2f}ms, P8: {result['lde_punto8']:.2f}ms, P12: {result['lde_punto12']:.2f}ms")
            print(f"  ABB - P4: {result['abb_punto4']:.2f}ms, P8: {result['abb_punto8']:.2f}ms, P12: {result['abb_punto12']:.2f}ms")
            print()
    else:
        print("No se generaron resultados. Verificar errores.") 