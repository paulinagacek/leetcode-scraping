import unittest


class TestLongestPalindrome(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_simple_case(self):
        self.assertEqual(self.solution.longestPalindrome("abccccdd"), 7)

    def test_single_character(self):
        self.assertEqual(self.solution.longestPalindrome("a"), 1)

    def test_already_palindrome(self):
        self.assertEqual(self.solution.longestPalindrome("racecar"), 7)

    def test_empty_string(self):
        self.assertEqual(self.solution.longestPalindrome(""), 0)

    def test_all_same_character_odd(self):
        self.assertEqual(self.solution.longestPalindrome("aaaaa"), 5)

    def test_all_same_character_even(self):
        self.assertEqual(self.solution.longestPalindrome("bbbbbb"), 6)

    def test_all_unique_characters(self):
        self.assertEqual(self.solution.longestPalindrome("abcdefg"), 1)

    def test_all_even_counts(self):
        self.assertEqual(self.solution.longestPalindrome("aabbccdd"), 8)

    def test_one_odd_count(self):
        self.assertEqual(self.solution.longestPalindrome("aabbc"), 5)

    def test_multiple_odd_counts(self):
        self.assertEqual(self.solution.longestPalindrome("bananas"), 5)

    def test_case_sensitivity(self):
        self.assertEqual(self.solution.longestPalindrome("Aa"), 1)
        self.assertEqual(self.solution.longestPalindrome("cccAAaa"), 7)
        self.assertEqual(self.solution.longestPalindrome("abA"), 1)

    def test_with_numbers_and_symbols(self):
        self.assertEqual(self.solution.longestPalindrome("123!@#123"), 7)
        self.assertEqual(self.solution.longestPalindrome("112233!@#"), 7)

    def test_long_string_with_one_odd_group(self):
        s = "a" * 500 + "b" * 499
        self.assertEqual(self.solution.longestPalindrome(s), 999)

    def test_long_string_all_even_groups(self):
        s = "a" * 1000 + "b" * 1000
        self.assertEqual(self.solution.longestPalindrome(s), 2000)

    def test_max_length_string_multiple_odd_groups(self):
        s = "a" * 1000 + "b" * 999 + "c"
        self.assertEqual(self.solution.longestPalindrome(s), 1999)

    def test_long_string_with_many_unique_chars(self):
        s = (
            "a" * 100
            + "b" * 100
            + "c" * 100
            + "".join([chr(i) for i in range(300, 500)])
        )
        self.assertEqual(self.solution.longestPalindrome(s), 301)


if __name__ == "__main__":
    unittest.main()
