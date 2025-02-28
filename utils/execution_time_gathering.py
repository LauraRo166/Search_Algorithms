import time
import pandas as pd
from algorithms.linearSearch import linearSearch
from algorithms.binarySearch import binarySearch
from algorithms.ternarySearch import ternarySearch
from data_generator.sorted_array_generator import get_sorted_list

def measure_execution_time(algorithm, data):
    """
    Mide el tiempo de ejecución de un algoritmo de búsqueda.

    :param algorithm: Función de búsqueda.
    :param data: Lista ordenada en la que se buscará el elemento.
    :return: Tiempo de ejecución en segundos.
    """
    target = data[len(data) // 2]  # Buscar el elemento del medio
    start_time = time.time()
    algorithm(data, target)
    return time.time() - start_time

def gather_execution_times(min_size, max_size, step, samples_per_size):
    """
    Recolecta tiempos de ejecución para listas de búsqueda de diferentes tamaños.

    :param min_size: Tamaño mínimo de la lista.
    :param max_size: Tamaño máximo de la lista.
    :param step: Tamaño del incremento.
    :param samples_per_size: Número de muestras por tamaño.
    :return: DataFrame con tiempos de ejecución.
    """
    results = []

    for size in range(min_size, max_size + 1, step):
        for _ in range(samples_per_size):
            data = get_sorted_list(size)  # Lista ordenada
            results.append({
                'Size': size,
                'Linear Search': measure_execution_time(linearSearch, data),
                'Binary Search': measure_execution_time(binarySearch, data),
                'Ternary Search': measure_execution_time(ternarySearch, data),
            })

    return pd.DataFrame(results).groupby("Size", as_index=False).mean()
