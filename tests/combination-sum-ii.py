import unittest
from typing import List

class TestCombinationSum2(unittest.TestCase):
    """
    Unit tests for the combinationSum2 method of the Solution class.
    Tests cover standard inputs, edge cases (no solution, zero target,
    large duplicates), and a large input case.
    """

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    def assertResultsEqual(self, actual: List[List[int]], expected: List[List[int]]):
        """
        Helper to compare two lists of lists (order-independent comparison).
        It sorts each inner list and then compares the sets of sorted tuples.
        """
        # Convert lists of lists to sets of sorted tuples for canonical comparison
        actual_set = set(tuple(sorted(t)) for t in actual)
        expected_set = set(tuple(sorted(t)) for t in expected)
        self.assertEqual(actual_set, expected_set, f"Actual: {actual}, Expected: {expected}")

    # ----------------------------------
    # ## Standard Cases
    # ----------------------------------

    def test_standard_case_one(self):
        """Standard case from problem description: candidates with duplicates."""
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        expected = [
            [1, 7],
            [1, 2, 5],
            [2, 6],
            [1, 1, 6]  # Note: The two '1's must be from different original positions, but since the array is sorted first, they are treated as unique combinations.
        ]
        self.assertResultsEqual(self.solution.combinationSum2(candidates, target), expected)

    def test_standard_case_two(self):
        """Standard case with a small set and no duplicates in output."""
        candidates = [2, 5, 2, 1, 2]
        target = 5
        # Sorted candidates: [1, 2, 2, 2, 5]
        expected = [
            [1, 2, 2],
            [5]
        ]
        self.assertResultsEqual(self.solution.combinationSum2(candidates, target), expected)

    # ----------------------------------
    # ## Edge Cases
    # ----------------------------------

    def test_no_solution(self):
        """Case where no combination sums to the target (target > max possible sum)."""
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 33
        expected = []
        self.assertResultsEqual(self.solution.combinationSum2(candidates, target), expected)

    def test_target_too_small(self):
        """Case where the target is smaller than the minimum candidate."""
        candidates = [5, 6, 7]
        target = 4
        expected = []
        self.assertResultsEqual(self.solution.combinationSum2(candidates, target), expected)

    def test_exact_match_with_single_element(self):
        """Case where a single candidate equals the target and others exist."""
        candidates = [3, 4, 5, 1, 6]
        target = 5
        expected = [[5], [1, 4]]
        self.assertResultsEqual(self.solution.combinationSum2(candidates, target), expected)

    def test_all_duplicates(self):
        """Case with all candidates being the same, testing the duplicate skipping logic."""
        candidates = [2, 2, 2, 2, 2, 2]
        target = 6
        # Expected: only one combination of three '2's: [2, 2, 2]
        expected = [[2, 2, 2]]
        self.assertResultsEqual(self.solution.combinationSum2(candidates, target), expected)

    def test_all_duplicates_no_solution(self):
        """Case with all candidates being the same, but no solution."""
        candidates = [3, 3, 3, 3]
        target = 10
        expected = []
        self.assertResultsEqual(self.solution.combinationSum2(candidates, target), expected)

    def test_mixed_duplicates_and_non_duplicates(self):
        """Case with several unique combinations possible due to duplicates."""
        candidates = [1, 1, 1, 3, 3, 5]
        target = 5
        expected = [
            [5],
            [1, 1, 3]
        ]
        self.assertResultsEqual(self.solution.combinationSum2(candidates, target), expected)
        
    def test_zero_target(self):
        """Case where the target is 0. The function returns [[]]."""
        candidates = [1, 2, 3]
        target = 0
        # Correction: The canonical solution returns [[]] for target=0.
        expected = [[]] 
        self.assertResultsEqual(self.solution.combinationSum2(candidates, target), expected)


    # ----------------------------------
    # ## Large Input Case
    # ----------------------------------

    def test_large_input_many_solutions(self):
        """Large input with many candidates and multiple combinations."""
        candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
        target = 12
        
        # Corrected Expected List (Removing the missing combination [1, 1, 2, 2, 3, 3])
        expected = [
            # L=2
            [2, 10], [3, 9], [4, 8], [5, 7],
            # L=3
            [1, 1, 10], [1, 2, 9], [1, 3, 8], [1, 4, 7], [1, 5, 6],
            [2, 2, 8], [2, 3, 7], [2, 4, 6], [3, 4, 5],
            # L=4
            [1, 1, 2, 8], [1, 1, 3, 7], [1, 1, 4, 6],
            [1, 2, 2, 7], [1, 2, 3, 6], [1, 2, 4, 5],
            [2, 2, 3, 5],
            # L=5
            [1, 1, 2, 2, 6], [1, 1, 2, 3, 5], [1, 2, 2, 3, 4],
        ]
        
        self.assertResultsEqual(self.solution.combinationSum2(candidates, target), expected)


if __name__ == '__main__':
    unittest.main()