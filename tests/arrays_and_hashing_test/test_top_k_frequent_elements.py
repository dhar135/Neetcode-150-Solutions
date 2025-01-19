import unittest
from src.arrays_and_hashing.top_k_frequent_elements.top_k_frequent_elements import Solution

class MyTestCase(unittest.TestCase):
    def test_example_1(self):
        nums = [1,2,2,3,3,3]
        k = 2
        expected = [2,3]
        self.assertCountEqual(expected, Solution().topKFrequent(nums, k))
    def test_array_with_one_element(self):
        nums = [1]
        k = 1
        expected = [1]
        self.assertCountEqual(expected, Solution().topKFrequent(nums, k))


if __name__ == '__main__':
    unittest.main()
