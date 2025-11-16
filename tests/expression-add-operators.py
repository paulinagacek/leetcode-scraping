
import unittest


class TestAddOperators(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        num = "123"
        target = 6
        expected = ["1*2*3", "1+2+3"]
        self.assertCountEqual(self.solution.addOperators(num, target), expected)

    def test_example_2(self):
        num = "232"
        target = 8
        expected = ["2*3+2", "2+3*2"]
        self.assertCountEqual(self.solution.addOperators(num, target), expected)

    def test_example_3(self):
        num = "105"
        target = 5
        expected = ["1*0+5", "10-5"]
        self.assertCountEqual(self.solution.addOperators(num, target), expected)

    def test_no_solution(self):
        num = "3456237490"
        target = 9191
        expected = []
        self.assertCountEqual(self.solution.addOperators(num, target), expected)

    def test_leading_zeros(self):
        num = "00"
        target = 0
        expected = ["0*0", "0+0", "0-0"]
        self.assertCountEqual(self.solution.addOperators(num, target), expected)

    def test_single_digit_match(self):
        num = "5"
        target = 5
        expected = ["5"]
        self.assertCountEqual(self.solution.addOperators(num, target), expected)

    def test_single_digit_no_match(self):
        num = "5"
        target = 10
        expected = []
        self.assertCountEqual(self.solution.addOperators(num, target), expected)

    def test_single_zero(self):
        num = "0"
        target = 0
        expected = ["0"]
        self.assertCountEqual(self.solution.addOperators(num, target), expected)
        
    def test_target_is_the_number_itself(self):
        num = "1234567"
        target = 1234567
        expected = ["1234567"]
        self.assertCountEqual(self.solution.addOperators(num, target), expected)

    def test_negative_target(self):
        num = "15"
        target = -4
        expected = ["1-5"]
        self.assertCountEqual(self.solution.addOperators(num, target), expected)

    def test_large_number_as_target(self):
        num = "2147483647"
        target = 2147483647
        expected = ["2147483647"]
        self.assertCountEqual(self.solution.addOperators(num, target), expected)

    def test_large_number_no_solution(self):
        num = "2147483648"
        target = -2147483648
        expected = []
        self.assertCountEqual(self.solution.addOperators(num, target), expected)

    def test_complex_case_with_multiplication_precedence(self):
        num = "1212"
        target = 25
        expected = ["1+2*12"]
        self.assertCountEqual(self.solution.addOperators(num, target), expected)

    def test_all_subtraction(self):
        num = "987"
        target = -86
        expected = ["9-8-7"]
        self.assertCountEqual(self.solution.addOperators(num, target), [])
        
        num = "321"
        target = 0
        expected = ["3-2-1"]
        self.assertCountEqual(self.solution.addOperators(num, target), expected)
        
    def test_long_string_with_solution(self):
        num = "123456789"
        target = 45
        # There are multiple solutions, we check for one known valid solution's existence
        # The simplest one is summing all digits
        results = self.solution.addOperators(num, target)
        self.assertIn("1+2+3+4+5+6+7+8+9", results)
        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
