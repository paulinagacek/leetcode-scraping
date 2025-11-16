import unittest
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        sumOfCurrentWindow = 0
        res = float("inf")

        for right in range(0, len(nums)):
            sumOfCurrentWindow += nums[right]

            while sumOfCurrentWindow >= target:
                res = min(res, right - left + 1)
                sumOfCurrentWindow -= nums[left]
                left += 1

        return res if res != float("inf") else 0


class TestMinSubArrayLen(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        target = 7
        nums = [2, 3, 1, 2, 4, 3]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 2)

    def test_example_2(self):
        target = 4
        nums = [1, 4, 4]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 1)

    def test_no_solution(self):
        target = 11
        nums = [1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 0)

    def test_empty_array(self):
        target = 5
        nums = []
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 0)

    def test_single_element_array_match(self):
        target = 5
        nums = [5]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 1)

    def test_single_element_array_no_match(self):
        target = 6
        nums = [5]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 0)

    def test_entire_array_is_exact_solution(self):
        target = 15
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 5)

    def test_entire_array_is_minimal_solution(self):
        target = 14
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 4)

    def test_solution_at_the_end(self):
        target = 10
        nums = [1, 1, 1, 1, 1, 1, 1, 1, 5, 5]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 2)

    def test_complex_window_movement(self):
        target = 15
        nums = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 2)

    def test_large_target_single_element(self):
        target = 10**9
        nums = [10**9, 1, 2, 3]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 1)

    def test_large_input_all_ones_match(self):
        target = 100000
        nums = [1] * 100000
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 100000)

    def test_large_input_all_ones_no_match(self):
        target = 100001
        nums = [1] * 100000
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 0)

    def test_large_input_early_solution(self):
        target = 50
        nums = [50] + [1] * 99999
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 1)

    def test_large_input_late_solution(self):
        target = 50
        nums = [1] * 99999 + [50]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 1)

    def test_large_numbers_in_array(self):
        target = 2000
        nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1001]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 3)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
