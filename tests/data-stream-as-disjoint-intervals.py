import unittest
from typing import List, Set


class TestSummaryRanges(unittest.TestCase):
    """
    Unit tests for the SummaryRanges class.
    Since the problem is sequential, a single comprehensive test sequence is most effective.
    """

    # ----------------------------------
    # ## Comprehensive Sequence Test 🧪
    # ----------------------------------

    def test_official_sequence_and_edge_cases(self):
        """Tests a standard sequence covering single numbers, merges, and duplicates."""
        sr = SummaryRanges()

        # 1. Edge Case: First number
        sr.addNum(1) 
        self.assertEqual(sr.getIntervals(), [[1, 1]])

        # 2. Standard Case: Non-contiguous addition
        sr.addNum(3) 
        self.assertEqual(sr.getIntervals(), [[1, 1], [3, 3]])

        # 3. Standard Case: New interval
        sr.addNum(7) 
        self.assertEqual(sr.getIntervals(), [[1, 1], [3, 3], [7, 7]])
        
        # 4. Standard Case: Merge backward (3 becomes [3, 4])
        sr.addNum(4) 
        self.assertEqual(sr.getIntervals(), [[1, 1], [3, 4], [7, 7]])

        # 5. Edge Case: Duplicate addition (no change)
        sr.addNum(4) 
        self.assertEqual(sr.getIntervals(), [[1, 1], [3, 4], [7, 7]])
        
        # 6. Standard Case: New interval at the end
        sr.addNum(9)
        self.assertEqual(sr.getIntervals(), [[1, 1], [3, 4], [7, 7], [9, 9]])

        # 7. Standard Case: Merge with existing neighbor ([7, 8])
        sr.addNum(8) 
        self.assertEqual(sr.getIntervals(), [[1, 1], [3, 4], [7, 9]])

        # 8. Standard Case: Merge two intervals ([3, 4] and [7, 9] merged to [3, 9])
        sr.addNum(5) 
        self.assertEqual(sr.getIntervals(), [[1, 1], [3, 5], [7, 9]])

        # 9. Final interval merger
        sr.addNum(2) 
        self.assertEqual(sr.getIntervals(), [[1, 5], [7, 9]])

    # ----------------------------------
    # ## Large Input & Extreme Cases 📈
    # ----------------------------------

    def test_large_sequential_input(self):
        """Test with a large number of sequential inputs (a single long interval)."""
        N = 1000
        sr = SummaryRanges()
        for i in range(N):
            sr.addNum(i)
        
        self.assertEqual(sr.getIntervals(), [[0, N - 1]])

    def test_large_sparse_input(self):
        """Test with a large number of sparse, non-contiguous inputs."""
        N = 500
        sr = SummaryRanges()
        expected = []
        for i in range(1, N + 1):
            # Add only numbers far apart (e.g., 1, 101, 201, ...)
            sr.addNum(i * 100)
            expected.append([i * 100, i * 100])
        
        self.assertEqual(sr.getIntervals(), expected)

    def test_large_input_complex_merges(self):
        """Test a large input designed to create many small intervals that eventually merge."""
        N = 200
        sr = SummaryRanges()
        
        # Phase 1: Create N/2 intervals of length 1, separated by 2
        for i in range(N // 2):
            sr.addNum(i * 3) # 0, 3, 6, 9, ...
        
        # Phase 2: Add numbers to merge them
        for i in range(N // 2):
            sr.addNum(i * 3 + 1) # 1, 4, 7, 10, ... (forms [0, 1], [3, 4], ...)
            sr.addNum(i * 3 + 2) # 2, 5, 8, 11, ... (forms [0, 2], [3, 5], ...)

        # The final result should be one continuous interval [0, 299]
        self.assertEqual(sr.getIntervals(), [[0, (N // 2) * 3 - 1]])
        
    def test_negative_numbers(self):
        """Edge case: Test with negative and zero numbers."""
        sr = SummaryRanges()
        sr.addNum(-5)
        sr.addNum(-4)
        sr.addNum(0)
        sr.addNum(2)
        sr.addNum(3)
        sr.addNum(-3) # Merges the [-5, -4]
        
        # Numbers: -5, -4, -3, 0, 2, 3
        # Intervals: [-5, -3], [0, 0], [2, 3]
        self.assertEqual(sr.getIntervals(), [[-5, -3], [0, 0], [2, 3]])

    def test_unordered_input_and_sorting_reliance(self):
        """Test input in descending order to confirm reliance on implicit/explicit sorting."""
        sr = SummaryRanges()
        # Adding out of order: 5, 1, 3, 4, 2
        sr.addNum(5)
        sr.addNum(1)
        sr.addNum(3)
        sr.addNum(4)
        sr.addNum(2)
        # Sorted numbers: 1, 2, 3, 4, 5. Should be one interval.
        self.assertEqual(sr.getIntervals(), [[1, 5]])

if __name__ == '__main__':
    unittest.main()