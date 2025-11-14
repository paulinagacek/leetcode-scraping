import unittest
from typing import List

class TestFirstMissingPositive(unittest.TestCase):
    """
    Unit tests for the firstMissingPositive method of the Solution class.
    Tests cover standard inputs, edge cases (empty list, negatives, zeros, 
    max/min values, and all consecutive numbers), and a large input.
    """

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    # ----------------------------------
    # ## Standard Cases
    # ----------------------------------

    def test_standard_case_one(self):
        """Simple case where the missing number is small."""
        nums = [1, 2, 0]
        expected = 3
        self.assertEqual(self.solution.firstMissingPositive(nums), expected)

    def test_standard_case_two(self):
        """Simple case where the missing number is in the middle."""
        nums = [3, 4, -1, 1]
        expected = 2
        self.assertEqual(self.solution.firstMissingPositive(nums), expected)

    def test_standard_case_three(self):
        """Simple case where the missing number is 1."""
        nums = [7, 8, 9, 11, 12]
        expected = 1
        self.assertEqual(self.solution.firstMissingPositive(nums), expected)
        
    def test_no_gaps_all_consecutive(self):
        """Case where 1 to n are present, so result is n + 1."""
        nums = [1, 2, 3, 4, 5]
        expected = 6
        self.assertEqual(self.solution.firstMissingPositive(nums), expected)

    # ----------------------------------
    # ## Edge Cases
    # ----------------------------------

    def test_empty_list(self):
        """The smallest missing positive in an empty list is 1."""
        nums = []
        expected = 1
        self.assertEqual(self.solution.firstMissingPositive(nums), expected)

    def test_single_element_list_missing(self):
        """List with one non-positive element."""
        nums = [0]
        expected = 1
        self.assertEqual(self.solution.firstMissingPositive(nums), expected)
        
    def test_single_element_list_present(self):
        """List with one positive element 1."""
        nums = [1]
        expected = 2
        self.assertEqual(self.solution.firstMissingPositive(nums), expected)

    def test_only_negative_numbers(self):
        """List containing only negative numbers."""
        nums = [-5, -10, -1, -20]
        expected = 1
        self.assertEqual(self.solution.firstMissingPositive(nums), expected)

    def test_contains_zero(self):
        """List containing only zeros."""
        nums = [0, 0, 0, 0]
        expected = 1
        self.assertEqual(self.solution.firstMissingPositive(nums), expected)

    def test_duplicates(self):
        """List with duplicates, which shouldn't affect the result."""
        nums = [1, 1, 2, 2, 3, 3]
        expected = 4
        self.assertEqual(self.solution.firstMissingPositive(nums), expected)

    def test_missing_and_out_of_range(self):
        """List contains a missing number and large numbers (which are ignored)."""
        # n = 4. We care about 1, 2, 3, 4. 3 is missing.
        nums = [1, 2, 100, 4]
        expected = 3
        self.assertEqual(self.solution.firstMissingPositive(nums), expected)

    # ----------------------------------
    # ## Large Input Case
    # ----------------------------------

    def test_large_input_missing_one_in_middle(self):
        """Large input where the missing number is far in the middle."""
        N = 1000
        # Create an array of [1, 2, ..., 499, 501, ..., 1000]
        nums = list(range(1, N + 1))
        missing_num = 500
        nums.remove(missing_num)
        # Add some irrelevant large numbers and negatives to the end
        nums.extend([N * 2, -10, 0, N * 3])
        
        expected = missing_num
        self.assertEqual(self.solution.firstMissingPositive(nums), expected)

    def test_large_input_missing_first(self):
        """Large input where 1 is the missing number."""
        N = 1000
        # Array is [2, 3, ..., 1000] plus non-relevant numbers
        nums = list(range(2, N + 1))
        nums.extend([-1, -2, 10000])
        
        expected = 1
        self.assertEqual(self.solution.firstMissingPositive(nums), expected)

    def test_large_input_all_present(self):
        """Large input where all numbers 1 to n are present."""
        N = 1000
        # Array of [1, 2, ..., 1000]
        nums = list(range(1, N + 1))
        # Add irrelevant numbers to increase array size (n)
        nums.extend([10000, 20000])
        
        # New N is 1002. The algorithm cares about 1 to 1002.
        # Since 1001 and 1002 are missing, the result should be 1001.
        
        expected = N + 1 # Which is 1001
        self.assertEqual(self.solution.firstMissingPositive(nums), expected)


if __name__ == '__main__':
    unittest.main()