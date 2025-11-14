import unittest
from typing import List

class TestFindMedianSortedArrays(unittest.TestCase):
    """
    Unit tests for the findMedianSortedArrays method.
    """

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    # Helper function for floating point comparison
    def assertFloatEqual(self, actual: float, expected: float):
        """Custom assertion for floats with a tolerance."""
        self.assertAlmostEqual(actual, expected, places=5)

    # ----------------------------------
    # ## Standard Cases
    # ----------------------------------

    def test_odd_length_different_arrays(self):
        """Odd total length, elements interleaved."""
        nums1 = [1, 3]
        nums2 = [2]
        expected = 2.0
        self.assertFloatEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)

    def test_even_length_different_arrays(self):
        """Even total length, elements interleaved."""
        nums1 = [1, 2]
        nums2 = [3, 4]
        expected = 2.5  # (2 + 3) / 2
        self.assertFloatEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)

    def test_one_array_before_other(self):
        """Elements of one array are entirely smaller than the other."""
        nums1 = [1, 5]
        nums2 = [10, 15]
        expected = 7.5  # (5 + 10) / 2
        self.assertFloatEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)

    def test_duplicates(self):
        """Arrays containing duplicate values."""
        nums1 = [1, 1, 3, 5]
        nums2 = [2, 2, 4, 6]
        expected = 2.5  # Merged: [1, 1, 2, 2, 3, 4, 5, 6]. Median: (2 + 3) / 2
        self.assertFloatEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)

    # ----------------------------------
    # ## Edge Cases
    # ----------------------------------

    def test_one_empty_array(self):
        """One array is empty."""
        nums1 = [1, 2, 3, 4, 5]
        nums2 = []
        expected = 3.0
        self.assertFloatEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)

    def test_second_empty_array(self):
        """The other array is empty."""
        nums1 = []
        nums2 = [10, 20]
        expected = 15.0
        self.assertFloatEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)

    def test_single_element_arrays(self):
        """Both arrays have a single element."""
        nums1 = [5]
        nums2 = [10]
        expected = 7.5
        self.assertFloatEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)

    def test_max_min_integers(self):
        """Test with Python's large/small integer limits (implicitly handled)."""
        nums1 = [-2**31, 0]
        nums2 = [1, 2**31 - 1]
        expected = 0.5  # Merged: [-2**31, 0, 1, 2**31 - 1]. Median: (0 + 1) / 2
        self.assertFloatEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)

    def test_very_long_overlap(self):
        """Arrays with similar values to test pointer handling."""
        nums1 = [1, 2, 3, 4, 5, 6, 7]
        nums2 = [3, 4, 5, 6, 7, 8, 9]
        # Merged: [1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 9]. N=14. Median: (5 + 5) / 2
        expected = 5.0
        self.assertFloatEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)


    # ----------------------------------
    # ## Large Input Cases
    # ----------------------------------

    def test_large_input_skewed_median(self):
        """Large arrays where the median comes from the larger array."""
        N1 = 1000
        N2 = 1001
        nums1 = list(range(1, N1 + 1))  # [1, ..., 1000]
        nums2 = list(range(N1 + 1, N1 + N2 + 1))  # [1001, ..., 2001]
        
        # Total length: 2001 (Odd). Median is the 1001st element (0-indexed 1000).
        # This is nums2[0], which is 1001.
        expected = 1001.0
        self.assertFloatEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)

    def test_large_input_median_from_both(self):
        """Large arrays where the median is the average of elements from both arrays."""
        N = 1000
        nums1 = list(range(1, N + 1))  # [1, ..., 1000]
        # Shift nums2 to get the median from the overlap
        nums2 = [i + N // 2 for i in range(1, N + 1)] # [501, ..., 1500]
        expected = 750.5
        self.assertFloatEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)

if __name__ == '__main__':
    unittest.main()