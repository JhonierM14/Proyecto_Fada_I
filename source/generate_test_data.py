import random
import os

def generar_encuestado(id_encuestado):
    """Genera un encuestado con datos aleatorios"""
    nombres = [
        "Ana", "Carlos", "María", "Juan", "Laura", "Pedro", "Sofía", "Diego",
        "Carmen", "Luis", "Elena", "Miguel", "Isabel", "Roberto", "Patricia",
        "Fernando", "Lucía", "Antonio", "Mónica", "Javier", "Claudia", "Ricardo",
        "Verónica", "Alberto", "Diana", "Francisco", "Gabriela", "Manuel",
        "Adriana", "José", "Silvia", "Andrés", "Rosa", "Eduardo", "Teresa",
        "Guillermo", "Beatriz", "Raúl", "Natalia", "Héctor", "Valeria", "Oscar"
    ]
    
    nombre = random.choice(nombres) + " " + random.choice(nombres)
    experticia = random.randint(1, 10)
    opinion = random.randint(0, 10)
    
    return f"{nombre}, Experticia: {experticia}, Opinión: {opinion}"

def generar_tema(num_tema, num_preguntas, num_encuestados_por_pregunta, inicio_id):
    """Genera un tema con preguntas y encuestados"""
    tema_lines = []
    
    # Generar grupos de encuestados por pregunta
    for pregunta in range(num_preguntas):
        inicio = inicio_id + pregunta * num_encuestados_por_pregunta
        fin = inicio + num_encuestados_por_pregunta - 1
        tema_lines.append(f"{{{', '.join(map(str, range(inicio, fin + 1)))}}}")
    
    return tema_lines, inicio_id + num_preguntas * num_encuestados_por_pregunta

def generar_archivo_prueba(nombre_archivo, num_temas, num_preguntas_por_tema, num_encuestados_por_pregunta):
    """Genera un archivo de prueba completo"""
    lines = []
    
    # Calcular total de encuestados
    total_encuestados = num_temas * num_preguntas_por_tema * num_encuestados_por_pregunta
    
    # Generar todos los encuestados primero
    for i in range(1, total_encuestados + 1):
        lines.append(generar_encuestado(i))
    
    # Agregar líneas en blanco
    lines.append("")
    lines.append("")
    
    # Generar estructura de temas y preguntas
    inicio_id = 1
    for tema in range(num_temas):
        tema_lines, inicio_id = generar_tema(tema + 1, num_preguntas_por_tema, num_encuestados_por_pregunta, inicio_id)
        lines.extend(tema_lines)
        lines.append("")  # Línea en blanco entre temas
    
    # Escribir al archivo
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    total_preguntas = num_temas * num_preguntas_por_tema
    
    print(f"Archivo {nombre_archivo} generado:")
    print(f"  - Temas: {num_temas}")
    print(f"  - Preguntas por tema: {num_preguntas_por_tema}")
    print(f"  - Encuestados por pregunta: {num_encuestados_por_pregunta}")
    print(f"  - Total encuestados: {total_encuestados}")
    print(f"  - Total preguntas: {total_preguntas}")

def generar_conjunto_pruebas():
    """Genera un conjunto completo de archivos de prueba para análisis de complejidad"""
    
    # Configuraciones de prueba para diferentes tamaños
    configuraciones = [
        # (nombre, temas, preguntas_por_tema, encuestados_por_pregunta)
        ("Test_Small.txt", 2, 3, 5),      # 30 encuestados, 6 preguntas
        ("Test_Medium.txt", 3, 4, 8),     # 96 encuestados, 12 preguntas
        ("Test_Large.txt", 4, 5, 12),     # 240 encuestados, 20 preguntas
        ("Test_XLarge.txt", 5, 6, 15),    # 450 encuestados, 30 preguntas
        ("Test_XXLarge.txt", 6, 8, 20),   # 960 encuestados, 48 preguntas
        ("Test_Huge.txt", 8, 10, 25),     # 2000 encuestados, 80 preguntas
        ("Test_Massive.txt", 10, 12, 30), # 3600 encuestados, 120 preguntas
        ("Test_Giant.txt", 12, 15, 35),   # 6300 encuestados, 180 preguntas
        ("Test_Colossal.txt", 15, 18, 40), # 10800 encuestados, 270 preguntas
        ("Test_Titanic.txt", 18, 20, 45), # 16200 encuestados, 360 preguntas
    ]
    
    # Crear directorio de tests si no existe
    os.makedirs("tests", exist_ok=True)
    
    for nombre, temas, preguntas, encuestados in configuraciones:
        ruta_archivo = f"tests/{nombre}"
        generar_archivo_prueba(ruta_archivo, temas, preguntas, encuestados)

if __name__ == "__main__":
    print("Generando conjunto de archivos de prueba para análisis de complejidad...")
    generar_conjunto_pruebas()
    print("\n¡Archivos de prueba generados exitosamente!") 