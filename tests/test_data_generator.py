import unittest
from random import randint
from data_generator.sorted_array_generator import get_sorted_list

class test_data_generator(unittest.TestCase):

    def test_list_size(self):
        """Verify that the generated list has the correct size."""
        for size in [0, 1, 10, 100]:
            with self.subTest(size=size):
                lst = get_sorted_list(size)
                self.assertEqual(len(lst), size)

    def test_list_sorted(self):
        """Verify that the generated list is always sorted."""
        lst = get_sorted_list(50)
        self.assertEqual(lst, sorted(lst))

    def test_values_within_limit(self):
        """Verify that the generated values are within the given limit."""
        limit = randint(10, 1000)
        lst = get_sorted_list(20, limit)
        self.assertTrue(all(0 <= num <= limit for num in lst))

    def test_unique_values(self):
        """Verify that the list has only unique values."""
        lst = get_sorted_list(20, 100)
        self.assertEqual(len(lst), len(set(lst)))

if __name__ == "__main__":
    unittest.main()