import time
import csv
import os
import sys
from pathlib import Path

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def load_test_data(test_file):
    """Load test data from a test file"""
    from data import Texto_a_Encuesta
    import sys
    import os
    
    # Get the global encuesta variable
    global encuesta
    
    # Load the test data using the existing function
    encuesta = Texto_a_Encuesta(test_file)
    
    # Count total encuestados
    total_encuestados = 0
    for tema in encuesta._iterate_temas():
        for pregunta in tema._iterate_preguntas():
            total_encuestados += len(pregunta.getIDS())
    
    return total_encuestados

def benchmark_lde_functions():
    """Benchmark LDE functions"""
    from LDE_utils import punto4_LDE, punto8_LDE, punto12_LDE
    
    times = {}
    
    # Measure punto4_LDE (ordenar encuestados por experticia)
    start_time = time.time()
    punto4_LDE()
    end_time = time.time()
    times['punto4'] = (end_time - start_time) * 1000  # Convert to milliseconds
    
    # Measure punto8_LDE (pregunta con menor mediana)
    start_time = time.time()
    punto8_LDE()
    end_time = time.time()
    times['punto8'] = (end_time - start_time) * 1000  # Convert to milliseconds
    
    # Measure punto12_LDE (pregunta con mayor consenso)
    start_time = time.time()
    punto12_LDE()
    end_time = time.time()
    times['punto12'] = (end_time - start_time) * 1000  # Convert to milliseconds
    
    return times

def benchmark_abb_functions():
    """Benchmark ABB functions"""
    from abb_utils import punto4_Abb, punto8_Abb, punto12_Abb
    
    times = {}
    
    # Measure punto4_Abb (ordenar encuestados por experticia)
    start_time = time.time()
    punto4_Abb()
    end_time = time.time()
    times['punto4'] = (end_time - start_time) * 1000  # Convert to milliseconds
    
    # Measure punto8_Abb (pregunta con menor mediana)
    start_time = time.time()
    punto8_Abb()
    end_time = time.time()
    times['punto8'] = (end_time - start_time) * 1000  # Convert to milliseconds
    
    # Measure punto12_Abb (pregunta con mayor consenso)
    start_time = time.time()
    punto12_Abb()
    end_time = time.time()
    times['punto12'] = (end_time - start_time) * 1000  # Convert to milliseconds
    
    return times

def run_benchmarks():
    """Run benchmarks for all test files"""
    test_files = [
        'Test_50.txt',
        'Test_64.txt', 
        'Test_100.txt',
        'Test_128.txt',
        'Test_200.txt',
        'Test_256.txt',
        'Test_400.txt',
        'Test_512.txt',
        'Test_800.txt',
        'Test_1024.txt',
        'Test_2048.txt',
        'Test_4096.txt',
        'Test_8192.txt'
    ]
    
    results = []
    
    for test_file in test_files:
        test_path = f"tests/{test_file}"
        if not os.path.exists(test_path):
            print(f"Warning: {test_path} not found, skipping...")
            continue
            
        print(f"Processing {test_file}...")
        
        # Load test data
        num_encuestados = load_test_data(test_file)
        
        # Get file size from filename
        size = int(test_file.split('_')[1].split('.')[0])
        
        # Benchmark LDE
        print("  Running LDE benchmarks...")
        lde_times = benchmark_lde_functions()
        
        # Benchmark ABB
        print("  Running ABB benchmarks...")
        abb_times = benchmark_abb_functions()
        
        # Store results
        result = {
            'size': size,
            'num_encuestados': num_encuestados,
            'lde_punto4': lde_times['punto4'],
            'lde_punto8': lde_times['punto8'],
            'lde_punto12': lde_times['punto12'],
            'abb_punto4': abb_times['punto4'],
            'abb_punto8': abb_times['punto8'],
            'abb_punto12': abb_times['punto12']
        }
        
        results.append(result)
        print(f"  Completed {test_file}")
    
    return results

def save_to_csv(results, filename='benchmark_results.csv'):
    """Save benchmark results to CSV file"""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'size', 'num_encuestados',
            'lde_punto4', 'lde_punto8', 'lde_punto12',
            'abb_punto4', 'abb_punto8', 'abb_punto12'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for result in results:
            writer.writerow(result)
    
    print(f"Results saved to {filename}")

if __name__ == "__main__":
    print("Starting benchmark tests...")
    print("This will test both LDE and ABB implementations across different data sizes.")
    print("=" * 60)
    
    results = run_benchmarks()
    
    if results:
        save_to_csv(results)
        
        print("\nBenchmark Summary:")
        print("=" * 60)
        for result in results:
            print(f"Size: {result['size']}, Encuestados: {result['num_encuestados']}")
            print(f"  LDE - P4: {result['lde_punto4']:.2f}ms, P8: {result['lde_punto8']:.2f}ms, P12: {result['lde_punto12']:.2f}ms")
            print(f"  ABB - P4: {result['abb_punto4']:.2f}ms, P8: {result['abb_punto8']:.2f}ms, P12: {result['abb_punto12']:.2f}ms")
            print()
    else:
        print("No results generated. Check if test files exist.") 