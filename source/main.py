from data import *
from LDE_utils import *
from abb_utils import *

encuesta_listas1, encuesta_arboles1 = Texto_a_Encuesta("Test1.txt")
encuesta_listas2, encuesta_arboles2 = Texto_a_Encuesta("Test2.txt")
encuesta_listas3, encuesta_arboles3 = Texto_a_Encuesta("Test3.txt")

# Resultados_a_Texto("LDE_output_Test1.txt", encuesta_listas1, "listas_entrelazadas")
# Resultados_a_Texto("LDE_output_Test2.txt", encuesta_listas2, "listas_entrelazadas")
# Resultados_a_Texto("LDE_output_Test3.txt", encuesta_listas3, "listas_entrelazadas")

# Resultados_a_Texto("ABB_output_Test1.txt", encuesta_arboles1, "arboles")
# Resultados_a_Texto("ABB_output_Test2.txt", encuesta_arboles2, "arboles")
# Resultados_a_Texto("ABB_output_Test3.txt", encuesta_arboles3, "arboles")

def seleccionarEstructuraDeDatos(estructura: int):
    """
    - 1 <-> LDE 
    - 2 <-> Abb
    """
    if estructura==1:
        return seleccionarFuncionLDE
    elif estructura==2:
        return seleccionarFuncionAbb
    
(seleccionarEstructuraDeDatos(1))(2)(encuesta_listas1)
(seleccionarEstructuraDeDatos(2))(2)(encuesta_arboles1)

