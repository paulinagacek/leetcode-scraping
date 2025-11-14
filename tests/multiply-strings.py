import unittest
from typing import List
from itertools import zip_longest

class TestMultiplyStrings(unittest.TestCase):
    """
    Unit tests for the multiply method of the Solution class.
    Tests cover standard inputs, edge cases (zero, one), and large inputs.
    """

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    # ----------------------------------
    # ## Standard Cases
    # ----------------------------------

    def test_standard_case_one(self):
        """Basic multiplication: 123 * 456 = 56088"""
        num1 = "123"
        num2 = "456"
        expected = "56088"
        self.assertEqual(self.solution.multiply(num1, num2), expected)

    def test_standard_case_two(self):
        """Multiplication with small numbers (9 * 9 = 81)"""
        num1 = "9"
        num2 = "9"
        expected = "81"
        self.assertEqual(self.solution.multiply(num1, num2), expected)
        
    def test_standard_case_three(self):
        """Multiplication resulting in carry-over across many places: 98 * 99 = 9702"""
        num1 = "98"
        num2 = "99"
        expected = "9702"
        self.assertEqual(self.solution.multiply(num1, num2), expected)

    def test_standard_case_four_with_internal_zeros(self):
        """Multiplication involving internal zeros: 105 * 20 = 2100"""
        num1 = "105"
        num2 = "20"
        expected = "2100"
        self.assertEqual(self.solution.multiply(num1, num2), expected)
        
    def test_standard_case_five_first_digit_is_one(self):
        """Test where one number starts with 1: 15 * 5 = 75"""
        num1 = "15"
        num2 = "5"
        expected = "75"
        self.assertEqual(self.solution.multiply(num1, num2), expected)

    # ----------------------------------
    # ## Edge Cases
    # ----------------------------------

    def test_zero_result_case_one(self):
        """One number is zero (num1="0")."""
        num1 = "0"
        num2 = "12345"
        expected = "0"
        self.assertEqual(self.solution.multiply(num1, num2), expected)

    def test_zero_result_case_two(self):
        """One number is zero (num2="0")."""
        num1 = "6789"
        num2 = "0"
        expected = "0"
        self.assertEqual(self.solution.multiply(num1, num2), expected)
        
    def test_one_as_multiplier(self):
        """One number is '1'."""
        num1 = "1"
        num2 = "98765"
        expected = "98765"
        self.assertEqual(self.solution.multiply(num1, num2), expected)
        
    def test_multiplication_by_one_zero(self):
        """Multiplication by 10 (which is '1' + zero). 12 * 10 = 120."""
        num1 = "12"
        num2 = "10"
        expected = "120"
        self.assertEqual(self.solution.multiply(num1, num2), expected)
        
    def test_long_zero_string(self):
        """Multiplication by a string of zeros: 12 * 00 = 0."""
        num1 = "12"
        num2 = "00000"
        expected = "000000"
        # The canonical solution handles "00000" implicitly because the multiplication 
        # result of any non-zero string with '0' digits will eventually return 0. 
        # However, the initial guard only checks "0". If it receives "00", it proceeds.
        # Since the digits are processed, '0' * X will result in '0' and the final sum will be 0.
        self.assertEqual(self.solution.multiply(num1, num2), expected)

    # ----------------------------------
    # ## Large Input Cases
    # ----------------------------------
    
    def test_large_input_square(self):
        """Test with two large, identical strings: 999 * 999 = 998001"""
        num1 = "999" * 10 # 30 digits
        num2 = "999" * 10 # 30 digits
        
        # Result of 999...999 * 999...999 (30 nines each)
        # 10 nines * 10 nines = (10^30 - 1)^2 = 10^60 - 2*10^30 + 1
        # The result is 59 nines, one 8, 30 zeros, one 1. Length 60.
        # It's (999... * 100...0) - (999...)
        # A simpler way: 9 * 9 = 81. 99 * 99 = 9801. 999 * 999 = 998001.
        # 9... (n) * 9... (n) = 9... (n-1) 8 0... (n-1) 1
        n = 30
        expected = "9" * (n - 1) + "8" + "0" * (n - 1) + "1"
        self.assertEqual(self.solution.multiply(num1, num2), expected)

    def test_large_input_different_lengths(self):
        """Test with two large strings of different, substantial lengths."""
        num1 = "123456789" # 9 digits
        num2 = "10000000000000000000" # 1 followed by 20 zeros (21 digits)
        
        # num1 * 10^20. Just appends 20 zeros to num1.
        zeros = "0" * 19
        expected = num1 + zeros
        self.assertEqual(self.solution.multiply(num1, num2), expected)
        
    def test_large_input_no_zeros_in_middle(self):
        """Test where every digit contributes to the sum (e.g., all ones)."""
        num1 = "11111" # 5 digits
        num2 = "11111" # 5 digits
        # Result is 123454321
        expected = "123454321"
        self.assertEqual(self.solution.multiply(num1, num2), expected)
        
    def test_large_input_first_long_second_short(self):
        """Test where the first number is much longer than the second."""
        num1 = "8" * 50 # 50 digits
        num2 = "2"
        
        # 88...8 * 2 = 177...76 (49 ones and one 6 at the end) -> NO
        # 8 * 2 = 16
        # 88 * 2 = 176
        # 888 * 2 = 1776
        # 8...8 (n) * 2 = 1 7...7 (n-1) 6
        n = 50
        expected = "1" + "7" * (n - 1) + "6"
        self.assertEqual(self.solution.multiply(num1, num2), expected)


if __name__ == '__main__':
    unittest.main()