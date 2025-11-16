import unittest


class TestMoveZeroes(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        nums = [0, 1, 0, 3, 12]
        expected = [1, 3, 12, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_empty_list(self):
        nums = []
        expected = []
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_no_zeros(self):
        nums = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_all_zeros(self):
        nums = [0, 0, 0, 0, 0]
        expected = [0, 0, 0, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_single_zero(self):
        nums = [0]
        expected = [0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_single_non_zero(self):
        nums = [1]
        expected = [1]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_zeros_already_at_end(self):
        nums = [1, 2, 3, 0, 0]
        expected = [1, 2, 3, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_zeros_at_beginning(self):
        nums = [0, 0, 0, 1, 2, 3]
        expected = [1, 2, 3, 0, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_mixed_zeros_and_non_zeros(self):
        nums = [4, 0, 2, 0, 1, 0, 3, 0]
        expected = [4, 2, 1, 3, 0, 0, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_with_negative_numbers(self):
        nums = [-1, 0, -3, 5, 0, 0, 8]
        expected = [-1, -3, 5, 8, 0, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_long_list_no_zeros(self):
        nums = list(range(1, 1001))
        expected = list(range(1, 1001))
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_long_list_all_zeros(self):
        nums = [0] * 1000
        expected = [0] * 1000
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_long_list_mixed(self):
        nums = [i if i % 5 != 0 else 0 for i in range(1000)]
        non_zeros = [x for x in nums if x != 0]
        zeros = [x for x in nums if x == 0]
        expected = non_zeros + zeros
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_long_list_alternating(self):
        nums = [i % 2 for i in range(2000)]  # Creates [0, 1, 0, 1, ...]
        expected = [1] * 1000 + [0] * 1000
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
