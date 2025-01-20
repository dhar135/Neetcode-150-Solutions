import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):
    def test_encode(self):
        solution = Solution()
        input = ["neet", "code", "loves", "you"]
        output = solution.encode(input)
        expected = "4:neet4:code5:loves3:you"

        self.assertEqual(expected, output)

    def test_decode(self):
        solution = Solution()
        input = "4:neet4:code5:loves3:you"
        output = solution.decode(input)
        expected = ["neet", "code", "loves", "you"]

if __name__ == '__main__':
    unittest.main()
