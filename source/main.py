from data import Texto_a_Encuesta, Resultados_a_Texto

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

Resultados_a_Texto("LDE output Test1.txt", encuesta_listas1, "listas entrelazadas")
Resultados_a_Texto("LDE output Test2.txt", encuesta_listas2, "listas entrelazadas")
Resultados_a_Texto("LDE output Test3.txt", encuesta_listas3, "listas entrelazadas")

Resultados_a_Texto("ABB output Test1.txt", encuesta_arboles1, "arboles")
Resultados_a_Texto("ABB output Test2.txt", encuesta_arboles2, "arboles")
Resultados_a_Texto("ABB output Test3.txt", encuesta_arboles3, "arboles")
