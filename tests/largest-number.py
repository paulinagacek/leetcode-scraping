import unittest


class TestLargestNumber(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.largestNumber([10, 2]), "210")

    def test_example_2(self):
        self.assertEqual(self.solution.largestNumber([3, 30, 34, 5, 9]), "9534330")

    def test_all_zeros(self):
        self.assertEqual(self.solution.largestNumber([0, 0, 0]), "0")

    def test_single_zero(self):
        self.assertEqual(self.solution.largestNumber([0]), "0")

    def test_single_non_zero_digit(self):
        self.assertEqual(self.solution.largestNumber([8]), "8")

    def test_tricky_prefix_case_1(self):
        self.assertEqual(self.solution.largestNumber([121, 12]), "12121")

    def test_tricky_prefix_case_2(self):
        self.assertEqual(self.solution.largestNumber([1, 10, 100]), "110100")

    def test_tricky_prefix_case_3(self):
        self.assertEqual(self.solution.largestNumber([432, 43243]), "43243432")

    def test_tricky_prefix_case_4(self):
        self.assertEqual(self.solution.largestNumber([111311, 1113]), "1113111311")

    def test_complex_order(self):
        self.assertEqual(self.solution.largestNumber([4, 40, 41, 45]), "4544140")

    def test_identical_numbers(self):
        self.assertEqual(self.solution.largestNumber([5, 5, 5]), "555")

    def test_mixed_with_zeros(self):
        self.assertEqual(self.solution.largestNumber([1, 0, 2, 0]), "2100")

    def test_large_numbers(self):
        self.assertEqual(
            self.solution.largestNumber([999999999, 9, 98]), "999999999998"
        )

    def test_large_input_list_identical(self):
        nums = [1] * 100
        expected = "1" * 100
        self.assertEqual(self.solution.largestNumber(nums), expected)

    def test_large_input_single_digits(self):
        nums = list(range(10))
        self.assertEqual(self.solution.largestNumber(nums), "9876543210")

    def test_another_large_number_case(self):
        nums = [i for i in range(99, -1, -1)]
        # This is hard to predict, but we can verify against a known correct implementation
        # The standard comparison `cmp(b+a, a+b)` should be used
        import functools

        def compare_func(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        num_strings = sorted(
            [str(n) for n in nums], key=functools.cmp_to_key(compare_func)
        )
        expected = "".join(num_strings)
        self.assertEqual(self.solution.largestNumber(nums), expected)


if __name__ == "__main__":
    unittest.main()
