import unittest
from typing import List

class TestGenerateMatrix(unittest.TestCase):
    """
    Unit tests for the generateMatrix method.
    """

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    # ----------------------------------
    # ## Standard Cases
    # ----------------------------------

    def test_n_equals_3(self):
        """Standard case: N=3 (Odd size)"""
        n = 3
        expected = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        self.assertEqual(self.solution.generateMatrix(n), expected)

    def test_n_equals_4(self):
        """Standard case: N=4 (Even size)"""
        n = 4
        expected = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
        self.assertEqual(self.solution.generateMatrix(n), expected)

    def test_n_equals_5(self):
        """Standard case: N=5 (Odd size, multiple layers)"""
        n = 5
        expected = [
            [1, 2, 3, 4, 5],
            [16, 17, 18, 19, 6],
            [15, 24, 25, 20, 7],
            [14, 23, 22, 21, 8],
            [13, 12, 11, 10, 9],
        ]
        self.assertEqual(self.solution.generateMatrix(n), expected)

    # ----------------------------------
    # ## Edge Cases
    # ----------------------------------

    def test_n_equals_1(self):
        """Edge case: Minimum size N=1."""
        n = 1
        expected = [[1]]
        self.assertEqual(self.solution.generateMatrix(n), expected)

    def test_n_equals_0_invalid_input(self):
        """Edge case: N=0 (Should typically not occur based on constraints, but useful for robustness)."""
        # Based on Python list comprehension, it returns an empty list of lists
        n = 0
        expected = []
        self.assertEqual(self.solution.generateMatrix(n), expected)

    def test_n_equals_2(self):
        """Edge case: Smallest even size N=2."""
        n = 2
        expected = [[1, 2], [4, 3]]
        self.assertEqual(self.solution.generateMatrix(n), expected)

    # ----------------------------------
    # ## Large Input Cases
    # ----------------------------------

    def test_large_input_n_equals_10(self):
        """Large even input (N=10). We verify boundaries and center values."""
        n = 10
        result = self.solution.generateMatrix(n)

        # Check size
        self.assertEqual(len(result), n)
        self.assertEqual(len(result[0]), n)

        # Check total range (1 to N^2)
        expected_set = set(range(1, n * n + 1))
        actual_set = set(val for row in result for val in row)
        self.assertEqual(actual_set, expected_set)

        # Check specific boundaries (top row, right column, bottom row, left column)
        self.assertEqual(result[0][0], 1)
        self.assertEqual(result[0][n - 1], n)
        self.assertEqual(result[n - 1][n - 1], 2 * n - 1)
        self.assertEqual(result[n - 1][0], 3 * n - 2)

        # Check the center value of the first layer (n^2)
        self.assertEqual(
            result[n // 2][n // 2 - 1], n * n
        )  # The last value filled in layer 1

    def test_large_input_n_equals_11(self):
        """Large odd input (N=11). We verify boundaries and the absolute center value."""
        n = 11
        result = self.solution.generateMatrix(n)

        # Check size and range (1 to N^2)
        expected_set = set(range(1, n * n + 1))
        actual_set = set(val for row in result for val in row)
        self.assertEqual(actual_set, expected_set)

        # Check the absolute center value (which should be N^2)
        center_index = n // 2  # 5
        self.assertEqual(result[center_index][center_index], n * n)  # 121

        # Check surrounding values of the center
        # Center is (5, 5) = 121
        # (5, 4) should be 120 (Direction 3, moving left)
        self.assertEqual(result[center_index][center_index - 1], n * n - 1)  # 120
        # (4, 4) should be 119 (Direction 4, moving up)
        self.assertEqual(result[center_index - 1][center_index - 1], 113)
        # (4, 5) should be 118 (Direction 1, moving right)
        self.assertEqual(result[center_index - 1][center_index], 114)  # 118


if __name__ == "__main__":
    unittest.main()
