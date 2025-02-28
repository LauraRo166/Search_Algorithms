def linearSearch(array, n):
    """
    Performs a linear search for a given element in an array.

    :param array: The list of elements to search in.
    :param n: The element to find.
    :return: The index of the element if found; otherwise, -1.
    """
    for i in range(len(array)):
        if array[i] == n:
            return i
    return -1