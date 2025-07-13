from Clases.encuestado import Encuestado
from Clases.pregunta import Pregunta
from Clases.tema import Tema
from Clases.encuesta import Encuesta

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

Persona  = Encuestado(1,  "Sofia García",         1, 6)
Persona2  = Encuestado(2,  "Alejandro Torres",     7, 10)
Persona3  = Encuestado(3,  "Valentina Rodriguez",  9, 0)
Persona4  = Encuestado(4,  "Juan Lopéz",          10, 1)
Persona5  = Encuestado(5,  "Martina Martinez",     7, 0)
Persona6  = Encuestado(6,  "Sebastián Pérez",      8, 9)
Persona7  = Encuestado(7,  "Camila Fernández",     2, 7)
Persona8  = Encuestado(8,  "Mateo González",       4, 7)
Persona9  = Encuestado(9,  "Isabella Díaz",        7, 5)
Persona10 = Encuestado(10, "Daniel Ruiz",          2, 9)
Persona11 = Encuestado(11, "Luciana Sánchez",      1, 7)
Persona12 = Encuestado(12, "Lucas Vásquez",        6, 8)

pregunta1_1 = Pregunta("Pregunta1.1", [Persona7, Persona8, Persona2])

#Punto 1: Ordenar encuestados de la pregunta ascendentemente segun su opinion.

#Insertion sort alreves
lista=[1,2,5,4,5]
for j in range(1, len(lista)):
     key=lista[len(lista)-j-1]
     i=len(lista)-j
     while i<len(lista) and key<lista[i]:
          lista[i-1]=lista[i]
          i=i+1
     lista[i-1]=key
     
#Se asigna a "lista" el arreglo que se quiere ordenar:
lista: list = pregunta1_1.encuestados
list_encuestados=[]
for e in lista:
    list_encuestados.append(e.getID())
print("Orden original: ", list_encuestados)

for j in range(1, len(lista)):
     key=lista[len(lista)-j-1]
     i=len(lista)-j
     while i<len(lista) and key.getOpinion()<=lista[i].getOpinion():
          if key.getOpinion()==lista[i].getOpinion():
               if key.getExperticia()>=lista[i].getExperticia():
                    #print(lista[i-1].getID())
                    #print(key.getID())
                    lista[i-1]=key
                    key=lista[i]
               else:
                    lista[i-1]=lista[i]
          else:
               lista[i-1]=lista[i]
          i=i+1
     lista[i-1]=key
     #print(lista)

#Toca hacer esto para mostrar las ids
list_encuestados=[]
for e in lista:
    list_encuestados.append(e.getID())

print("Nuevo orden: ", list_encuestados)


pregunta1_2 = Pregunta("Pregunta1.2", [Persona, Persona9, Persona12, Persona6])
pregunta2_1 = Pregunta("Pregunta2.1", [Persona11, Persona8, Persona7])
pregunta2_2 = Pregunta("Pregunta2.2", [Persona3, Persona4, Persona5])

tema1 = Tema("Tema 1", [pregunta1_1, pregunta1_2])
tema2 = Tema("Tema 2", [pregunta2_1, pregunta2_2])

prueba = Encuesta(2, 2, 2, 4, [tema1, tema2])


# ---------------------------------------------------------------

"Estructura de datos propuesta, PILA, COLA" '?'  \
" tener en cuenta que debemos poder organizar los " \
"datos, en este caso instancias de las clases, en la estructura"

# ---------------------------------------------------------------

"añadir las medidas de tencia central y los tiempos de los algoritmos"

"con los datos se deberia imprimir"

"[8.25] Tema 1:" \
    "[9.50] Pregunta 1.1: (2, 10)" \
    "[7.00] Pregunta 1.2: (6, 12, 1, 9) " \
"[3.67] Tema 2:" \
    "[7.00] Pregunta 2.2: (8, 7, 11)" \
    "[0.33] Pregunta 2.1: (4, 3, 5)" \
"Lista de encuestados:" \
"{4, 3, 6, 9, 5, 2, 12, 10, 7, 11, 1}" \

"(los valores entre corchetes son los promedios tanto de la " \
"pregunta como del tema, es necesario incluirlos" \
"en la salida final)" 