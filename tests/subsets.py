import unittest
from typing import List


class TestSubsets(unittest.TestCase):
    """
    Unit tests for the subsets method of the Solution class.
    Tests cover standard inputs, edge cases, and large inputs.
    """

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    def assertSubsetsEqual(self, actual: List[List[int]], expected: List[List[int]]):
        """
        Custom assertion to check if two lists of subsets are equal,
        regardless of the order of subsets (outer list) and the order of elements
        within each subset (inner list).

        Note: The canonical solution maintains element order, but for robustness
        and general adherence to power set properties, we'll sort the subsets
        themselves for comparison.
        """

        # 1. Sort elements within each subset
        actual_sorted_inner = [sorted(s) for s in actual]
        expected_sorted_inner = [sorted(s) for s in expected]

        # 2. Sort the list of subsets (based on their content)
        # Using tuple(s) allows sorting a list of lists/subsets
        actual_sorted = sorted(actual_sorted_inner, key=lambda s: tuple(s))
        expected_sorted = sorted(expected_sorted_inner, key=lambda s: tuple(s))

        self.assertEqual(actual_sorted, expected_sorted)

    # ----------------------------------
    # ## Standard Cases
    # ----------------------------------

    def test_standard_case_n3(self):
        """Standard case with 3 elements, generating 8 subsets."""
        nums = [1, 2, 3]
        expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
        self.assertSubsetsEqual(self.solution.subsets(nums), expected)

    def test_standard_case_n4(self):
        """Standard case with 4 elements, generating 16 subsets."""
        nums = [4, 1, 0, 2]
        expected = [
            [],
            [4],
            [1],
            [0],
            [2],
            [4, 1],
            [4, 0],
            [4, 2],
            [1, 0],
            [1, 2],
            [0, 2],
            [4, 1, 0],
            [4, 1, 2],
            [4, 0, 2],
            [1, 0, 2],
            [4, 1, 0, 2],
        ]
        self.assertSubsetsEqual(self.solution.subsets(nums), expected)

    # ----------------------------------
    # ## Edge Cases
    # ----------------------------------

    def test_empty_list(self):
        """Edge case: Empty input list."""
        nums = []
        expected = [[]]
        self.assertSubsetsEqual(self.solution.subsets(nums), expected)

    def test_single_element(self):
        """Edge case: Single element input."""
        nums = [7]
        expected = [[], [7]]
        self.assertSubsetsEqual(self.solution.subsets(nums), expected)

    def test_negative_numbers(self):
        """Case with negative numbers."""
        nums = [-1, 0, 1]
        expected = [[], [-1], [0], [1], [-1, 0], [-1, 1], [0, 1], [-1, 0, 1]]
        self.assertSubsetsEqual(self.solution.subsets(nums), expected)

    def test_list_with_zero(self):
        """Case with zero as a single element."""
        nums = [0]
        expected = [[], [0]]
        self.assertSubsetsEqual(self.solution.subsets(nums), expected)

    # ----------------------------------
    # ## Large Input Cases
    # ----------------------------------

    def test_large_input_n10(self):
        """
        Large input (N=10). Total of 2^10 = 1024 subsets.
        We verify the count and a few boundary subsets.
        """
        n = 10
        nums = list(range(n))  # [0, 1, ..., 9]
        result = self.solution.subsets(nums)

        # 1. Check the count (2^N)
        self.assertEqual(len(result), 2**n)

        # 2. Check the empty set
        self.assertTrue([] in result)

        # 3. Check single-element subsets
        for i in range(n):
            self.assertTrue([i] in result)

        # 4. Check the full set
        self.assertTrue(nums in result)

        # 5. Check a specific large subset (e.g., all evens)
        all_evens = [i for i in nums if i % 2 == 0]
        self.assertTrue(all_evens in result)

        # 6. Check a specific subset with a known structure (e.g., all but the last)
        all_but_last = nums[:-1]
        self.assertTrue(all_but_last in result)


if __name__ == "__main__":
    unittest.main()
