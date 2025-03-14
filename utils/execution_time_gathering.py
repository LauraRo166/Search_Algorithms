import time
import pandas as pd
import random
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

    start_time = time.time()
    algorithm(data, -1)
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
        print ("Generating " + str(size))
        times1 = []
        times2 = []
        for _ in range(samples_per_size):
            times1.append(measure_execution_time(binarySearch, get_sorted_list(size)))
            times2.append(measure_execution_time(ternarySearch, get_sorted_list(size)))
        times1.sort()
        times2.sort()
        results.append({
            'Size': size,
            'Binary Search': times1[samples_per_size//2],
            'Ternary Search': times2[samples_per_size//2],
        })

    return pd.DataFrame(results).groupby("Size", as_index=False).mean()
