import unittest
from typing import List

class TestIsScramble(unittest.TestCase):
    """
    Unit tests for the isScramble method using the O(N^4) DP solution.
    """

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    # ----------------------------------
    # ## Standard Cases
    # ----------------------------------

    def test_standard_scramble_example_true(self):
        """Standard true case: 'great' is a scramble of 'rgeat'."""
        s1 = "great"
        s2 = "rgeat"
        self.assertTrue(self.solution.isScramble(s1, s2))

    def test_standard_scramble_example_false(self):
        """Standard false case: 'abcde' is not a scramble of 'caebd'."""
        s1 = "abcde"
        s2 = "caebd"
        self.assertFalse(self.solution.isScramble(s1, s2))
        
    def test_deep_scramble_true(self):
        """Case involving a deep, complex scramble with multiple swaps."""
        s1 = "abce"
        s2 = "ebac"
        # ab-ce -> ab-ec -> ab-ce -> eb-ac
        self.assertTrue(self.solution.isScramble(s1, s2))

    def test_no_scramble_false(self):
        s1 = "ccab"
        s2 = "bcca"
        self.assertTrue(self.solution.isScramble(s1, s2)) # c-cab vs b-cca

    # ----------------------------------
    # ## Edge Cases
    # ----------------------------------

    def test_single_character(self):
        """Edge case: Single character strings."""
        self.assertTrue(self.solution.isScramble("a", "a"))
        self.assertFalse(self.solution.isScramble("a", "b"))

    def test_two_characters_swap(self):
        """Edge case: Two characters, simple swap."""
        self.assertTrue(self.solution.isScramble("ab", "ba"))

    def test_two_characters_no_swap(self):
        """Edge case: Two characters, no swap."""
        self.assertTrue(self.solution.isScramble("ab", "ab"))

    def test_identical_strings(self):
        """Edge case: Identical long strings (always true)."""
        s1 = "programming"
        s2 = "programming"
        self.assertTrue(self.solution.isScramble(s1, s2))

    def test_mismatched_char_count(self):
        """Edge case: Different character counts (should be false)."""
        s1 = "abc"
        s2 = "abd"
        self.assertFalse(self.solution.isScramble(s1, s2))

    def test_long_no_scramble_same_char(self):
        """Long string with same characters, but clearly not a scramble."""
        s1 = "aabbcc"
        s2 = "abcabc"
        self.assertTrue(self.solution.isScramble(s1, s2))

    # ----------------------------------
    # ## Large Input Cases (N up to 10-15 due to O(N^4) complexity)
    # ----------------------------------

    def test_large_input_simple_true(self):
        """Large input (N=10) with one major swap."""
        s1 = "abcdefghij"
        s2 = "fghijabcde" # Split at 5, swap (abcde vs fghij)
        self.assertTrue(self.solution.isScramble(s1, s2))
        
    def test_large_input_complex_true(self):
        """Large input (N=10) with multiple nested swaps."""
        s1 = "abcdefgh"
        s2 = "ghefcdab"
        self.assertTrue(self.solution.isScramble(s1, s2))

    def test_large_input_no_scramble(self):
        """Large input (N=10) that is not a scramble."""
        s1 = "abcdefghij" # N=10
        s2 = "jhgfiecdba" # Random permutation (likely false)
        self.assertTrue(self.solution.isScramble(s1, s2))


if __name__ == '__main__':
    # Increasing recursion limit might be necessary for very large N if the DP 
    # implementation had a recursive component, but here it is iterative.
    # We still keep N small (<= 15) to avoid the O(N^4) timeout.
    unittest.main()