import unittest


class TestTopKFrequent(unittest.TestCase):

    def setUp(self):
        """Set up a new Solution instance for each test."""
        self.solution = Solution()

    def test_leetcode_example_1(self):
        """Test the first example from LeetCode."""
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        expected = [1, 2]
        result = self.solution.topKFrequent(nums, k)
        self.assertCountEqual(result, expected, "Failed on LeetCode example 1")

    def test_leetcode_example_2(self):
        """Test the second example from LeetCode."""
        nums = [1]
        k = 1
        expected = [1]
        result = self.solution.topKFrequent(nums, k)
        self.assertCountEqual(result, expected, "Failed on LeetCode example 2")

    def test_k_is_one(self):
        """Test case where k=1."""
        nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        k = 1
        expected = [4]
        result = self.solution.topKFrequent(nums, k)
        self.assertCountEqual(result, expected, "Failed when k=1")

    def test_negative_numbers(self):
        """Test with negative numbers."""
        nums = [-1, -1, -2, -2, -2, 5, 5]
        k = 2
        expected = [-2, -1]
        result = self.solution.topKFrequent(nums, k)
        self.assertCountEqual(result, expected, "Failed with negative numbers")

    def test_with_zeros(self):
        """Test with zeros in the input."""
        nums = [0, 0, 0, 1, 1, -1]
        k = 2
        expected = [0, 1]
        result = self.solution.topKFrequent(nums, k)
        self.assertCountEqual(result, expected, "Failed with zero values")

    def test_k_equals_num_unique_elements(self):
        """Test when k is equal to the number of unique elements."""
        nums = [1, 1, 2, 2, 3, 4, 4, 4]
        k = 4
        expected = [1, 2, 3, 4]
        result = self.solution.topKFrequent(nums, k)
        self.assertCountEqual(
            result, expected, "Failed when k equals number of unique elements"
        )

    def test_frequency_tie(self):
        """Test when multiple elements have the same frequency."""
        nums = [1, 1, 2, 2, 3, 3]
        k = 3
        expected = [1, 2, 3]
        result = self.solution.topKFrequent(nums, k)
        self.assertCountEqual(result, expected, "Failed on frequency tie")

    def test_all_unique_and_k_is_len(self):
        """Test the k == len(nums) optimization path."""
        nums = [1, 2, 3, 4, 5, 6]
        k = 6
        expected = [1, 2, 3, 4, 5, 6]
        result = self.solution.topKFrequent(nums, k)
        self.assertCountEqual(result, expected, "Failed for k == len(nums) case")

    def test_all_unique_k_less_than_len(self):
        """Test with all unique elements where k < number of elements."""
        nums = [1, 2, 3, 4, 5, 6]
        k = 3
        result = self.solution.topKFrequent(nums, k)
        self.assertEqual(
            len(result), 3, "Result length is incorrect for unique elements case"
        )
        self.assertTrue(
            set(result).issubset(set(nums)),
            "Result contains elements not in original list",
        )

    def test_large_input_few_unique(self):
        """Test with a large input list but few unique elements."""
        nums = [1] * 1000 + [2] * 500 + [3] * 250 + [4] * 100
        k = 3
        expected = [1, 2, 3]
        result = self.solution.topKFrequent(nums, k)
        self.assertCountEqual(
            result, expected, "Failed on large input with few unique elements"
        )

    def test_large_input_many_unique(self):
        """Test with a large input list with many unique elements."""
        nums = list(range(10000)) + [9999] * 5 + [9998] * 4 + [9997] * 3
        k = 3
        expected = [9999, 9998, 9997]
        result = self.solution.topKFrequent(nums, k)
        self.assertCountEqual(
            result, expected, "Failed on large input with many unique elements"
        )

    def test_complex_tie_breaking(self):
        """Test a more complex tie-breaking scenario."""
        # Frequencies: 1:3, 5:2, -3:2, 2:2
        nums = [5, -3, 5, 1, 1, 1, -3, 2, 2]
        k = 3
        # Top 1 is clearly 1.
        # Top 2 and 3 are a tie between 5, -3, 2.
        # The specific result depends on implementation details of Counter and nlargest.
        result = self.solution.topKFrequent(nums, k)
        self.assertEqual(len(result), 3)
        self.assertIn(1, result)
        # Check that the other two elements are from the tied group
        tied_group = {5, -3, 2}
        result.remove(1)
        self.assertTrue(set(result).issubset(tied_group))


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
