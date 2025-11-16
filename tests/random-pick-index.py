import unittest


class TestSolution(unittest.TestCase):

    def test_basic_functionality(self):
        nums = [1, 2, 3, 3, 3]
        sol = Solution(nums)

        # Test for a number that appears once
        self.assertEqual(sol.pick(1), 0)
        self.assertEqual(sol.pick(2), 1)

        # Test for a number that appears multiple times
        possible_indices = {2, 3, 4}
        for _ in range(100):
            self.assertIn(sol.pick(3), possible_indices)

    def test_single_element_list(self):
        nums = [99]
        sol = Solution(nums)
        self.assertEqual(sol.pick(99), 0)

    def test_all_elements_are_the_same(self):
        nums = [5, 5, 5, 5, 5, 5]
        sol = Solution(nums)
        possible_indices = set(range(6))
        for _ in range(100):
            self.assertIn(sol.pick(5), possible_indices)

    def test_with_negative_numbers_and_zero(self):
        nums = [-1, 0, 1, 0, -1, -1]
        sol = Solution(nums)

        self.assertEqual(sol.pick(1), 2)

        possible_indices_neg_one = {0, 4, 5}
        for _ in range(100):
            self.assertIn(sol.pick(-1), possible_indices_neg_one)

        possible_indices_zero = {1, 3}
        for _ in range(100):
            self.assertIn(sol.pick(0), possible_indices_zero)

    def test_non_existent_target(self):
        nums = [1, 2, 3]
        sol = Solution(nums)
        with self.assertRaises(IndexError):
            sol.pick(4)

    def test_large_input_and_uniform_distribution(self):
        # Create a large list with a predictable pattern: 1000 occurrences for each digit 0-9
        nums = [i % 10 for i in range(10000)]
        target = 7
        sol = Solution(nums)

        valid_indices = {i for i, num in enumerate(nums) if num == target}
        self.assertEqual(len(valid_indices), 1000)

        num_picks = 50000
        counts = collections.Counter()

        # Perform the picks and check if the returned index is always valid
        for _ in range(num_picks):
            picked_index = sol.pick(target)
            self.assertIn(picked_index, valid_indices)
            counts[picked_index] += 1

        # Check that most of the possible indices were picked at least once.
        # With 50000 picks for 1000 items, it's overwhelmingly likely all are picked.
        self.assertGreater(len(counts), len(valid_indices) * 0.99)

        # Check for uniform distribution
        num_valid_indices = len(valid_indices)
        expected_count = num_picks / num_valid_indices

        # We use a statistical check. The number of hits for a specific bin
        # follows a binomial distribution. We expect counts to be within a
        # few standard deviations of the mean. 4 standard deviations is a
        # very high confidence interval (>99.9%).
        p = 1.0 / num_valid_indices
        mean = expected_count
        std_dev = (num_picks * p * (1 - p)) ** 0.5

        tolerance = 4.5 * std_dev
        lower_bound = mean - tolerance
        upper_bound = mean + tolerance

        for index in valid_indices:
            # It's possible, though extremely unlikely, that an index is never picked.
            # We only check the counts for indices that were actually picked.
            if index in counts:
                count = counts[index]
                self.assertTrue(
                    lower_bound <= count <= upper_bound,
                    f"Count for index {index} was {count}, which is outside the expected "
                    f"range [{lower_bound:.2f}, {upper_bound:.2f}] for a uniform distribution.",
                )


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
