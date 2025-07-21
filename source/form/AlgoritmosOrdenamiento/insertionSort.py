def insertion_sort(arr: list):
    """
    Recorre el arreglo elemento por elemento e inserta cada
    uno en la posición correcta respecto a los elementos 
    anteriores (como si estuvieras ordenando cartas en tu mano).
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
