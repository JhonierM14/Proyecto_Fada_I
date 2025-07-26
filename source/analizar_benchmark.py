import csv
import statistics

def cargar_datos():
    """Carga los datos del archivo CSV"""
    try:
        datos = []
        with open('benchmark_resultados.csv', 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                datos.append({
                    'archivo': fila['archivo'],
                    'tamaño_entrada': int(fila['tamaño_entrada']),
                    'total_preguntas': int(fila['total_preguntas']),
                    'tiempo_p4_lde_ms': float(fila['tiempo_p4_lde_ms']),
                    'tiempo_p8_lde_ms': float(fila['tiempo_p8_lde_ms']),
                    'tiempo_p12_lde_ms': float(fila['tiempo_p12_lde_ms']),
                    'tiempo_p4_abb_ms': float(fila['tiempo_p4_abb_ms']),
                    'tiempo_p8_abb_ms': float(fila['tiempo_p8_abb_ms']),
                    'tiempo_p12_abb_ms': float(fila['tiempo_p12_abb_ms'])
                })
        return datos
    except FileNotFoundError:
        print("Error: No se encontró el archivo benchmark_resultados.csv")
        return None

def calcular_estadisticas(datos):
    """Calcula estadísticas de los datos"""
    if not datos:
        return None
    
    # Extraer listas de tiempos
    p4_lde = [d['tiempo_p4_lde_ms'] for d in datos]
    p4_abb = [d['tiempo_p4_abb_ms'] for d in datos]
    p8_lde = [d['tiempo_p8_lde_ms'] for d in datos]
    p8_abb = [d['tiempo_p8_abb_ms'] for d in datos]
    p12_lde = [d['tiempo_p12_lde_ms'] for d in datos]
    p12_abb = [d['tiempo_p12_abb_ms'] for d in datos]
    
    stats = {
        'Punto 4 - LDE': {
            'Promedio': statistics.mean(p4_lde),
            'Mínimo': min(p4_lde),
            'Máximo': max(p4_lde),
            'Mediana': statistics.median(p4_lde)
        },
        'Punto 4 - ABB': {
            'Promedio': statistics.mean(p4_abb),
            'Mínimo': min(p4_abb),
            'Máximo': max(p4_abb),
            'Mediana': statistics.median(p4_abb)
        },
        'Punto 8 - LDE': {
            'Promedio': statistics.mean(p8_lde),
            'Mínimo': min(p8_lde),
            'Máximo': max(p8_lde),
            'Mediana': statistics.median(p8_lde)
        },
        'Punto 8 - ABB': {
            'Promedio': statistics.mean(p8_abb),
            'Mínimo': min(p8_abb),
            'Máximo': max(p8_abb),
            'Mediana': statistics.median(p8_abb)
        },
        'Punto 12 - LDE': {
            'Promedio': statistics.mean(p12_lde),
            'Mínimo': min(p12_lde),
            'Máximo': max(p12_lde),
            'Mediana': statistics.median(p12_lde)
        },
        'Punto 12 - ABB': {
            'Promedio': statistics.mean(p12_abb),
            'Mínimo': min(p12_abb),
            'Máximo': max(p12_abb),
            'Mediana': statistics.median(p12_abb)
        }
    }
    
    return stats

def mostrar_tabla_detallada(datos):
    """Muestra la tabla detallada de resultados"""
    print("\n" + "="*120)
    print("TABLA DETALLADA DE RESULTADOS")
    print("="*120)
    print(f"{'Archivo':<15} {'Tamaño':<8} {'P4_LDE':<10} {'P8_LDE':<10} {'P12_LDE':<10} {'P4_ABB':<10} {'P8_ABB':<10} {'P12_ABB':<10}")
    print("-"*120)
    
    for dato in datos:
        print(f"{dato['archivo']:<15} {dato['tamaño_entrada']:<8} "
              f"{dato['tiempo_p4_lde_ms']:<10.3f} {dato['tiempo_p8_lde_ms']:<10.3f} "
              f"{dato['tiempo_p12_lde_ms']:<10.3f} {dato['tiempo_p4_abb_ms']:<10.3f} "
              f"{dato['tiempo_p8_abb_ms']:<10.3f} {dato['tiempo_p12_abb_ms']:<10.3f}")

def mostrar_estadisticas(stats):
    """Muestra las estadísticas calculadas"""
    print("\n" + "="*100)
    print("ESTADÍSTICAS DE RENDIMIENTO")
    print("="*100)
    print(f"{'Métrica':<20} {'Promedio (ms)':<15} {'Mínimo (ms)':<15} {'Máximo (ms)':<15} {'Mediana (ms)':<15}")
    print("-" * 100)
    
    for metrica, valores in stats.items():
        print(f"{metrica:<20} {valores['Promedio']:<15.3f} {valores['Mínimo']:<15.3f} "
              f"{valores['Máximo']:<15.3f} {valores['Mediana']:<15.3f}")

def analizar_rendimiento(stats):
    """Analiza el rendimiento comparativo"""
    print("\n" + "="*100)
    print("ANÁLISIS DE RENDIMIENTO COMPARATIVO")
    print("="*100)
    
    # Comparar promedios
    print("Comparación de Promedios (ms):")
    print(f"  Punto 4:  LDE = {stats['Punto 4 - LDE']['Promedio']:.3f} vs ABB = {stats['Punto 4 - ABB']['Promedio']:.3f}")
    print(f"  Punto 8:  LDE = {stats['Punto 8 - LDE']['Promedio']:.3f} vs ABB = {stats['Punto 8 - ABB']['Promedio']:.3f}")
    print(f"  Punto 12: LDE = {stats['Punto 12 - LDE']['Promedio']:.3f} vs ABB = {stats['Punto 12 - ABB']['Promedio']:.3f}")
    
    # Determinar cuál es más rápido en cada punto
    print("\nEstructura más rápida por punto:")
    if stats['Punto 4 - LDE']['Promedio'] < stats['Punto 4 - ABB']['Promedio']:
        print("  Punto 4: Lista Doblemente Enlazada")
        mejora = ((stats['Punto 4 - ABB']['Promedio'] - stats['Punto 4 - LDE']['Promedio']) / stats['Punto 4 - ABB']['Promedio']) * 100
        print(f"    Mejora: {mejora:.1f}% más rápido")
    else:
        print("  Punto 4: Árbol Binario de Búsqueda")
        mejora = ((stats['Punto 4 - LDE']['Promedio'] - stats['Punto 4 - ABB']['Promedio']) / stats['Punto 4 - LDE']['Promedio']) * 100
        print(f"    Mejora: {mejora:.1f}% más rápido")
    
    if stats['Punto 8 - LDE']['Promedio'] < stats['Punto 8 - ABB']['Promedio']:
        print("  Punto 8: Lista Doblemente Enlazada")
        mejora = ((stats['Punto 8 - ABB']['Promedio'] - stats['Punto 8 - LDE']['Promedio']) / stats['Punto 8 - ABB']['Promedio']) * 100
        print(f"    Mejora: {mejora:.1f}% más rápido")
    else:
        print("  Punto 8: Árbol Binario de Búsqueda")
        mejora = ((stats['Punto 8 - LDE']['Promedio'] - stats['Punto 8 - ABB']['Promedio']) / stats['Punto 8 - LDE']['Promedio']) * 100
        print(f"    Mejora: {mejora:.1f}% más rápido")
    
    if stats['Punto 12 - LDE']['Promedio'] < stats['Punto 12 - ABB']['Promedio']:
        print("  Punto 12: Lista Doblemente Enlazada")
        mejora = ((stats['Punto 12 - ABB']['Promedio'] - stats['Punto 12 - LDE']['Promedio']) / stats['Punto 12 - ABB']['Promedio']) * 100
        print(f"    Mejora: {mejora:.1f}% más rápido")
    else:
        print("  Punto 12: Árbol Binario de Búsqueda")
        mejora = ((stats['Punto 12 - LDE']['Promedio'] - stats['Punto 12 - ABB']['Promedio']) / stats['Punto 12 - LDE']['Promedio']) * 100
        print(f"    Mejora: {mejora:.1f}% más rápido")
    
    # Análisis general
    print("\nAnálisis General:")
    tiempo_promedio_lde = (stats['Punto 4 - LDE']['Promedio'] + stats['Punto 8 - LDE']['Promedio'] + stats['Punto 12 - LDE']['Promedio']) / 3
    tiempo_promedio_abb = (stats['Punto 4 - ABB']['Promedio'] + stats['Punto 8 - ABB']['Promedio'] + stats['Punto 12 - ABB']['Promedio']) / 3
    
    print(f"  Tiempo promedio LDE: {tiempo_promedio_lde:.3f} ms")
    print(f"  Tiempo promedio ABB: {tiempo_promedio_abb:.3f} ms")
    
    if tiempo_promedio_lde < tiempo_promedio_abb:
        print("  En general: Listas Doblemente Enlazadas son más rápidas")
        mejora_total = ((tiempo_promedio_abb - tiempo_promedio_lde) / tiempo_promedio_abb) * 100
        print(f"  Mejora promedio: {mejora_total:.1f}%")
    else:
        print("  En general: Árboles Binarios de Búsqueda son más rápidos")
        mejora_total = ((tiempo_promedio_lde - tiempo_promedio_abb) / tiempo_promedio_lde) * 100
        print(f"  Mejora promedio: {mejora_total:.1f}%")

def generar_reporte_csv(datos, stats):
    """Genera un reporte CSV con el análisis"""
    with open('analisis_benchmark.csv', 'w', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        
        # Escribir datos detallados
        writer.writerow(['DETALLES POR ARCHIVO'])
        writer.writerow(['Archivo', 'Tamaño_Entrada', 'Total_Preguntas', 'P4_LDE_ms', 'P8_LDE_ms', 'P12_LDE_ms', 'P4_ABB_ms', 'P8_ABB_ms', 'P12_ABB_ms'])
        for dato in datos:
            writer.writerow([
                dato['archivo'], dato['tamaño_entrada'], dato['total_preguntas'],
                dato['tiempo_p4_lde_ms'], dato['tiempo_p8_lde_ms'], dato['tiempo_p12_lde_ms'],
                dato['tiempo_p4_abb_ms'], dato['tiempo_p8_abb_ms'], dato['tiempo_p12_abb_ms']
            ])
        
        writer.writerow([])  # Línea en blanco
        
        # Escribir estadísticas
        writer.writerow(['ESTADÍSTICAS GENERALES'])
        writer.writerow(['Métrica', 'Promedio_ms', 'Mínimo_ms', 'Máximo_ms', 'Mediana_ms'])
        for metrica, valores in stats.items():
            writer.writerow([
                metrica, f"{valores['Promedio']:.3f}", f"{valores['Mínimo']:.3f}",
                f"{valores['Máximo']:.3f}", f"{valores['Mediana']:.3f}"
            ])
    
    print(f"\nReporte detallado guardado en: analisis_benchmark.csv")

def main():
    """Función principal"""
    print("Analizando resultados del benchmark...")
    print("="*80)
    
    # Cargar datos
    datos = cargar_datos()
    if datos is None:
        return
    
    # Calcular estadísticas
    stats = calcular_estadisticas(datos)
    if stats is None:
        return
    
    # Mostrar resultados
    mostrar_tabla_detallada(datos)
    mostrar_estadisticas(stats)
    analizar_rendimiento(stats)
    
    # Generar reporte CSV
    generar_reporte_csv(datos, stats)
    
    print("\n¡Análisis completado!")

if __name__ == "__main__":
    main() 