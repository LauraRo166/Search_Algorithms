def ternarySearch(array, n):
    """
    Performs a ternary search for a given element in a sorted array.

    :param array: A sorted list of elements.
    :param n: The element to find.
    :return: The index of the element if found; otherwise, -1.
    """
    left, right = 0, len(array) - 1
    while left <= right:
        third1 = left + (right - left) // 3
        third2 = right - (right - left) // 3
        if array[third1] == n:
            return third1
        if array[third2] == n:
            return third2
        if n < array[third1]:
            right = third1 - 1
        elif n > array[third2]:
            left = third2 + 1
        else:
            left = third1 + 1
            right = third2 - 1
    return -1
