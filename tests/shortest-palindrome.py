import unittest


class TestShortestPalindrome(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_empty_string(self):
        self.assertEqual(self.solution.shortestPalindrome(""), "")

    def test_single_char_string(self):
        self.assertEqual(self.solution.shortestPalindrome("a"), "a")

    def test_already_palindrome(self):
        self.assertEqual(self.solution.shortestPalindrome("aa"), "aa")
        self.assertEqual(self.solution.shortestPalindrome("aba"), "aba")
        self.assertEqual(self.solution.shortestPalindrome("racecar"), "racecar")
        self.assertEqual(self.solution.shortestPalindrome("madam"), "madam")

    def test_simple_non_palindrome(self):
        self.assertEqual(self.solution.shortestPalindrome("ab"), "bab")
        self.assertEqual(self.solution.shortestPalindrome("abc"), "cbabc")
        self.assertEqual(self.solution.shortestPalindrome("abcd"), "dcbabcd")

    def test_leet_code_examples(self):
        self.assertEqual(self.solution.shortestPalindrome("aacecaaa"), "aaacecaaa")
        self.assertEqual(self.solution.shortestPalindrome("abcd"), "dcbabcd")

    def test_with_palindromic_prefix(self):
        self.assertEqual(self.solution.shortestPalindrome("abbacd"), "dcabbacd")
        self.assertEqual(self.solution.shortestPalindrome("abab"), "babab")
        self.assertEqual(self.solution.shortestPalindrome("google"), "elgoogle")
        self.assertEqual(
            self.solution.shortestPalindrome("ananana"), "ananana"
        )  # longest prefix is 'ana'

    def test_long_input_already_palindrome(self):
        s = "a" * 50000
        self.assertEqual(self.solution.shortestPalindrome(s), s)
        s = "abacaba" * 5000
        self.assertEqual(self.solution.shortestPalindrome(s), s)

    def test_long_input_no_palindromic_prefix(self):
        s = "a" + "b" * 49999
        expected = "b" * 49999 + s
        self.assertEqual(self.solution.shortestPalindrome(s), expected)

    def test_long_input_alternating(self):
        s = "ab" * 25000
        expected = "b" + s
        self.assertEqual(self.solution.shortestPalindrome(s), expected)

    def test_long_input_with_long_palindromic_prefix(self):
        prefix = "a" * 49998
        s = prefix + "bc"
        expected = "cb" + s
        self.assertEqual(self.solution.shortestPalindrome(s), expected)

    def test_long_input_with_complex_prefix(self):
        prefix = "ab" * 20000 + "a"
        s = prefix + "xyz"
        expected = "zyx" + s
        self.assertEqual(self.solution.shortestPalindrome(s), expected)


if __name__ == "__main__":
    unittest.main()
