#!/usr/bin/env python3
"""
Script principal para ejecutar el análisis completo de complejidad computacional
"""

import os
import sys
import subprocess
import time

def ejecutar_comando(comando, descripcion):
    """Ejecuta un comando y muestra el progreso"""
    print(f"\n{'='*60}")
    print(f"EJECUTANDO: {descripcion}")
    print(f"Comando: {comando}")
    print(f"{'='*60}")
    
    inicio = time.time()
    try:
        resultado = subprocess.run(comando, shell=True, check=True, 
                                 capture_output=True, text=True)
        tiempo = time.time() - inicio
        print(f"✅ Completado en {tiempo:.2f} segundos")
        if resultado.stdout:
            print("Salida:")
            print(resultado.stdout)
        return True
    except subprocess.CalledProcessError as e:
        tiempo = time.time() - inicio
        print(f"❌ Error después de {tiempo:.2f} segundos")
        print(f"Error: {e}")
        if e.stdout:
            print("Salida estándar:")
            print(e.stdout)
        if e.stderr:
            print("Error estándar:")
            print(e.stderr)
        return False

def verificar_dependencias():
    """Verifica que las dependencias necesarias estén instaladas"""
    print("Verificando dependencias...")
    
    dependencias = ['pandas', 'matplotlib', 'numpy']
    faltantes = []
    
    for dep in dependencias:
        try:
            __import__(dep)
            print(f"✅ {dep}")
        except ImportError:
            print(f"❌ {dep} - NO INSTALADO")
            faltantes.append(dep)
    
    if faltantes:
        print(f"\n⚠️  Dependencias faltantes: {', '.join(faltantes)}")
        print("Instalando dependencias...")
        for dep in faltantes:
            comando = f"pip install {dep}"
            if not ejecutar_comando(comando, f"Instalando {dep}"):
                print(f"❌ No se pudo instalar {dep}")
                return False
    
    return True

def main():
    """Función principal que ejecuta todo el análisis"""
    
    print("🚀 INICIANDO ANÁLISIS COMPLETO DE COMPLEJIDAD COMPUTACIONAL")
    print("=" * 60)
    
    # Verificar que estamos en el directorio correcto
    if not os.path.exists("source"):
        print("❌ Error: No se encontró el directorio 'source'")
        print("Ejecuta este script desde el directorio raíz del proyecto")
        return False
    
    # Cambiar al directorio source
    os.chdir("source")
    
    # Verificar dependencias
    if not verificar_dependencias():
        print("❌ No se pudieron instalar las dependencias necesarias")
        return False
    
    # Paso 1: Generar datos de prueba más grandes
    print("\n📊 PASO 1: Generando datos de prueba más grandes...")
    if not ejecutar_comando("python generate_test_data.py", "Generando archivos de prueba"):
        return False
    
    # Paso 2: Ejecutar pruebas de rendimiento
    print("\n⚡ PASO 2: Ejecutando pruebas de rendimiento...")
    if not ejecutar_comando("python run_performance_tests.py", "Ejecutando pruebas de rendimiento"):
        return False
    
    # Paso 3: Generar gráficas
    print("\n📈 PASO 3: Generando gráficas de análisis...")
    if not ejecutar_comando("python generate_graphs.py", "Generando gráficas"):
        return False
    
    # Verificar resultados
    print("\n🔍 VERIFICANDO RESULTADOS...")
    archivos_esperados = [
        "resultados/punto4_merge_sort.csv",
        "resultados/punto8_insertion_sort.csv", 
        "resultados/punto12_insertion_sort.csv",
        "resultados/grafica_punto4.png",
        "resultados/grafica_punto8.png",
        "resultados/grafica_punto12.png",
        "resultados/grafica_comparativa.png"
    ]
    
    todos_existen = True
    for archivo in archivos_esperados:
        if os.path.exists(archivo):
            print(f"✅ {archivo}")
        else:
            print(f"❌ {archivo} - NO ENCONTRADO")
            todos_existen = False
    
    if todos_existen:
        print("\n🎉 ¡ANÁLISIS COMPLETADO EXITOSAMENTE!")
        print("=" * 60)
        print("📁 Archivos generados en el directorio 'source/resultados/':")
        print("   • punto4_merge_sort.csv - Datos del Merge Sort")
        print("   • punto8_insertion_sort.csv - Datos del Insertion Sort (mediana)")
        print("   • punto12_insertion_sort.csv - Datos del Insertion Sort (consenso)")
        print("   • grafica_punto4.png - Gráfica Merge Sort vs O(n log n)")
        print("   • grafica_punto8.png - Gráfica Insertion Sort vs O(p²)")
        print("   • grafica_punto12.png - Gráfica Insertion Sort vs O(p²)")
        print("   • grafica_comparativa.png - Comparación de los tres algoritmos")
        print("\n📊 Los datos CSV y gráficas están listos para incluir en el informe LaTeX")
        return True
    else:
        print("\n❌ ALGUNOS ARCHIVOS NO SE GENERARON CORRECTAMENTE")
        return False

if __name__ == "__main__":
    exito = main()
    sys.exit(0 if exito else 1) 