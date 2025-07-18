from source.LDE_utils import *
from source.abb_utils import *

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
    