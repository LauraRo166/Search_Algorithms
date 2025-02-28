def binarySearch(array, n):
    """
   Performs a binary search for a given element in a sorted array.

   :param array: A sorted list of elements.
   :param n: The element to find.
   :return: The index of the element if found; otherwise, -1.
   """
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == n:
            return mid
        elif array[mid] < n:
            left = mid + 1
        else:
            right = mid - 1
    return -1
