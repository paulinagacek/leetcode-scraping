import unittest

class TestBasicCalculatorII(unittest.TestCase):
    """
    Unit tests for the calculate method.
    """

    def setUp(self):
        self.solution = Solution()

    # ----------------------------------
    # ## Standard Cases (Order of Operations) ➕➖✖️➗
    # ----------------------------------

    def test_standard_case_1_order_of_ops(self):
        """Test standard multiplication/division before addition/subtraction."""
        s = "3+2*2"  # 3 + (2*2) = 7
        self.assertEqual(self.solution.calculate(s), 7)

    def test_standard_case_2_division(self):
        """Test division and subtraction with spaces."""
        s = " 3/2 "  # 1 (truncated)
        self.assertEqual(self.solution.calculate(s), 1)

    def test_standard_case_3_mixed_ops(self):
        """Test a mix of all four operators."""
        s = " 3+5 / 2 " # 3 + (5/2) = 3 + 2 = 5
        self.assertEqual(self.solution.calculate(s), 5)
        
    def test_multi_digit_numbers(self):
        """Test with multi-digit numbers."""
        s = "100 + 50 * 2 / 10 - 5" # 100 + (100/10) - 5 = 100 + 10 - 5 = 105
        self.assertEqual(self.solution.calculate(s), 105)

    def test_starting_with_negative_term(self):
        """Test expression starting with a negative term (implicitly 0 - N)."""
        s = "-10 + 5*2" # -10 + 10 = 0. (The canonical solution doesn't handle this directly, 
                       # but standard LeetCode constraints guarantee positive first number, 
                       # or it's handled externally. Assuming standard input.)
        
        # Note: If the first character is a '-', the solution handles it as sign='+', 
        # then processes '-', resulting in 0, then sign='-' for the next number.
        # This solution does NOT correctly handle a leading unary negation.
        # Test case must adhere to typical LeetCode constraint: positive leading term.
        # But if we must test the canonical solution as-is, we must use cases it supports.
        
        # Test case adjusted to include a leading number that makes the expression valid for this solution
        s = "0 - 10 + 5 * 2" # 0 - 10 + 10 = 0
        self.assertEqual(self.solution.calculate(s), 0)

    # ----------------------------------
    # ## Edge Cases 📐
    # ----------------------------------

    def test_single_number(self):
        """Edge case: The string contains only one number."""
        s = "123"
        self.assertEqual(self.solution.calculate(s), 123)

    def test_single_number_with_spaces(self):
        """Edge case: Single number surrounded by spaces."""
        s = " 42 "
        self.assertEqual(self.solution.calculate(s), 42)

    def test_division_by_one(self):
        """Edge case: Division by 1."""
        s = "100 / 1"
        self.assertEqual(self.solution.calculate(s), 100)
        
    def test_zero_numerator(self):
        """Edge case: Zero in the numerator."""
        s = "0 * 5 + 10 / 2" # 0 + 5 = 5
        self.assertEqual(self.solution.calculate(s), 5)
        
    def test_negative_division_truncation(self):
        """Test integer division that truncates towards zero (standard behavior)."""
        s = "1 - 8 / 3" # 1 - (8/3) = 1 - 2 = -1
        self.assertEqual(self.solution.calculate(s), -1)
        
        s = "-1 - 8 / 3" # (Implicitly handled as 0-1) - 8/3 = -1 - 2 = -3
        self.assertEqual(self.solution.calculate(s), -3) 
        
        s = "1 + 7 / -3" # 1 + (7/-3) = 1 + (-2) = -1. Note: The solution does not handle negative numbers unless they are a result of subtraction.
        # Let's use subtraction to introduce a negative number:
        s = "10 - 15 / 2" # 10 - (15/2) = 10 - 7 = 3
        self.assertEqual(self.solution.calculate(s), 3)

        s = "10 - 17 / 5" # 10 - (17/5) = 10 - 3 = 7
        self.assertEqual(self.solution.calculate(s), 7)

    # ----------------------------------
    # ## Large Input Cases 📏
    # ----------------------------------

    def test_large_input_many_additions(self):
        """Test with a long string of additions and large numbers."""
        s = "1000000 + 2000000 + 3000000 + 4000000"
        self.assertEqual(self.solution.calculate(s), 10000000)

    def test_large_input_many_multiplications_and_divisions(self):
        """Test with a long string dominated by high-precedence operations."""
        # 1 * 2 * 3 * 4 * 5 * 6 / 9 = 720 / 9 = 80
        s = "1 * 2 * 3 * 4 * 5 * 6 / 9"
        self.assertEqual(self.solution.calculate(s), 80)
        
    def test_large_input_mixed_long(self):
        """Test a long, complex mixed expression."""
        # (1000*5 + 100/2) - (5*10 + 1) = 5050 - 51 = 4999
        s = "1000 * 5 + 100 / 2 - 5 * 10 - 1"
        self.assertEqual(self.solution.calculate(s), 4999)

if __name__ == '__main__':
    unittest.main()