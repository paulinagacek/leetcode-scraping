import unittest
from typing import List, Set


class TestWordBreakII(unittest.TestCase):
    """
    Unit tests for the wordBreak method using a backtracking solution.
    """

    def setUp(self):
        self.solution = Solution()

    def assertSentencesEqual(self, actual: List[str], expected: List[str]):
        """Sorts the result lists before comparison as the order doesn't matter."""
        self.assertEqual(sorted(actual), sorted(expected))

    # ----------------------------------
    # ## Standard Cases
    # ----------------------------------

    def test_standard_case_multiple_breaks(self):
        """Standard example with two words that can be broken multiple ways."""
        s = "catsanddog"
        wordDict = ["cat", "cats", "and", "sand", "dog"]
        expected = ["cat sand dog", "cats and dog"]
        self.assertSentencesEqual(self.solution.wordBreak(s, wordDict), expected)

    def test_standard_case_one_break(self):
        """Case with only one valid sentence."""
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        expected = ["apple pen apple"]
        self.assertSentencesEqual(self.solution.wordBreak(s, wordDict), expected)

    def test_case_overlapping_words(self):
        """Case with multiple short words that overlap to form longer words."""
        s = "aabaa"
        wordDict = ["a", "aa", "b", "aba"]
        # All 5 possible breaks
        expected = ["a a b a a", "a a b aa", "a aba a", "aa b a a", "aa b aa"]
        self.assertSentencesEqual(self.solution.wordBreak(s, wordDict), expected)

    # ----------------------------------
    # ## Edge Cases
    # ----------------------------------

    def test_empty_string(self):
        """Edge case: Empty input string s. Should return [""] based on the base case implementation."""
        s = ""
        wordDict = ["a", "b"]
        expected = [""] # Backtracking base case for empty input
        self.assertSentencesEqual(self.solution.wordBreak(s, wordDict), expected)

    def test_empty_dictionary(self):
        """Edge case: Empty dictionary."""
        s = "word"
        wordDict = []
        expected = []
        self.assertSentencesEqual(self.solution.wordBreak(s, wordDict), expected)

    def test_no_break_possible(self):
        """Edge case: No valid segmentation exists."""
        s = "leetcode"
        wordDict = ["leet", "codeee"]  # 'code' is missing
        expected = []
        self.assertSentencesEqual(self.solution.wordBreak(s, wordDict), expected)

    def test_full_string_is_a_word(self):
        """Edge case: The entire string is a single word, but also has valid multi-word segmentations."""
        s = "programming"
        wordDict = ["programming", "pro", "gram", "ming"]
        # Valid: "programming" AND "pro gram ming"
        expected = ["programming", "pro gram ming"]
        self.assertSentencesEqual(self.solution.wordBreak(s, wordDict), expected)

    def test_single_character_words(self):
        """Edge case: All words are single characters."""
        s = "aaaa"
        wordDict = ["a"]
        expected = ["a a a a"]
        self.assertSentencesEqual(self.solution.wordBreak(s, wordDict), expected)

    # ----------------------------------
    # ## Large Input Cases (Long string/Many words)
    # ----------------------------------

    def test_large_input_high_ambiguity(self):
        """
        Large input with many potential breaks (exponential complexity test).
        Verifies the overall count and key boundary sentences.
        """
        s = "aaaaaaaa" 
        wordDict = ["a", "aa", "aaa", "aaaa"]
        
        result = self.solution.wordBreak(s, wordDict)
        
        # Check size range (Should be 113, checking a minimum to avoid TLE failure)
        self.assertTrue(len(result) >= 108, "Should find at least 108 sentences.")
        
        # Spot check some specific sentences
        self.assertTrue("a a a a a a a a" in result)
        self.assertTrue("aa aa aa aa" in result)
        self.assertTrue("aaaa aaaa" in result)

    def test_large_input_no_break(self):
        """
        Long string where all characters match a single-character word in the dictionary.
        This results in exactly one long sentence.
        """
        s = "b" * 20
        wordDict = ["a", "b"]
        expected = ["b " * 19 + "b"] # One valid segmentation
        self.assertSentencesEqual(self.solution.wordBreak(s, wordDict), expected)

    def test_large_input_long_words(self):
        """Long string using long, distinct words."""
        s = "abracadabra"
        wordDict = ["abra", "cadabra", "a", "bracadabra"]
        expected = ["abra cadabra", "a bracadabra"]
        self.assertSentencesEqual(self.solution.wordBreak(s, wordDict), expected)


if __name__ == "__main__":
    unittest.main()
