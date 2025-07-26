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

def generar_archivo_prueba_escalable(nombre_archivo, num_encuestados, num_preguntas):
    """Genera un archivo de prueba con número específico de encuestados y preguntas"""
    lines = []
    
    # Generar todos los encuestados primero
    for i in range(1, num_encuestados + 1):
        lines.append(generar_encuestado(i))
    
    # Agregar líneas en blanco
    lines.append("")
    lines.append("")
    
    # Calcular encuestados por pregunta
    encuestados_por_pregunta = num_encuestados // num_preguntas
    encuestados_restantes = num_encuestados % num_preguntas
    
    # Generar grupos de encuestados por pregunta
    inicio_id = 1
    for pregunta in range(num_preguntas):
        # Distribuir encuestados restantes entre las primeras preguntas
        encuestados_esta_pregunta = encuestados_por_pregunta
        if pregunta < encuestados_restantes:
            encuestados_esta_pregunta += 1
        
        fin_id = inicio_id + encuestados_esta_pregunta - 1
        lines.append(f"{{{', '.join(map(str, range(inicio_id, fin_id + 1)))}}}")
        inicio_id = fin_id + 1
    
    # Escribir al archivo
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    print(f"Archivo {nombre_archivo} generado:")
    print(f"  - Encuestados: {num_encuestados}")
    print(f"  - Preguntas: {num_preguntas}")
    print(f"  - Encuestados por pregunta: ~{encuestados_por_pregunta}")

def generar_conjunto_pruebas_escalable():
    """Genera un conjunto de archivos de prueba escalables para análisis de complejidad"""
    
    # Configuraciones específicas para análisis de complejidad
    configuraciones = [
        # (nombre, encuestados, preguntas)
        ("Test_50_5.txt", 50, 5),      # 50 encuestados, 5 preguntas
        ("Test_100_8.txt", 100, 8),    # 100 encuestados, 8 preguntas
        ("Test_200_12.txt", 200, 12),  # 200 encuestados, 12 preguntas
        ("Test_400_16.txt", 400, 16),  # 400 encuestados, 16 preguntas
        ("Test_800_20.txt", 800, 20),  # 800 encuestados, 20 preguntas
        ("Test_1600_25.txt", 1600, 25), # 1600 encuestados, 25 preguntas
        ("Test_3200_30.txt", 3200, 30), # 3200 encuestados, 30 preguntas
        ("Test_6400_35.txt", 6400, 35), # 6400 encuestados, 35 preguntas
        ("Test_12800_40.txt", 12800, 40), # 12800 encuestados, 40 preguntas
        ("Test_25600_45.txt", 25600, 45), # 25600 encuestados, 45 preguntas
    ]
    
    # Crear directorio de tests si no existe
    os.makedirs("tests", exist_ok=True)
    
    for nombre, encuestados, preguntas in configuraciones:
        ruta_archivo = f"tests/{nombre}"
        generar_archivo_prueba_escalable(ruta_archivo, encuestados, preguntas)

if __name__ == "__main__":
    print("Generando conjunto de archivos de prueba escalables para análisis de complejidad...")
    generar_conjunto_pruebas_escalable()
    print("\n¡Archivos de prueba escalables generados exitosamente!") 