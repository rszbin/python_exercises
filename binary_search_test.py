import unittest
from binary_search_2 import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(binary_search([], 5), None)

    def test_single_element_found(self):
        self.assertEqual(binary_search([7], 7), 0)

    def test_single_element_not_found(self):
        self.assertEqual(binary_search([7], 3), None)

    def test_target_at_beginning(self):
        arr = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(arr, 1), 0)

    def test_target_in_middle(self):
        arr = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(arr, 5), 2)

    # why does this test fail?
    # why is 3 + 4 // 2 == 5?
    def test_target_at_end(self):
        arr = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(arr, 9), 4)

    def test_target_not_present(self):
        arr = [2, 4, 6, 8, 10]
        self.assertEqual(binary_search(arr, 5), None)

    def test_with_duplicates(self):
        arr = [1, 2, 2, 2, 3]
        idx = binary_search(arr, 2)
        self.assertIn(idx, [1, 2, 3])  # any of the duplicate positions is valid

    def test_negative_numbers(self):
        arr = [-10, -5, 0, 5, 10]
        self.assertEqual(binary_search(arr, -5), 1)
        self.assertEqual(binary_search(arr, 10), 4)
        self.assertEqual(binary_search(arr, -7), None)

if __name__ == '__main__':
    unittest.main()