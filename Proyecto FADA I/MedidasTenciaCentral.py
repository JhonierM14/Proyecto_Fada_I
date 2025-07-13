def promedio(valores):
    if not valores:
        return 0
    return sum(valores) / len(valores)


def mediana(valores):
    if not valores:
        return 0
    ordenados = sorted(valores)
    n = len(ordenados)
    medio = n // 2
    if n % 2 == 0:
        return (ordenados[medio - 1] + ordenados[medio]) / 2
    else:
        return ordenados[medio]


def moda(valores):
    if not valores:
        return None
    frecuencia = {}
    for v in valores:
        frecuencia[v] = frecuencia.get(v, 0) + 1

    max_frecuencia = max(frecuencia.values())
    modas = [k for k, v in frecuencia.items() if v == max_frecuencia]

    # Varias modas ...
    return max(modas)
