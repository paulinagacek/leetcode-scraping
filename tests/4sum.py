import unittest
from typing import List

class TestFourSum(unittest.TestCase):
    """
    Unit tests for the fourSum method of the Solution class.
    The test cases cover standard inputs, edge cases (empty list, target not found,
    duplicates, min/max integer values), and a large input.
    """

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    def assertResultsEqual(self, actual: List[List[int]], expected: List[List[int]]):
        """Helper to compare two lists of lists (sets of tuples for order-independent comparison)."""
        # Convert lists of lists to sets of sorted tuples for canonical comparison
        actual_set = set(tuple(sorted(t)) for t in actual)
        expected_set = set(tuple(sorted(t)) for t in expected)
        self.assertEqual(actual_set, expected_set, f"Actual: {actual}, Expected: {expected}")

    # Standard Test Cases
    def test_standard_case_one(self):
        """Standard case with positive, negative, and zero numbers."""
        nums = [1, 0, -1, 0, -2, 2]
        target = 0
        expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        self.assertResultsEqual(self.solution.fourSum(nums, target), expected)

    def test_standard_case_two(self):
        """Standard case with all positive numbers."""
        nums = [2, 2, 2, 2, 2]
        target = 8
        expected = [[2, 2, 2, 2]]
        self.assertResultsEqual(self.solution.fourSum(nums, target), expected)

    def test_standard_case_three(self):
        """Case with a solution of 10."""
        nums = [1, 2, 3, 4]
        target = 10
        expected = [[1, 2, 3, 4]] 
        self.assertResultsEqual(self.solution.fourSum(nums, target), expected)

    # Edge Cases
    def test_minimum_length_input(self):
        """Input with exactly 4 elements."""
        nums = [1, 1, 1, 1]
        target = 4
        expected = [[1, 1, 1, 1]]
        self.assertResultsEqual(self.solution.fourSum(nums, target), expected)
        
    def test_less_than_four_elements(self):
        """Input with less than 4 elements (should return empty list)."""
        nums = [1, 2, 3]
        target = 6
        expected = []
        self.assertResultsEqual(self.solution.fourSum(nums, target), expected)

    def test_empty_list(self):
        """Empty input list."""
        nums = []
        target = 0
        expected = []
        self.assertResultsEqual(self.solution.fourSum(nums, target), expected)

    def test_with_duplicates_and_non_zero_target(self):
        """Case with many duplicates and a non-zero target."""
        nums = [-3, -1, 0, 0, 1, 3]
        target = 0
        # Expected: [-3, -1, 1, 3], [-3, 0, 0, 3], [-1, 0, 0, 1]
        expected = [[-3, -1, 1, 3], [-3, 0, 0, 3], [-1, 0, 0, 1]]
        self.assertResultsEqual(self.solution.fourSum(nums, target), expected)
        
    def test_duplicates_leading_to_empty_result(self):
        """Case with duplicates but no four-sum solution."""
        nums = [0, 0, 0, 0]
        target = 1
        expected = []
        self.assertResultsEqual(self.solution.fourSum(nums, target), expected)

    # Large Number Cases (Min/Max Target and Array Values)
    def test_max_target_and_values(self):
        """Test with very large values and large target (potential overflow if not handled)."""
        # LeetCode constraints often limit values to around 10^9. Python handles large integers.
        # Use values that challenge the average_value pruning logic and two-pointer logic.
        MAX_VAL = 10**5
        nums = [MAX_VAL, MAX_VAL, MAX_VAL, MAX_VAL]
        target = 4 * MAX_VAL
        expected = [[MAX_VAL, MAX_VAL, MAX_VAL, MAX_VAL]]
        self.assertResultsEqual(self.solution.fourSum(nums, target), expected)

    def test_min_target_and_values(self):
        """Test with very small/negative values and small target."""
        MIN_VAL = -10**5
        nums = [MIN_VAL, MIN_VAL, MIN_VAL, MIN_VAL]
        target = 4 * MIN_VAL
        expected = [[MIN_VAL, MIN_VAL, MIN_VAL, MIN_VAL]]
        self.assertResultsEqual(self.solution.fourSum(nums, target), expected)

    def test_target_zero_with_large_mixed_values(self):
        """Target zero with large positive and negative numbers."""
        nums = [-1000, -1, 1, 1000]
        target = 0
        expected = [[-1000, -1, 1, 1000]]
        self.assertResultsEqual(self.solution.fourSum(nums, target), expected)
        
    def test_large_input_many_solutions(self):
        """Test with a relatively large input with many possible solutions."""
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 20
        # The full 16 solutions are listed below:
        expected = [
            [1, 2, 7, 10], [1, 2, 8, 9], [1, 3, 6, 10], [1, 3, 7, 9], 
            [1, 4, 5, 10], [1, 4, 6, 9], [1, 4, 7, 8], [1, 5, 6, 8], 
            [2, 3, 5, 10], [2, 3, 6, 9], [2, 3, 7, 8], [2, 4, 5, 9], 
            [2, 4, 6, 8], [2, 5, 6, 7], [3, 4, 5, 8], [3, 4, 6, 7]
        ]
        self.assertResultsEqual(self.solution.fourSum(nums, target), expected)

    def test_large_input_with_duplicates_and_negative_target(self):
        """Large input with mixed values, duplicates, and a negative target."""
        nums = [-5, -5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        target = -10
        # The full 19 correct solutions (summing to -10) are listed below:
        expected = [
            [-5, -5, 0, 0],   # -10
            [-5, -5, -1, 1],  # -10
            [-5, -5, -2, 2],  # -10
            [-5, -4, -1, 0],  # -10
            [-5, -4, -2, 1],  # -10
            [-5, -4, -3, 2],  # -10
            [-5, -3, -2, 0],  # -10
            [-5, -3, -3, 1],  # -10 (Missing)
            [-5, -2, -2, -1], # -10 (Missing)
            [-5, -3, -1, -1], # -10 (Missing)
            [-5, -4, -4, 3],  # -10 (Missing)
            [-4, -4, -2, 0],  # -10
            [-4, -4, -3, 1],  # -10 (Missing)
            [-4, -4, -1, -1], # -10 (Missing)
            [-4, -3, -2, -1], # -10
            [-4, -3, -3, 0],  # -10 (Missing)
            [-3, -3, -2, -2], # -10 (Missing)
            [-5, -5, -4, 4],  # -10 (Missing)
            [-5, -3, -2, -0] # This should be [-5, -3, -2, 0] (Present)
        ]
        
        # A clean, sorted list of the 19 correct solutions:
        expected = [
            [-5, -5, -4, 4], [-5, -5, -3, 3], [-5, -5, -2, 2], [-5, -5, -1, 1], [-5, -5, 0, 0], 
            [-5, -4, -4, 3], [-5, -4, -3, 2], [-5, -4, -2, 1], [-5, -4, -1, 0],
            [-5, -3, -3, 1], [-5, -3, -2, 0], [-5, -3, -1, -1], 
            [-5, -2, -2, -1],
            [-4, -4, -3, 1], [-4, -4, -2, 0], [-4, -4, -1, -1],
            [-4, -3, -3, 0], [-4, -3, -2, -1],
            [-3, -3, -2, -2]
        ]
        self.assertResultsEqual(self.solution.fourSum(nums, target), expected)

if __name__ == '__main__':
    unittest.main()