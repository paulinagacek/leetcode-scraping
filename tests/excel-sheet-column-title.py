import unittest


class TestConvertToTitle(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_single_letter_start(self):
        self.assertEqual(self.solution.convertToTitle(1), "A")

    def test_single_letter_middle(self):
        self.assertEqual(self.solution.convertToTitle(13), "M")

    def test_single_letter_end(self):
        self.assertEqual(self.solution.convertToTitle(26), "Z")

    def test_two_letters_start(self):
        self.assertEqual(self.solution.convertToTitle(27), "AA")

    def test_two_letters_second(self):
        self.assertEqual(self.solution.convertToTitle(28), "AB")

    def test_two_letters_end_of_first_char(self):
        self.assertEqual(self.solution.convertToTitle(52), "AZ")

    def test_two_letters_start_of_second_char(self):
        self.assertEqual(self.solution.convertToTitle(53), "BA")

    def test_leetcode_example(self):
        self.assertEqual(self.solution.convertToTitle(701), "ZY")

    def test_two_letters_end(self):
        self.assertEqual(self.solution.convertToTitle(702), "ZZ")

    def test_three_letters_start(self):
        self.assertEqual(self.solution.convertToTitle(703), "AAA")

    def test_three_letters_middle(self):
        self.assertEqual(self.solution.convertToTitle(704), "AAB")

    def test_three_letters_end(self):
        self.assertEqual(self.solution.convertToTitle(18278), "ZZZ")

    def test_four_letters_start(self):
        self.assertEqual(self.solution.convertToTitle(18279), "AAAA")

    def test_large_number(self):
        self.assertEqual(self.solution.convertToTitle(534645), "ADJWG")

    def test_very_large_number(self):
        self.assertEqual(self.solution.convertToTitle(2147483647), "FXSHRXW")


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
