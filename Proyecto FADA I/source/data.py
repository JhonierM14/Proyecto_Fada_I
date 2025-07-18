from source.form.encuestado import Encuestado
from source.form.pregunta import Pregunta
from source.form.tema import Tema
from source.form.encuesta import Encuesta

Persona   = Encuestado(1,  "Sofia García",         1, 6)
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
pregunta1_2 = Pregunta("Pregunta1.2", [Persona, Persona9, Persona12, Persona6])
pregunta2_1 = Pregunta("Pregunta2.1", [Persona11, Persona8, Persona7])
pregunta2_2 = Pregunta("Pregunta2.2", [Persona3, Persona4, Persona5])

tema1 = Tema("Tema 1", [pregunta1_1, pregunta1_2])
tema2 = Tema("Tema 2", [pregunta2_1, pregunta2_2])

prueba = Encuesta(2, 2, 2, 4, [tema1, tema2])
