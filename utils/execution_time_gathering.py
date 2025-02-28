import time
import pandas as pd
from algorithms.linearSearch import linearSearch
from algorithms.binarySearch import binarySearch
from algorithms.ternarySearch import ternarySearch
from data_generator.sorted_array_generator import get_sorted_list

def measure_execution_time(algorithm, data):
    """
    Measures the execution time of a search algorithm.

    :param algorithm: Search function.
    :param data: Ordered list in which the element will be searched.
    :return: Execution time in seconds.
    """
    target = data[len(data) // 2]
    start_time = time.time()
    algorithm(data, target)
    return time.time() - start_time

def gather_execution_times(min_size, max_size, step, samples_per_size):
    """
    Collects execution times for search lists of different sizes.

    :param min_size: Minimum list size.
    :param max_size: Maximum list size.
    :param step: Size of the increment.
    :param samples_per_size: Number of samples per size.
    :return: DataFrame with execution times.
    """
    results = []

    for size in range(min_size, max_size + 1, step):
        for _ in range(samples_per_size):
            data = get_sorted_list(size)
            results.append({
                'Size': size,
                'Linear Search': measure_execution_time(linearSearch, data),
                'Binary Search': measure_execution_time(binarySearch, data),
                'Ternary Search': measure_execution_time(ternarySearch, data),
            })

    return pd.DataFrame(results).groupby("Size", as_index=False).mean()
