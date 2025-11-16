import unittest


class TestNumberToWords(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_zero(self):
        self.assertEqual(self.solution.numberToWords(0), "Zero")

    def test_single_digits(self):
        self.assertEqual(self.solution.numberToWords(1), "One")
        self.assertEqual(self.solution.numberToWords(8), "Eight")

    def test_teens(self):
        self.assertEqual(self.solution.numberToWords(10), "Ten")
        self.assertEqual(self.solution.numberToWords(13), "Thirteen")
        self.assertEqual(self.solution.numberToWords(19), "Nineteen")

    def test_tens(self):
        self.assertEqual(self.solution.numberToWords(20), "Twenty")
        self.assertEqual(self.solution.numberToWords(55), "Fifty Five")
        self.assertEqual(self.solution.numberToWords(99), "Ninety Nine")

    def test_hundreds(self):
        self.assertEqual(self.solution.numberToWords(100), "One Hundred")
        self.assertEqual(self.solution.numberToWords(101), "One Hundred One")
        self.assertEqual(self.solution.numberToWords(110), "One Hundred Ten")
        self.assertEqual(self.solution.numberToWords(123), "One Hundred Twenty Three")
        self.assertEqual(self.solution.numberToWords(999), "Nine Hundred Ninety Nine")

    def test_thousands(self):
        self.assertEqual(self.solution.numberToWords(1000), "One Thousand")
        self.assertEqual(self.solution.numberToWords(1001), "One Thousand One")
        self.assertEqual(
            self.solution.numberToWords(2345), "Two Thousand Three Hundred Forty Five"
        )
        self.assertEqual(self.solution.numberToWords(10000), "Ten Thousand")
        self.assertEqual(
            self.solution.numberToWords(54321),
            "Fifty Four Thousand Three Hundred Twenty One",
        )
        self.assertEqual(self.solution.numberToWords(100000), "One Hundred Thousand")
        self.assertEqual(
            self.solution.numberToWords(123456),
            "One Hundred Twenty Three Thousand Four Hundred Fifty Six",
        )
        self.assertEqual(
            self.solution.numberToWords(999999),
            "Nine Hundred Ninety Nine Thousand Nine Hundred Ninety Nine",
        )

    def test_millions(self):
        self.assertEqual(self.solution.numberToWords(1000000), "One Million")
        self.assertEqual(self.solution.numberToWords(1000001), "One Million One")
        self.assertEqual(
            self.solution.numberToWords(1001000), "One Million One Thousand"
        )
        self.assertEqual(
            self.solution.numberToWords(1234567),
            "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven",
        )
        self.assertEqual(
            self.solution.numberToWords(101101101),
            "One Hundred One Million One Hundred One Thousand One Hundred One",
        )
        self.assertEqual(
            self.solution.numberToWords(999999999),
            "Nine Hundred Ninety Nine Million Nine Hundred Ninety Nine Thousand Nine Hundred Ninety Nine",
        )

    def test_billions(self):
        self.assertEqual(self.solution.numberToWords(1000000000), "One Billion")
        self.assertEqual(self.solution.numberToWords(1000000001), "One Billion One")
        self.assertEqual(
            self.solution.numberToWords(1234567890),
            "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety",
        )

    def test_large_number_and_max_int(self):
        self.assertEqual(self.solution.numberToWords(2000000000), "Two Billion")
        self.assertEqual(
            self.solution.numberToWords(2147483647),
            "Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven",
        )

    def test_numbers_with_internal_zeros(self):
        self.assertEqual(self.solution.numberToWords(10001), "Ten Thousand One")
        self.assertEqual(
            self.solution.numberToWords(10101), "Ten Thousand One Hundred One"
        )
        self.assertEqual(self.solution.numberToWords(1000010), "One Million Ten")
        self.assertEqual(
            self.solution.numberToWords(50868),
            "Fifty Thousand Eight Hundred Sixty Eight",
        )
        self.assertEqual(
            self.solution.numberToWords(100000001), "One Hundred Million One"
        )


if __name__ == "__main__":
    unittest.main()
