import unittest
from typing import List

class TestLongestCommonPrefix(unittest.TestCase):
    """
    Unit tests for the longestCommonPrefix method of the Solution class.
    Tests cover standard inputs, edge cases (empty list, empty strings, 
    no common prefix, long prefix), and a large input.
    """

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    # ----------------------------------
    # ## Standard Cases
    # ----------------------------------

    def test_standard_case_one(self):
        """Case with a common prefix 'fl'."""
        strs = ["flower", "flow", "flight"]
        expected = "fl"
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)

    def test_standard_case_two_no_common_prefix(self):
        """Case where there is no common prefix."""
        strs = ["dog", "racecar", "car"]
        expected = ""
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)

    def test_standard_case_three_full_string_prefix(self):
        """Case where one string is a prefix of all others."""
        strs = ["apple", "appletree", "application"]
        expected = "appl"
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)
        
    def test_standard_case_four_single_letter_prefix(self):
        """Case where the prefix is just one character."""
        strs = ["a", "b"]
        expected = ""
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)

    # ----------------------------------
    # ## Edge Cases
    # ----------------------------------

    def test_empty_list(self):
        """The smallest possible input: an empty list of strings."""
        strs = []
        expected = ""
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)

    def test_list_with_one_string(self):
        """List containing only one string."""
        strs = ["hello"]
        expected = "hello"
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)

    def test_contains_empty_string(self):
        """List contains an empty string, forcing the result to be empty."""
        strs = ["flower", "", "flight"]
        expected = ""
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)
        
    def test_all_empty_strings(self):
        """List where all strings are empty."""
        strs = ["", "", ""]
        expected = ""
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)

    def test_identical_strings(self):
        """List where all strings are identical."""
        strs = ["test", "test", "test", "test"]
        expected = "test"
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)

    def test_all_mismatch_at_first_char(self):
        """Strings mismatch immediately at the first character."""
        strs = ["zpple", "a", "b"]
        expected = ""
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)

    # ----------------------------------
    # ## Large Input Case
    # ----------------------------------

    def test_large_input_long_prefix(self):
        """Test with a large number of long strings with a long prefix."""
        N = 1000  # Number of strings
        L = 500   # Length of the common prefix
        
        long_prefix = "a" * L
        
        # Create a list where the first N-1 strings share the long prefix
        strs = [long_prefix + str(i) for i in range(N - 1)]
        
        # The last string is just the long prefix
        strs.append(long_prefix)
        
        expected = long_prefix
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)

    def test_large_input_prefix_is_one_char(self):
        """Test with a large number of strings, where the prefix is just one character."""
        N = 1000
        strs = ["a" * 1000] # Starts with "a"
        strs.extend(["a" + "b" * 999] * (N - 1)) # Also starts with "a"
        
        expected = "a"
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)
        
    def test_large_input_no_prefix(self):
        """Test with a large number of strings where there is no common prefix."""
        N = 1000
        strs = ["b" * 1000] * (N - 1)
        strs.append("a" * 1000)
        
        expected = ""
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)


if __name__ == '__main__':
    unittest.main()