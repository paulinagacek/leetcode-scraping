import unittest


class TestNthUglyNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first_ugly_number(self):
        self.assertEqual(self.solution.nthUglyNumber(1), 1)

    def test_small_inputs(self):
        self.assertEqual(self.solution.nthUglyNumber(2), 2)
        self.assertEqual(self.solution.nthUglyNumber(3), 3)
        self.assertEqual(self.solution.nthUglyNumber(4), 4)
        self.assertEqual(self.solution.nthUglyNumber(5), 5)
        self.assertEqual(self.solution.nthUglyNumber(6), 6)
        self.assertEqual(self.solution.nthUglyNumber(7), 8)
        self.assertEqual(self.solution.nthUglyNumber(8), 9)
        self.assertEqual(self.solution.nthUglyNumber(9), 10)

    def test_tenth_ugly_number(self):
        self.assertEqual(self.solution.nthUglyNumber(10), 12)

    def test_eleventh_ugly_number(self):
        self.assertEqual(self.solution.nthUglyNumber(11), 15)

    def test_medium_input_1(self):
        self.assertEqual(self.solution.nthUglyNumber(20), 36)

    def test_medium_input_2(self):
        self.assertEqual(self.solution.nthUglyNumber(150), 5832)

    def test_large_input_1(self):
        self.assertEqual(self.solution.nthUglyNumber(1000), 51200000)

    def test_large_input_2(self):
        self.assertEqual(self.solution.nthUglyNumber(1352), 402653184)

    def test_max_constraint(self):
        self.assertEqual(self.solution.nthUglyNumber(1690), 2123366400)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
