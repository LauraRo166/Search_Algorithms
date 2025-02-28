import random

def get_sorted_list(size, limit=1000):
    """
    Generates a sorted list of random integers for testing search algorithms.

    :param size: Size of the list.
    :param limit: Maximum value for random integers.
    :return: Sorted list of integers.
    """
    lst = random.sample(range(limit + 1), min(size, limit + 1))

    return sorted(lst)  # Siempre devuelve una lista ordenada

