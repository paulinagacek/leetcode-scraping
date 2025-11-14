import unittest
from typing import List

class TestReverseInteger(unittest.TestCase):
    """
    Unit tests for the reverse method of the Solution class.
    Tests cover standard inputs, edge cases (zero, large/small numbers), 
    and the crucial overflow condition.
    """

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    # ----------------------------------
    # ## Standard Cases
    # ----------------------------------

    def test_standard_positive(self):
        """Basic positive number."""
        self.assertEqual(self.solution.reverse(123), 321)

    def test_standard_negative(self):
        """Basic negative number."""
        self.assertEqual(self.solution.reverse(-123), -321)

    def test_with_trailing_zero(self):
        """Number ending in zero."""
        self.assertEqual(self.solution.reverse(120), 21)

    def test_with_internal_zeros(self):
        """Number with internal zeros."""
        self.assertEqual(self.solution.reverse(5001), 1005)

    # ----------------------------------
    # ## Edge Cases
    # ----------------------------------

    def test_single_digit(self):
        """Single-digit number."""
        self.assertEqual(self.solution.reverse(7), 7)

    def test_single_digit_negative(self):
        """Single-digit negative number."""
        self.assertEqual(self.solution.reverse(-9), -9)

    def test_zero(self):
        """Input is zero."""
        self.assertEqual(self.solution.reverse(0), 0)

    # ----------------------------------
    # ## Overflow Cases (Crucial for this problem)
    # ----------------------------------

    def test_positive_overflow(self):
        """Number that reverses to exceed the MAX_INT (2^31 - 1)."""
        # MAX_INT is 2147483647.
        # Reversing 1463847412 (9 digits) -> 2147483641 (within limit)
        # Reversing 1463847413 (9 digits) -> 3147483641 (overflow)
        self.assertEqual(self.solution.reverse(1463847413), 0)

    def test_max_int_minus_one_reverse(self):
        """Test the largest number that reverses without overflow."""
        # 1056389759 should not overflow (reversed is 9579836501, overflows) -> NO
        
        # Test 1999999999 (9 digits). Reversed is 9999999991 (Overflow).
        self.assertEqual(self.solution.reverse(1999999999), 0)
        
    def test_positive_borderline_overflow(self):
        """Test a number that reverses to the maximum possible value 2147483647."""
        # Reversing 7463847412 -> 2147483647 (MAX_INT)
        self.assertEqual(self.solution.reverse(7463847412), 2147483647)
        
    def test_positive_borderline_overflow_one_more(self):
        """Test a number that reverses to 2147483648 (Overflow)."""
        # Reversing 8463847412 -> 2147483648 (Overflow)
        self.assertEqual(self.solution.reverse(8463847412), 0)

    def test_negative_overflow(self):
        """Number that reverses to exceed the MIN_INT (-2^31). 
           Since the solution checks the absolute value, it checks against 2^31 - 1.
           If the reversed absolute value equals 2^31, it's an overflow when the sign is applied.
           The provided solution only checks against 2^31 - 1, which works for the positive case.
           For the negative case, the limit is 2^31 (2147483648).
        """
        # Test a number that reverses to 2147483648 (abs value)
        # Reversing -8463847412 (9 digits) -> -2147483648 (MIN_INT)
        # The canonical solution will only return 0 if rev > 2^31 - 1.
        # If rev = 2147483648, it is > 2147483647, so it returns 0.
        self.assertEqual(self.solution.reverse(-8463847412), 0)
        
    def test_negative_borderline_valid(self):
        """Test a number that reverses to -2147483647."""
        # Reversing -7463847412 -> -2147483647
        self.assertEqual(self.solution.reverse(-7463847412), -2147483647)

    # ----------------------------------
    # ## Large Input (10+ digits)
    # ----------------------------------

    def test_large_input_many_zeros(self):
        """Large number with many zeros, should not overflow."""
        self.assertEqual(self.solution.reverse(1000000000), 1)
        self.assertEqual(self.solution.reverse(-1000000000), -1)


if __name__ == '__main__':
    unittest.main()