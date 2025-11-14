import unittest
from typing import List

class TestRegularExpressionMatching(unittest.TestCase):
    """
    Unit tests for the isMatch method of the Solution class.
    Tests verify the correct application of '.' and '*'.
    """

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    # ----------------------------------
    # ## Standard Cases
    # ----------------------------------

    def test_standard_case_no_wildcards(self):
        """Simple exact match."""
        self.assertTrue(self.solution.isMatch("abc", "abc"))
        self.assertFalse(self.solution.isMatch("aab", "abc"))

    def test_dot_wildcard(self):
        """Use of the '.' wildcard."""
        self.assertTrue(self.solution.isMatch("aab", "a.b"))
        self.assertFalse(self.solution.isMatch("aab", "b.b"))

    def test_star_wildcard_zero_matches(self):
        """Use of '*' matching zero occurrences."""
        self.assertTrue(self.solution.isMatch("ab", "a*ab")) # 'a*' matches zero 'a's
        self.assertTrue(self.solution.isMatch("b", "a*b"))    # 'a*' matches zero 'a's
        
    def test_star_wildcard_one_match(self):
        """Use of '*' matching one occurrence."""
        self.assertTrue(self.solution.isMatch("aab", "a*b")) # 'a*' matches one 'a'
        
    def test_star_wildcard_multiple_matches(self):
        """Use of '*' matching multiple occurrences."""
        self.assertTrue(self.solution.isMatch("aaab", "a*b")) # 'a*' matches two 'a's

    def test_dot_star_wildcard(self):
        """Use of '.*' matching any sequence."""
        self.assertTrue(self.solution.isMatch("mississippi", "mis*is*ip*."))
        self.assertTrue(self.solution.isMatch("a", ".*"))
        self.assertTrue(self.solution.isMatch("abcdefg", ".*"))

    # ----------------------------------
    # ## Edge Cases
    # ----------------------------------

    def test_empty_string_and_pattern(self):
        """Empty text and empty pattern."""
        self.assertTrue(self.solution.isMatch("", ""))

    def test_empty_text_non_empty_pattern(self):
        """Empty text should only match patterns that consume zero characters."""
        self.assertFalse(self.solution.isMatch("", "a"))
        self.assertTrue(self.solution.isMatch("", "a*"))
        self.assertTrue(self.solution.isMatch("", ".*"))
        self.assertTrue(self.solution.isMatch("", "a*b*"))

    def test_non_empty_text_empty_pattern(self):
        """Non-empty text cannot match an empty pattern."""
        self.assertFalse(self.solution.isMatch("a", ""))

    def test_multiple_stars(self):
        """Pattern with sequential stars."""
        self.assertTrue(self.solution.isMatch("aabc", "a*a*b*c"))
        self.assertTrue(self.solution.isMatch("ab", "a*b*"))
        self.assertTrue(self.solution.isMatch("aaa", "a*b*"))
        
    def test_complex_zero_match(self):
        """Complex scenario where many '*' must match zero."""
        self.assertTrue(self.solution.isMatch("b", "c*b*d*b"))

    def test_partial_match_fail(self):
        """Pattern must match the whole string."""
        self.assertFalse(self.solution.isMatch("aa", "a"))
        self.assertFalse(self.solution.isMatch("mississippi", "mis*is*p*."))

    # ----------------------------------
    # ## Large Input Cases (Testing performance limit of non-memoized recursion)
    # ----------------------------------

    def test_large_input_full_match(self):
        """Large text and pattern with simple wildcards."""
        N = 20  # Keep N small as the O(2^(M+N)) complexity will stack overflow/timeout quickly
        text = "a" * N
        pattern = "a" * N
        self.assertTrue(self.solution.isMatch(text, pattern))

    def test_large_input_star_match_all(self):
        """Large text matched by '.*'."""
        N = 20
        text = "a" * N
        pattern = ".*"
        self.assertTrue(self.solution.isMatch(text, pattern))

    def test_large_input_complex_match(self):
        """Large text with a complex star match at the end."""
        N = 20
        text = "b" + "a" * N + "b"
        # Pattern: 'b' followed by 20 'a's, matched by 'a*', followed by 'b'
        pattern = "b" + "a*" * 5 + "b"
        self.assertTrue(self.solution.isMatch(text, pattern))

    def test_large_input_failure(self):
        """Large input that should fail clearly."""
        N = 20
        text = "a" * N
        pattern = "b" * N
        self.assertFalse(self.solution.isMatch(text, pattern))


if __name__ == '__main__':
    # Due to the non-memoized recursive structure, increase recursion limit for stability
    # on larger test cases (like N=20).
    import sys
    sys.setrecursionlimit(2000)
    unittest.main()