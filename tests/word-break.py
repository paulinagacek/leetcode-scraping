import unittest
from collections import deque
from typing import List, Set

class TestWordBreak(unittest.TestCase):
    """
    Unit tests for the wordBreak method using the BFS solution.
    """

    def setUp(self):
        self.solution = Solution()

    # ----------------------------------
    # ## Standard Cases
    # ----------------------------------

    def test_standard_case_true(self):
        """Standard true case: s can be segmented."""
        s = "leetcode"
        wordDict = ["leet", "code"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_standard_case_false(self):
        """Standard false case: s cannot be segmented."""
        s = "applepie"
        wordDict = ["apple", "pen"]
        self.assertFalse(self.solution.wordBreak(s, wordDict))
        
    def test_overlapping_words_true(self):
        """Case with overlapping words and different lengths."""
        s = "catsandog"
        wordDict = ["cat", "cats", "and", "sand", "dog"]
        self.assertFalse(self.solution.wordBreak(s, wordDict)) # cats | and | dog

    def test_repeated_words_true(self):
        """Case where a word is repeated."""
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    # ----------------------------------
    # ## Edge Cases
    # ----------------------------------

    def test_empty_string(self):
        """Edge case: Empty input string s."""
        s = ""
        wordDict = ["a", "b"]
        self.assertTrue(self.solution.wordBreak(s, wordDict)) # Empty string is always a valid "break"

    def test_empty_dictionary(self):
        """Edge case: Empty dictionary."""
        s = "word"
        wordDict = []
        self.assertFalse(self.solution.wordBreak(s, wordDict))

    def test_single_character_words(self):
        """Edge case: All single-character words."""
        s = "aaaaa"
        wordDict = ["a", "aa"]
        self.assertTrue(self.solution.wordBreak(s, wordDict))

    def test_dictionary_superset(self):
        """Edge case: Dictionary contains longer words not used for the break."""
        s = "abc"
        wordDict = ["a", "b", "c", "abcde"]
        self.assertTrue(self.solution.wordBreak(s, wordDict)) # a | b | c

    def test_leading_failing_branch(self):
        """Case where a long, failing path must be correctly seen/memoized."""
        s = "aaaaab"
        wordDict = ["a", "aa", "aaa", "b"]
        # aaaaa (fails)
        self.assertTrue(self.solution.wordBreak(s, wordDict)) # a | a | a | a | a | b

    def test_long_failing_path_must_be_pruned(self):
        """Case designed to show the benefit of the 'seen' set."""
        s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
        # Length 150 'a's followed by 'b'
        wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaab"]
        # The only way to succeed is by matching the last word 'aaaaaaab', 
        # but the BFS will explore many "a|a|a|..." paths first.
        self.assertTrue(self.solution.wordBreak(s, wordDict))


    # ----------------------------------
    # ## Large Input Cases
    # ----------------------------------

    def test_large_input_true_case(self):
        """Long string where segmentation is possible."""
        s = "dataandstructure"
        wordDict = ["data", "and", "structure", "dat", "a"]
        self.assertTrue(self.solution.wordBreak(s, wordDict)) # data | and | structure

    def test_large_input_false_case(self):
        """
        Long string where many prefixes match but the end fails, testing 
        the effectiveness of the BFS and `seen` set (similar to DP).
        """
        # 30 'a's, followed by 'b'
        s = "a" * 30 + "b"
        wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa"]
        # All segmentations fail because 'b' cannot be matched.
        self.assertFalse(self.solution.wordBreak(s, wordDict))

    def test_large_input_complex_true(self):
        """Case with high ambiguity that resolves to True."""
        s = "carsarefastandreliable"
        wordDict = ["car", "cars", "are", "fast", "and", "relia", "ble", "reliable"]
        self.assertTrue(self.solution.wordBreak(s, wordDict)) # cars | are | fast | and | reliable


if __name__ == '__main__':
    unittest.main()