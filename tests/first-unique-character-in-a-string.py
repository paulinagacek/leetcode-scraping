import unittest


class TestFirstUniqChar(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.firstUniqChar("leetcode"), 0)

    def test_example_2(self):
        self.assertEqual(self.solution.firstUniqChar("loveleetcode"), 2)

    def test_no_unique_char(self):
        self.assertEqual(self.solution.firstUniqChar("aabb"), -1)

    def test_empty_string(self):
        self.assertEqual(self.solution.firstUniqChar(""), -1)

    def test_all_unique_chars(self):
        self.assertEqual(self.solution.firstUniqChar("abcdefg"), 0)

    def test_all_same_chars(self):
        self.assertEqual(self.solution.firstUniqChar("zzzzzzz"), -1)

    def test_single_char_string(self):
        self.assertEqual(self.solution.firstUniqChar("a"), 0)

    def test_unique_at_end(self):
        self.assertEqual(self.solution.firstUniqChar("aabbccddeef"), 10)

    def test_unique_in_middle(self):
        self.assertEqual(self.solution.firstUniqChar("aadadafb"), 6)

    def test_case_sensitivity(self):
        # 'a' and 'A' are considered different characters
        self.assertEqual(self.solution.firstUniqChar("aAbBc"), 0)

    def test_with_numbers_and_symbols(self):
        self.assertEqual(self.solution.firstUniqChar("123123#"), 6)

    def test_long_string_no_unique(self):
        s = "a" * 50000 + "b" * 50000
        self.assertEqual(self.solution.firstUniqChar(s), -1)

    def test_long_string_unique_at_end(self):
        s = ("ab" * 25000) + "c"
        self.assertEqual(self.solution.firstUniqChar(s), 50000)

    def test_long_string_unique_at_start(self):
        s = "c" + ("ab" * 25000)
        self.assertEqual(self.solution.firstUniqChar(s), 0)

    def test_long_string_unique_in_middle(self):
        s = "a" * 25000 + "b" + "c" * 25000
        self.assertEqual(self.solution.firstUniqChar(s), 25000)


if __name__ == "__main__":
    unittest.main()
