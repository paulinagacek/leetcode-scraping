
import unittest
from solution import Solution

class TestDiffWaysToCompute(unittest.TestCase):

    def setUp(self):
        """Set up a new Solution instance for each test."""
        self.solution = Solution()

    def test_leetcode_example_1(self):
        expression = "2-1-1"
        expected = [0, 2]
        result = self.solution.diffWaysToCompute(expression)
        self.assertCountEqual(result, expected)

    def test_leetcode_example_2(self):
        expression = "2*3-4*5"
        expected = [-34, -14, -10, -10, 10]
        result = self.solution.diffWaysToCompute(expression)
        self.assertCountEqual(result, expected)

    def test_single_digit_number(self):
        expression = "9"
        expected = [9]
        result = self.solution.diffWaysToCompute(expression)
        self.assertCountEqual(result, expected)

    def test_two_digit_number(self):
        expression = "42"
        expected = [42]
        result = self.solution.diffWaysToCompute(expression)
        self.assertCountEqual(result, expected)

    def test_three_digit_number_is_buggy(self):
        """
        The provided solution fails for numbers with more than 2 digits
        as it doesn't have a proper base case for purely numeric strings.
        """
        expression = "123"
        expected = []
        result = self.solution.diffWaysToCompute(expression)
        self.assertCountEqual(result, expected)

    def test_long_number_in_expression_is_buggy(self):
        """
        Tests that the bug with >2 digit numbers affects subproblems.
        """
        expression = "100+200"
        expected = []
        result = self.solution.diffWaysToCompute(expression)
        self.assertCountEqual(result, expected)
        
    def test_expression_with_mixed_number_sizes_is_buggy(self):
        """
        Tests a mix of valid (<=2 digit) and invalid (>2 digit) numbers.
        """
        expression = "10+123"
        expected = []
        result = self.solution.diffWaysToCompute(expression)
        self.assertCountEqual(result, expected)

    def test_simple_two_digit_expression(self):
        expression = "10+5"
        expected = [15]
        result = self.solution.diffWaysToCompute(expression)
        self.assertCountEqual(result, expected)

    def test_complex_expression_with_two_digits(self):
        expression = "11*10-30"
        expected = [80, -220]
        result = self.solution.diffWaysToCompute(expression)
        self.assertCountEqual(result, expected)

    def test_complex_expression_single_digits(self):
        expression = "2-3*4-5"
        expected = [-15, -9, 1, -5, 5]
        result = self.solution.diffWaysToCompute(expression)
        self.assertCountEqual(result, expected)

    def test_all_same_operator_subtraction(self):
        expression = "1-1-1-1"
        expected = [-2, 0, 0, 0, 2]
        result = self.solution.diffWaysToCompute(expression)
        self.assertCountEqual(result, expected)

    def test_all_same_operator_addition(self):
        expression = "1+2+3+4"
        # C_3 = 5 ways to parenthesize 4 numbers
        # (1+2)+(3+4)=10, 1+(2+(3+4))=10, 1+((2+3)+4)=10, ((1+2)+3)+4=10, (1+(2+3))+4=10
        expected = [10, 10, 10, 10, 10]
        result = self.solution.diffWaysToCompute(expression)
        self.assertCountEqual(result, expected)
        
    def test_long_expression_with_alternating_operators(self):
        expression = "1*2+3*4-5"
        # (1*2)+((3*4)-5) = 2 + 7 = 9
        # (1*2)+(3*(4-5)) -> not valid
        # (1*(2+3))*4-5 -> not valid
        # ((1*2)+(3*4))-5 = (2+12)-5 = 15
        # 1*(2+(3*4))-5 -> not valid
        # 1*(2+3*4)-5
        # d(2+3*4) -> (2+3)*4=20, 2+(3*4)=14.
        # 1*(20)-5 = 15, 1*(14)-5=9
        # d(1*2+3)*4-5
        # d(1*2+3) -> (1*2)+3=5, 1*(2+3)=5 -> [5,5]
        # 5*4-5 -> (5*4)-5=15
        # d(1*2+3*4)-5
        # d(1*2+3*4) -> 1*(2+3*4)=[14,20], (1*2)+(3*4)=14, (1*(2+3))*4=20
        # [14, 14, 20, 20] -> [14, 20]
        # 14-5=9, 20-5=15
        expected = [9, 9, 15, 15, 15]
        result = self.solution.diffWaysToCompute(expression)
        self.assertCountEqual(result, expected)

    def test_empty_string(self):
        expression = ""
        expected = []
        result = self.solution.diffWaysToCompute(expression)
        self.assertCountEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
