import unittest


class TestLongestSubstring(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.longestSubstring("aaabb", 3), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.longestSubstring("ababbc", 2), 5)

    def test_empty_string(self):
        self.assertEqual(self.solution.longestSubstring("", 5), 0)

    def test_k_is_one(self):
        self.assertEqual(self.solution.longestSubstring("asdfghjkl", 1), 9)

    def test_k_larger_than_string_length(self):
        self.assertEqual(self.solution.longestSubstring("abc", 4), 0)

    def test_no_valid_substring(self):
        self.assertEqual(self.solution.longestSubstring("abcdefg", 2), 0)

    def test_whole_string_is_solution(self):
        self.assertEqual(self.solution.longestSubstring("ababab", 3), 6)

    def test_single_char_repeating_valid(self):
        self.assertEqual(self.solution.longestSubstring("aaaaa", 5), 5)

    def test_single_char_repeating_invalid(self):
        self.assertEqual(self.solution.longestSubstring("bbbbb", 6), 0)

    def test_multiple_splits_needed(self):
        self.assertEqual(self.solution.longestSubstring("bbaaacbd", 3), 3)

    def test_complex_string_with_nested_splits(self):
        self.assertEqual(self.solution.longestSubstring("abacbadccba", 2), 2)

    def test_long_string_no_split(self):
        s = "a" * 500 + "b" * 500
        self.assertEqual(self.solution.longestSubstring(s, 500), 1000)

    def test_long_string_one_split(self):
        s = "a" * 1000 + "b" + "c" * 900
        self.assertEqual(self.solution.longestSubstring(s, 100), 1000)

    def test_long_string_many_splits(self):
        s = "x".join(["a" * 50] * 50)
        self.assertEqual(self.solution.longestSubstring(s, 50), 50)

    def test_very_large_k(self):
        s = "a" * 1000
        self.assertEqual(self.solution.longestSubstring(s, 1001), 0)

    def test_sequential_invalid_chars(self):
        self.assertEqual(self.solution.longestSubstring("aaabbbcccdddeeeffg", 3), 15)

    def test_all_unique_characters(self):
        self.assertEqual(self.solution.longestSubstring("weitong", 2), 0)

    def test_single_character_string_k_is_one(self):
        self.assertEqual(self.solution.longestSubstring("a", 1), 1)

    def test_all_characters_valid_long(self):
        self.assertEqual(self.solution.longestSubstring("zzzyyyxxx", 3), 9)

    def test_substring_at_end(self):
        self.assertEqual(self.solution.longestSubstring("zzyyxxaabb", 2), 10)

    def test_substring_at_start(self):
        self.assertEqual(self.solution.longestSubstring("aabbccxyz", 2), 6)


if __name__ == "__main__":
    unittest.main()
