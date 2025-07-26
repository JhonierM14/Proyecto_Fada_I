from LDE_utils import *
from abb_utils import *

"La consultoría busca que cada pregunta tenga sus en " \
"cuestados internamente ordenados descendentemente según su valor " \
"de opinión, en caso de empate se colocará primero el encuestado " \
"con mayor nivel de experticia."

"por cada tema, se busca que las preguntas estén ordenadas" \
"descendentemente según su promedio del valor de opinión. " \
"en caso de empate entre dos o más preguntas, se pondrá primero" \
"la pregunta que tiene mayor promedio de experticia, en caso de" \
"que persista el empate se pondrá primero aquella que tenga el " \
"mayor número de encuestados"

def generar_formato_encuesta():
    """
    Genera el formato requerido de "Resultados de la encuesta:" usando los datos existentes
    """
    print("Resultados de la encuesta:\n")
    
    # Recopilar todos los temas con sus promedios
    temas_con_promedio = []
    for tema in encuesta._iterate_temas():
        promedio_tema = tema.getPromedioAllPreguntas()
        temas_con_promedio.append((tema, promedio_tema))
    
    # Ordenar temas por promedio descendente usando insertion sort
    for i in range(1, len(temas_con_promedio)):
        key_item = temas_con_promedio[i]
        j = i - 1
        while j >= 0 and temas_con_promedio[j][1] < key_item[1]:  # Descendente
            temas_con_promedio[j + 1] = temas_con_promedio[j]
            j -= 1
        temas_con_promedio[j + 1] = key_item
    
    for tema, promedio_tema in temas_con_promedio:
        print(f"[{promedio_tema:.2f}] {tema.getNombre()}:")
        
        # Recopilar preguntas del tema con sus promedios
        preguntas_con_promedio = []
        pregunta_num = 1
        tema_num = int(tema.getNombre().split()[1])
        
        for pregunta in tema._iterate_preguntas():
            promedio_pregunta = pregunta.getPromedioPregunta()
            ids_encuestados = tuple(pregunta.getIDS())
            preguntas_con_promedio.append((pregunta, promedio_pregunta, ids_encuestados, f"{tema_num}.{pregunta_num}"))
            pregunta_num += 1
        
        # Ordenar preguntas por promedio descendente usando insertion sort
        for i in range(1, len(preguntas_con_promedio)):
            key_item = preguntas_con_promedio[i]
            j = i - 1
            while j >= 0 and preguntas_con_promedio[j][1] < key_item[1]:  # Descendente
                preguntas_con_promedio[j + 1] = preguntas_con_promedio[j]
                j -= 1
            preguntas_con_promedio[j + 1] = key_item
        
        for pregunta, promedio_pregunta, ids_encuestados, nombre_pregunta in preguntas_con_promedio:
            print(f" [{promedio_pregunta:.2f}] Pregunta {nombre_pregunta}: {ids_encuestados}")
        
        print()

# Generar el output en el formato exacto requerido
if __name__ == "__main__":
    # Generar formato de encuesta sin modificar punto2_LDE
    generar_formato_encuesta()
    
    # Punto 4: Mostrar lista de encuestados ordenados por experticia (USANDO ÁRBOLES)
    punto4_Abb()
    
    # Mostrar solo los resultados de puntos implementados
    print("Resultados:")
    
    # Punto 8: Pregunta con menor mediana de opinión (USANDO ÁRBOLES)
    menor_mediana = punto8_Abb()
    if menor_mediana:
        print(f"  Pregunta con menor mediana de opinion: [{int(menor_mediana['mediana_opinion'])}] Pregunta: {menor_mediana['nombre']}")
    
    # Punto 12: Pregunta con mayor consenso (USANDO ÁRBOLES)
    mayor_consenso = punto12_Abb()
    if mayor_consenso:
        print(f"  Pregunta con mayor consenso: [{mayor_consenso['consenso']:.2f}] Pregunta: {mayor_consenso['nombre']}") 