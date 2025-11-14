import unittest
import collections
from typing import List, Dict, Set, Tuple, Any

class TestMergeIntervalsGraph(unittest.TestCase):
    """
    Unit tests for the merge method using the Graph approach.
    Since the problem only requires the merged intervals, not a specific order, 
    the results are sorted for comparison.
    """

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()
        
    def assertIntervalsEqual(self, actual: List[List[int]], expected: List[List[int]]):
        """Sorts the result lists before comparison as order doesn't matter."""
        actual_sorted = sorted(actual, key=lambda x: x[0])
        expected_sorted = sorted(expected, key=lambda x: x[0])
        self.assertEqual(actual_sorted, expected_sorted)

    # ----------------------------------
    # ## Standard Cases
    # ----------------------------------

    def test_standard_merge(self):
        """Basic case: Two intervals merge."""
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        self.assertIntervalsEqual(self.solution.merge(intervals), expected)

    def test_multi_merge(self):
        """Case where multiple intervals form one large component."""
        intervals = [[1, 4], [0, 2], [3, 5], [6, 8]]
        expected = [[0, 5], [6, 8]]
        self.assertIntervalsEqual(self.solution.merge(intervals), expected)

    def test_contained_interval(self):
        """Case where one interval is fully contained within another."""
        intervals = [[1, 10], [3, 7], [12, 15]]
        expected = [[1, 10], [12, 15]]
        self.assertIntervalsEqual(self.solution.merge(intervals), expected)
        
    def test_touching_intervals(self):
        """Case where intervals only touch at the boundary."""
        intervals = [[1, 2], [2, 3], [3, 4]]
        expected = [[1, 4]]
        self.assertIntervalsEqual(self.solution.merge(intervals), expected)

    # ----------------------------------
    # ## Edge Cases
    # ----------------------------------

    def test_empty_list(self):
        """Edge case: Empty input list."""
        intervals = []
        expected = []
        self.assertIntervalsEqual(self.solution.merge(intervals), expected)

    def test_single_interval(self):
        """Edge case: List with a single interval."""
        intervals = [[1, 4]]
        expected = [[1, 4]]
        self.assertIntervalsEqual(self.solution.merge(intervals), expected)

    def test_no_overlap(self):
        """Edge case: No intervals overlap at all."""
        intervals = [[1, 2], [3, 4], [5, 6]]
        expected = [[1, 2], [3, 4], [5, 6]]
        self.assertIntervalsEqual(self.solution.merge(intervals), expected)

    def test_all_intervals_identical(self):
        """Edge case: All intervals are the same."""
        intervals = [[1, 5], [1, 5], [1, 5]]
        expected = [[1, 5]]
        self.assertIntervalsEqual(self.solution.merge(intervals), expected)
        
    def test_negative_coordinates(self):
        """Case with negative and zero coordinates."""
        intervals = [[-5, -1], [0, 5], [-1, 2]]
        expected = [[-5, 5]]
        self.assertIntervalsEqual(self.solution.merge(intervals), expected)

    # ----------------------------------
    # ## Large Input Cases
    # ----------------------------------

    def test_large_input_linear_overlap(self):
        """Large array where all intervals overlap linearly (N^2 check)."""
        N = 100
        # Intervals: [[1, 3], [2, 4], [3, 5], ..., [100, 102]]
        intervals = [[i, i + 2] for i in range(1, N + 1)]
        
        # All intervals overlap, should merge into one component.
        # Min start is 1, Max end is 102 (from [100, 102]).
        expected = [[1, N + 2]] 
        self.assertIntervalsEqual(self.solution.merge(intervals), expected)

    def test_large_input_no_overlap(self):
        """Large array where no intervals overlap (N^2 check)."""
        N = 500
        # Intervals: [[1, 2], [4, 5], [7, 8], ..., [1501, 1502]]
        intervals = [[3 * i + 1, 3 * i + 2] for i in range(N)]
        
        # No merges, the result is the same as the input.
        expected = intervals
        self.assertIntervalsEqual(self.solution.merge(intervals), expected)

    def test_large_input_two_large_components(self):
        """Large array split into two large, separate connected components."""
        N = 100
        # Component 1 (low range): [[1, 3], [2, 4], ..., [50, 52]]
        comp1 = [[i, i + 2] for i in range(1, N // 2 + 1)] 
        # Component 2 (high range): [[101, 103], [102, 104], ..., [152, 154]]
        comp2 = [[i, i + 2] for i in range(N + 1, N + N // 2 + 2)] 
        
        intervals = comp1 + comp2
        
        # Expected merge 1: Min start is 1, Max end is 50 + 2 = 52
        expected_merge1 = [1, N // 2 + 2] # [1, 52] - CORRECT
        
        # Expected merge 2: Min start is 101, Max end is (152 + 2) = 154
        # N + N // 2 + 1 is the last 'i', so max end is N + N // 2 + 1 + 2 = 153
        # No, the range stops at 153. The last element is 152. Max end is 152 + 2 = 154.
        expected_merge2 = [N + 1, N + N // 2 + 3] # [101, 154]
        
        expected = [expected_merge1, expected_merge2]
        self.assertIntervalsEqual(self.solution.merge(intervals), expected)


if __name__ == '__main__':
    unittest.main()