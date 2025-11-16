import unittest


class TestCountSegments(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_string(self):
        self.assertEqual(self.solution.countSegments(""), 0)

    def test_string_with_only_spaces(self):
        self.assertEqual(self.solution.countSegments("     "), 0)

    def test_string_with_only_tabs_and_newlines(self):
        self.assertEqual(self.solution.countSegments("\t\t\n  \t\n"), 0)

    def test_simple_sentence(self):
        self.assertEqual(self.solution.countSegments("Hello, my name is John"), 5)

    def test_leading_spaces(self):
        self.assertEqual(self.solution.countSegments("    Hello World"), 2)

    def test_trailing_spaces(self):
        self.assertEqual(self.solution.countSegments("Hello World   "), 2)

    def test_leading_and_trailing_spaces(self):
        self.assertEqual(self.solution.countSegments("   Hello   World   "), 2)

    def test_multiple_spaces_between_words(self):
        self.assertEqual(self.solution.countSegments("Hello         World"), 2)

    def test_single_segment_no_spaces(self):
        self.assertEqual(self.solution.countSegments("oneword"), 1)

    def test_single_segment_with_punctuation(self):
        self.assertEqual(self.solution.countSegments("this-is-one-segment"), 1)
        self.assertEqual(self.solution.countSegments("another,one,segment"), 1)

    def test_mixed_whitespace_types(self):
        self.assertEqual(self.solution.countSegments("  \t one\n two \tthree  "), 3)

    def test_sentence_from_problem_description(self):
        self.assertEqual(
            self.solution.countSegments("The-Best-Time-to-Buy-and-Sell-Stock-II"), 1
        )
        self.assertEqual(self.solution.countSegments("                "), 0)
        self.assertEqual(self.solution.countSegments(", , , ,        a, eaefa"), 6)

    def test_long_string_many_segments(self):
        s = "word " * 5000
        self.assertEqual(self.solution.countSegments(s), 5000)

    def test_long_string_one_segment(self):
        s = "a" * 50000
        self.assertEqual(self.solution.countSegments(s), 1)

    def test_long_string_no_segments(self):
        s = " " * 50000
        self.assertEqual(self.solution.countSegments(s), 0)

    def test_long_string_alternating_words_and_spaces(self):
        s = "a  b   c    " * 1000
        self.assertEqual(self.solution.countSegments(s), 3000)


if __name__ == "__main__":
    unittest.main()
