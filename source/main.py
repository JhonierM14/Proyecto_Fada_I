from data import Texto_a_Encuesta, Resultados_a_Texto
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

encuesta_listas1, encuesta_arboles1 = Texto_a_Encuesta("Test1.txt")
encuesta_listas2, encuesta_arboles2 = Texto_a_Encuesta("Test2.txt")
encuesta_listas3, encuesta_arboles3 = Texto_a_Encuesta("Test3.txt")
encuesta_listas4, encuesta_arboles4 = Texto_a_Encuesta("Test4.txt")

print("LISTAS---------------------------------------------------")
print("K: 2, M: 2, n: 3")
Resultados_a_Texto("LDE output Test1.txt", encuesta_listas1, "listas entrelazadas")
print("K: 3, M: 2, n: 3.5")
Resultados_a_Texto("LDE output Test2.txt", encuesta_listas2, "listas entrelazadas")
print("K: 3, M: 3, n: 4.5")
Resultados_a_Texto("LDE output Test3.txt", encuesta_listas3, "listas entrelazadas")
print("K: 3, M: 3, n: 5")
Resultados_a_Texto("LDE output Test4.txt", encuesta_listas4, "listas entrelazadas")

print("ARBOLES---------------------------------------------------")
print("K: 2, M: 2, n: 3")
Resultados_a_Texto("ABB output Test1.txt", encuesta_arboles1, "arboles")
print("K: 3, M: 2, n: 3.5")
Resultados_a_Texto("ABB output Test2.txt", encuesta_arboles2, "arboles")
print("K: 3, M: 3, n: 4.5")
Resultados_a_Texto("ABB output Test3.txt", encuesta_arboles3, "arboles")
print("K: 4, M: 4, n: 5")
Resultados_a_Texto("ABB output Test4.txt", encuesta_arboles4, "arboles")