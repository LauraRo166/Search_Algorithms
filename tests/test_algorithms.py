import unittest
from algorithms.linearSearch import linearSearch
from algorithms.binarySearch import binarySearch
from algorithms.ternarySearch import ternarySearch

class test_algorithms(unittest.TestCase):
    def setUp(self):
        """Runs before every test"""
        self.unsorted_array = [4, 2, 7, 1, 9, 3]
        self.sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_linear_search(self):
        """Tests for linear search"""
        self.assertEqual(linearSearch(self.unsorted_array, 4), 0)
        self.assertEqual(linearSearch(self.unsorted_array, 9), 4)
        self.assertEqual(linearSearch(self.unsorted_array, 3), 5)
        self.assertEqual(linearSearch(self.unsorted_array, 10), -1)
        self.assertEqual(linearSearch([], 1), -1)
        self.assertEqual(linearSearch([5], 5), 0)

    def test_binary_search(self):
        """Tests for binary search"""
        self.assertEqual(binarySearch(self.sorted_array, 1), 0)
        self.assertEqual(binarySearch(self.sorted_array, 9), 8)
        self.assertEqual(binarySearch(self.sorted_array, 5), 4)
        self.assertEqual(binarySearch(self.sorted_array, 10), -1)
        self.assertEqual(binarySearch([], 1), -1)
        self.assertEqual(binarySearch([5], 5), 0)
        self.assertEqual(binarySearch([1, 3, 5, 7], 6), -1)

    def test_ternary_search(self):
        """Tests for ternary search"""
        self.assertEqual(ternarySearch(self.sorted_array, 1), 0)
        self.assertEqual(ternarySearch(self.sorted_array, 9), 8)
        self.assertEqual(ternarySearch(self.sorted_array, 5), 4)
        self.assertEqual(ternarySearch(self.sorted_array, 10), -1)
        self.assertEqual(ternarySearch([], 1), -1)
        self.assertEqual(ternarySearch([5], 5), 0)
        self.assertEqual(ternarySearch([1, 3, 5, 7], 6), -1)

if __name__ == '__main__':
    unittest.main()
