def promedio(valores: list) -> int:
        if not valores:
            return 0
        return sum(valores) / len(valores)


def mediana(valores: list) -> float:
    if not valores:
        return 0
    # Manual sorting using insertion sort since we can't use sorted()
    ordenados = valores.copy()
    for i in range(1, len(ordenados)):
        key = ordenados[i]
        j = i - 1
        while j >= 0 and ordenados[j] > key:
            ordenados[j + 1] = ordenados[j]
            j -= 1
        ordenados[j + 1] = key
    
    n = len(ordenados)
    medio = n // 2
    if n % 2 == 0:
        # Para número par, elegir el menor de los dos centrales
        return ordenados[medio - 1]
    else:
        return ordenados[medio]


def moda(valores: list) -> int:
    if not valores:
        return None
    frecuencia = {}
    for v in valores:
        frecuencia[v] = frecuencia.get(v, 0) + 1

    max_frecuencia = max(frecuencia.values())
    modas = [k for k, v in frecuencia.items() if v == max_frecuencia]

    # En caso de empate, usar la moda con menor valor
    return min(modas)

def consenso(valores: list) -> float:
    """
    Calcula el consenso basado en la moda
    Consenso = frecuencia de la moda / total de valores (como decimal entre 0 y 1)
    """
    if not valores:
        return 0.0
    
    frecuencia = {}
    for v in valores:
        frecuencia[v] = frecuencia.get(v, 0) + 1

    max_frecuencia = max(frecuencia.values())
    
    # Consenso como decimal (0.0 a 1.0)
    consenso_decimal = max_frecuencia / len(valores)
    return consenso_decimal
