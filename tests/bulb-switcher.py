import unittest
from math import sqrt


class TestBulbSwitch(unittest.TestCase):
    """
    Unit tests for the bulbSwitch method, which implements the floor(sqrt(n)) logic.
    """

    def setUp(self):
        self.solution = Solution()

    # ----------------------------------
    # ## Edge Cases 💡
    # ----------------------------------

    def test_n_equals_zero(self):
        """Edge case: N = 0 (No bulbs)."""
        n = 0
        self.assertEqual(self.solution.bulbSwitch(n), 0)

    def test_n_equals_one(self):
        """Edge case: N = 1 (Only one bulb, switched once)."""
        n = 1
        self.assertEqual(self.solution.bulbSwitch(n), 1)

    def test_small_non_square(self):
        """Test a small non-perfect square."""
        n = 5
        # Perfect squares <= 5 are 1 and 4. Result should be 2.
        self.assertEqual(self.solution.bulbSwitch(n), 2)

    def test_small_perfect_square(self):
        """Test a small perfect square."""
        n = 9
        # Perfect squares <= 9 are 1, 4, 9. Result should be 3.
        self.assertEqual(self.solution.bulbSwitch(n), 3)

    def test_n_just_below_perfect_square(self):
        """Test N just below a perfect square (e.g., 15)."""
        n = 15
        # Perfect squares <= 15 are 1, 4, 9. Result should be 3.
        self.assertEqual(self.solution.bulbSwitch(n), 3)

    def test_n_just_above_perfect_square(self):
        """Test N just above a perfect square (e.g., 17)."""
        n = 17
        # Perfect squares <= 17 are 1, 4, 9, 16. Result should be 4.
        self.assertEqual(self.solution.bulbSwitch(n), 4)

    # ----------------------------------
    # ## Large Input Cases 📏
    # ----------------------------------

    def test_large_perfect_square(self):
        """Test a large perfect square (e.g., 100,000,000)."""
        n = 100_000_000
        # sqrt(n) = 10,000. Result should be 10,000.
        self.assertEqual(self.solution.bulbSwitch(n), 10_000)

    def test_large_non_square(self):
        """Test a large non-perfect square."""
        n = 99_999_999
        # sqrt(n) approx 9999.99995. Result should be 9999.
        self.assertEqual(self.solution.bulbSwitch(n), 9999)

    def test_very_large_input_boundary(self):
        """Test close to the maximum typical integer limit."""
        # This is 46340^2 - 1. sqrt(n) is 46339.999...
        n = 2_147_395_600 
        self.assertEqual(self.solution.bulbSwitch(n), 46340)
        
    def test_maximum_possible_square_within_standard_int(self):
        """Test the largest square near 2^31."""
        n = 46340 * 46340 # 2147483600
        self.assertEqual(self.solution.bulbSwitch(n), 46340)

if __name__ == '__main__':
    unittest.main()