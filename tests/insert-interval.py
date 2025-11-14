import unittest
from typing import List

class TestInsertInterval(unittest.TestCase):
    """
    Unit tests for the insert method of the Solution class.
    Tests cover standard merges, boundary conditions, and large lists.
    """

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    # ----------------------------------
    # ## Standard Cases
    # ----------------------------------

    def test_standard_case_middle_merge(self):
        """Standard case: newInterval merges with two existing intervals in the middle."""
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval = [4, 8]  # Merges [3, 5], [6, 7], [8, 10]
        expected = [[1, 2], [3, 10], [12, 16]]
        self.assertEqual(self.solution.insert(intervals, newInterval), expected)

    def test_standard_case_single_merge(self):
        """newInterval merges with only one existing interval."""
        intervals = [[1, 3], [6, 9]]
        newInterval = [2, 5]
        expected = [[1, 5], [6, 9]]
        self.assertEqual(self.solution.insert(intervals, newInterval), expected)

    def test_standard_case_no_merge(self):
        """newInterval is inserted without merging any existing intervals."""
        intervals = [[1, 2], [6, 7], [10, 15]]
        newInterval = [4, 5]
        expected = [[1, 2], [4, 5], [6, 7], [10, 15]]
        self.assertEqual(self.solution.insert(intervals, newInterval), expected)

    # ----------------------------------
    # ## Edge Cases
    # ----------------------------------

    def test_empty_intervals_list(self):
        """Edge case: The list of existing intervals is empty."""
        intervals = []
        newInterval = [5, 7]
        expected = [[5, 7]]
        self.assertEqual(self.solution.insert(intervals, newInterval), expected)

    def test_new_interval_before_all(self):
        """Edge case: newInterval comes before all others and doesn't overlap."""
        intervals = [[5, 8], [10, 12]]
        newInterval = [1, 3]
        expected = [[1, 3], [5, 8], [10, 12]]
        self.assertEqual(self.solution.insert(intervals, newInterval), expected)

    def test_new_interval_after_all(self):
        """Edge case: newInterval comes after all others and doesn't overlap."""
        intervals = [[1, 3], [5, 7]]
        newInterval = [10, 12]
        expected = [[1, 3], [5, 7], [10, 12]]
        self.assertEqual(self.solution.insert(intervals, newInterval), expected)

    def test_new_interval_fully_contains_others(self):
        """Edge case: newInterval covers all existing intervals."""
        intervals = [[1, 3], [5, 7], [9, 11]]
        newInterval = [0, 15]
        expected = [[0, 15]]
        self.assertEqual(self.solution.insert(intervals, newInterval), expected)

    def test_new_interval_fully_contained(self):
        """Edge case: newInterval is entirely contained within an existing interval."""
        intervals = [[1, 10]]
        newInterval = [3, 5]
        expected = [[1, 10]]
        self.assertEqual(self.solution.insert(intervals, newInterval), expected)

    def test_merge_touching_boundaries(self):
        """Edge case: newInterval merges with others only by touching boundaries."""
        intervals = [[1, 2], [3, 4], [5, 6]]
        newInterval = [2, 5]  # Touches [1, 2] at 2, touches [3, 4] at 3, touches [5, 6] at 5
        expected = [[1, 6]]
        self.assertEqual(self.solution.insert(intervals, newInterval), expected)

    def test_boundary_no_overlap(self):
        """Edge case: newInterval is exactly one unit away from an interval."""
        intervals = [[1, 2], [4, 5]]
        newInterval = [3, 3]
        expected = [[1, 2], [3, 3], [4, 5]]
        self.assertEqual(self.solution.insert(intervals, newInterval), expected)

    # ----------------------------------
    # ## Large Input Cases
    # ----------------------------------

    def test_large_input_merge_all(self):
        """Large array where the new interval merges everything into one."""
        N = 1000
        # Create intervals: [[1, 2], [3, 4], [5, 6], ..., [1999, 2000]]
        intervals = [[2 * i + 1, 2 * i + 2] for i in range(N)]
        # New interval covers start and end: [0, 2001]
        newInterval = [0, 2 * N + 1]
        
        expected = [[0, 2 * N + 1]]
        self.assertEqual(self.solution.insert(intervals, newInterval), expected)

    def test_large_input_no_merge(self):
        """Large array where the new interval is placed at the end without merging."""
        N = 1000
        # Intervals: [[0, 1], [2, 3], ..., [1998, 1999]]
        intervals = [[2 * i, 2 * i + 1] for i in range(N)]
        # New interval: [2000, 2001]
        newInterval = [2 * N, 2 * N + 1]
        
        expected = intervals + [newInterval]
        self.assertEqual(self.solution.insert(intervals, newInterval), expected)
        
    def test_large_input_merge_only_last_third(self):
        """Large array where the new interval only merges with the last third."""
        N = 999
        intervals = [[i, i + 1] for i in range(N)]
        
        # New interval starts at 666 and ends at 1000
        newInterval = [N // 3 * 2, N + 1] # [666, 1000]
        
        # --- CORRECTION ---
        # The new interval [666, 1000] touches/overlaps with [665, 666].
        # It merges all intervals from index 665 onward.
        
        # Intervals before merge: 0 to 664 (665 intervals)
        expected_no_merge = intervals[:N // 3 * 2 - 1] # Slicing up to index 664
        
        # The final merged interval starts at 665 (min(666, 665)) and ends at 1000 (N+1)
        expected_merged = [[N // 3 * 2 - 1, N + 1]] # [665, 1000]
        
        expected = expected_no_merge + expected_merged
        self.assertEqual(self.solution.insert(intervals, newInterval), expected)


if __name__ == '__main__':
    unittest.main()