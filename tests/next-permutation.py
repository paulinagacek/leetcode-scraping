import unittest
from typing import List

class TestNextPermutation(unittest.TestCase):
    """
    Unit tests for the nextPermutation method of the Solution class.
    Tests verify the in-place modification of the input list.
    """

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    # ----------------------------------
    # ## Standard Cases
    # ----------------------------------

    def test_standard_case_one(self):
        """Standard case: 1, 2, 3 -> 1, 3, 2"""
        nums = [1, 2, 3]
        expected = [1, 3, 2]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, expected)

    def test_standard_case_two(self):
        """Standard case: 1, 3, 2 -> 2, 1, 3 (Pivot is 1, swap with 2, reverse [3, 2] -> [2, 3])"""
        nums = [1, 3, 2]
        expected = [2, 1, 3]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, expected)

    def test_standard_case_three(self):
        """Standard case: 6, 2, 1, 5, 4, 3, 0 -> 6, 2, 3, 0, 1, 4, 5"""
        nums = [6, 2, 1, 5, 4, 3, 0]
        expected = [6, 2, 3, 0, 1, 4, 5]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, expected)

    # ----------------------------------
    # ## Edge Cases
    # ----------------------------------

    def test_already_largest_permutation(self):
        """Edge case: Array is sorted descending, should wrap to the smallest permutation."""
        nums = [3, 2, 1]
        expected = [1, 2, 3]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, expected)

    def test_single_element(self):
        """Edge case: Array with a single element."""
        nums = [1]
        expected = [1]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, expected)
        
    def test_two_elements_next(self):
        """Edge case: Two elements, next permutation."""
        nums = [1, 5]
        expected = [5, 1]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, expected)

    def test_two_elements_wrap(self):
        """Edge case: Two elements, wrap-around."""
        nums = [5, 1]
        expected = [1, 5]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, expected)

    def test_with_duplicates(self):
        """Edge case: Array contains duplicate numbers."""
        nums = [1, 1, 5]
        expected = [1, 5, 1]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, expected)
        
    def test_duplicates_and_wrap(self):
        """Edge case: Duplicates in descending order should wrap."""
        nums = [3, 3, 2, 2, 1, 1]
        expected = [1, 1, 2, 2, 3, 3]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, expected)
        
    def test_long_suffix_decreasing(self):
        """Case where the pivot is far to the left and the suffix is long."""
        nums = [1, 9, 8, 7, 6, 5, 4, 3, 2, 0] # Pivot 1
        expected = [2, 0, 1, 3, 4, 5, 6, 7, 8, 9] # Swap 1 and 2, reverse suffix
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, expected)


    # ----------------------------------
    # ## Large Input Case
    # ----------------------------------

    def test_large_input_small_increment(self):
        """Large array, requires a small change (just the last two elements)."""
        N = 500
        # Array: [0, 1, 2, ..., 497, 498, 499] -> next is [0, 1, ..., 499, 498]
        nums = list(range(N))
        expected = list(range(N))
        expected[-1], expected[-2] = expected[-2], expected[-1] # Swap 498 and 499
        
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, expected)

    def test_large_input_wrap_around(self):
        """Large array, sorted in descending order, forcing a wrap-around."""
        N = 1000
        # Array: [999, 998, ..., 1, 0] -> next is [0, 1, ..., 999]
        nums = list(range(N - 1, -1, -1))
        expected = list(range(N))
        
        self.solution.nextPermutation(nums)
        self.assertEqual(nums, expected)

    def test_large_input_pivot_at_start(self):
        """Large array where the pivot is the first element, forcing a large reversal."""
        N = 1000
        # Array: [0, 999, 998, ..., 1] -> next is [1, 0, 999, 998, ...] -> [1, 0, 2, 3, ..., 999]
        nums = [0] + list(range(N - 1, 0, -1)) # [0, 999, 998, ..., 1]
        
        # Expected: Swap 0 with 1, then reverse the rest.
        expected = [1] + list(range(0, N - 1))[::-1] # [1, 999, 998, ..., 0] -> [1, 0, 2, 3, ..., 999]
        # More accurately: expected is [1] followed by [0, 2, 3, ..., 999] reversed.
        # Original suffix: [999, 998, ..., 1]
        # After swap: [1, 999, 998, ..., 0]
        # After reverse: [1] + [0, 1, 2, ..., 999] (reverse of [999, ..., 0])
        expected = [1] + list(range(N - 1))
        
        self.solution.nextPermutation(nums)
        # We need to manually construct the correct expected array based on the logic:
        # Initial: [0, 999, 998, ..., 1]
        # 1. i=0, nums[i]=0. 2. j=999, nums[j]=1. Swap 0 and 1.
        # After Swap: [1, 999, 998, ..., 0]
        # 3. Reverse suffix (from index i+1=1): [999, 998, ..., 0] -> [0, 1, 2, ..., 999]
        # Final: [1, 0, 2, 3, ..., 999] -> NO.
        # Final: [1, 0, 1, 2, ..., 998, 999] -> NO.
        # The correct reverse is: [1] + [0, 2, 3, ..., 999] reversed -> [1, 0, 1, 2, ..., 998] (999 elements).
        # Suffix to reverse is [999, 998, ..., 2, 0]. Reversed is [0, 2, 3, ..., 999].
        
        # Let's verify the exact array manipulation for [0, 999, 998, ..., 1]
        # Suffix is [999, 998, ..., 1]. Length 999.
        # Swap 0 and 1: [1, 999, 998, ..., 0].
        # Reverse [999, 998, ..., 0]: [0, 1, 2, ..., 999].
        # Final: [1, 0, 2, 3, ..., 999] -> This is wrong.

        # Let's use N=5 for clarity: [0, 4, 3, 2, 1]
        # 1. i=0, nums[i]=0. 2. j=4, nums[j]=1. Swap 0 and 1.
        # After Swap: [1, 4, 3, 2, 0]
        # 3. Reverse suffix (from index 1): [4, 3, 2, 0] -> [0, 2, 3, 4]
        # Final: [1, 0, 2, 3, 4]
        
        expected = [1, 0] + list(range(2, N))
        self.assertEqual(nums, expected)


if __name__ == '__main__':
    unittest.main()