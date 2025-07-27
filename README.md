# Proyecto_Fada_I
## El problema del procesamiento de una encuesta

Añadir el archivo de prueba con la siguiente estructura

```
Lista de participantes
• salto de línea
• salto de línea
• Pregunta 1.1
• …
• pregunta 1.n
• salto de línea
• salto de línea
• pregunta 2.1
• …
• pregunta 2.n
```
Es de vital importancia que procure que no haya ninguna linea ni salto de linea después de la última pregunta

Después de crearlo debe pegarlo en la siguiente ubicación:
```
Proyecto_FADA_I/Pruebas/
```

Para procesar su archivo txt debe ir al archivo main.py y escribir las siguientes lineas de código:
```
encuesta = Texto_a_Encuesta("Nombre_de_su_archivo.txt")

Resultados_a_Texto("Nombre_de_salida.txt", encuesta)
```

Y ejecutar main.py, los resultados los encontrará en la carpeta results