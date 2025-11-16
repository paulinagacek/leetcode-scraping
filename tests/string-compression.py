import unittest


class TestCompress(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        expected_len = 6
        expected_chars = ["a", "2", "b", "2", "c", "3"]
        new_len = self.solution.compress(chars)
        self.assertEqual(new_len, expected_len)
        self.assertEqual(chars[:new_len], expected_chars)

    def test_single_char_group(self):
        chars = ["a"]
        expected_len = 1
        expected_chars = ["a"]
        new_len = self.solution.compress(chars)
        self.assertEqual(new_len, expected_len)
        self.assertEqual(chars[:new_len], expected_chars)

    def test_all_unique_chars(self):
        chars = ["a", "b", "c", "d", "e"]
        expected_len = 5
        expected_chars = ["a", "b", "c", "d", "e"]
        new_len = self.solution.compress(chars)
        self.assertEqual(new_len, expected_len)
        self.assertEqual(chars[:new_len], expected_chars)

    def test_all_same_chars(self):
        chars = ["z", "z", "z", "z", "z", "z", "z"]
        expected_len = 2
        expected_chars = ["z", "7"]
        new_len = self.solution.compress(chars)
        self.assertEqual(new_len, expected_len)
        self.assertEqual(chars[:new_len], expected_chars)

    def test_multi_digit_count(self):
        chars = ["a"] * 12
        expected_len = 3
        expected_chars = ["a", "1", "2"]
        new_len = self.solution.compress(chars)
        self.assertEqual(new_len, expected_len)
        self.assertEqual(chars[:new_len], expected_chars)

    def test_empty_list(self):
        chars = []
        expected_len = 0
        expected_chars = []
        new_len = self.solution.compress(chars)
        self.assertEqual(new_len, expected_len)
        self.assertEqual(chars[:new_len], expected_chars)

    def test_mixed_single_and_multi_groups(self):
        chars = ["a", "b", "b", "b", "c", "c", "d", "e", "e", "e", "e"]
        expected_len = 8
        expected_chars = ["a", "b", "3", "c", "2", "d", "e", "4"]
        new_len = self.solution.compress(chars)
        self.assertEqual(new_len, expected_len)
        self.assertEqual(chars[:new_len], expected_chars)

    def test_large_group_three_digits(self):
        chars = ["b"] * 250
        expected_len = 4
        expected_chars = ["b", "2", "5", "0"]
        new_len = self.solution.compress(chars)
        self.assertEqual(new_len, expected_len)
        self.assertEqual(chars[:new_len], expected_chars)

    def test_large_group_four_digits(self):
        chars = ["x"] * 1000
        expected_len = 5
        expected_chars = ["x", "1", "0", "0", "0"]
        new_len = self.solution.compress(chars)
        self.assertEqual(new_len, expected_len)
        self.assertEqual(chars[:new_len], expected_chars)

    def test_long_input_with_multiple_large_groups(self):
        chars = ["a"] * 500 + ["b"] * 750 + ["c"] * 1000
        expected_len = (1 + 3) + (1 + 3) + (1 + 4)
        expected_chars = list("a500b750c1000")
        new_len = self.solution.compress(chars)
        self.assertEqual(new_len, expected_len)
        self.assertEqual(chars[:new_len], expected_chars)

    def test_long_input_with_many_small_groups(self):
        chars = []
        expected_chars = []
        for char_code in range(ord("a"), ord("z") + 1):
            char = chr(char_code)
            count = (char_code - ord("a")) + 2
            chars.extend([char] * count)
            expected_chars.append(char)
            if count > 1:
                expected_chars.extend(list(str(count)))

        expected_len = len(expected_chars)
        new_len = self.solution.compress(chars)
        self.assertEqual(new_len, expected_len)
        self.assertEqual(chars[:new_len], expected_chars)

    def test_long_input_alternating_chars(self):
        chars = []
        for _ in range(1000):
            chars.extend(["a", "b"])
        expected_len = 2000
        expected_chars = chars[:]
        new_len = self.solution.compress(chars)
        self.assertEqual(new_len, expected_len)
        self.assertEqual(chars[:new_len], expected_chars)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
