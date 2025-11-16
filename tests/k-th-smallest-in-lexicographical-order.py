import unittest


class TestFindKthNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_leetcode_example_1(self):
        self.assertEqual(self.solution.findKthNumber(13, 2), 10)

    def test_leetcode_example_2(self):
        self.assertEqual(self.solution.findKthNumber(1, 1), 1)

    def test_k_is_1(self):
        self.assertEqual(self.solution.findKthNumber(100, 1), 1)
        self.assertEqual(self.solution.findKthNumber(98765, 1), 1)

    def test_single_digit_n(self):
        self.assertEqual(self.solution.findKthNumber(9, 5), 5)
        self.assertEqual(self.solution.findKthNumber(9, 9), 9)

    def test_small_n_and_k(self):
        self.assertEqual(self.solution.findKthNumber(25, 15), 22)
        self.assertEqual(self.solution.findKthNumber(10, 3), 2)

    def test_n_is_100(self):
        self.assertEqual(self.solution.findKthNumber(100, 100), 99)
        self.assertEqual(self.solution.findKthNumber(100, 13), 2)

    def test_medium_n(self):
        self.assertEqual(self.solution.findKthNumber(10000, 5000), 5498)

    def test_k_equals_n(self):
        self.assertEqual(self.solution.findKthNumber(13, 13), 9)

    def test_large_n_small_k(self):
        self.assertEqual(self.solution.findKthNumber(1000000000, 10), 1000000000)

    def test_large_n_large_k_1(self):
        self.assertEqual(self.solution.findKthNumber(1000000000, 200000000), 279999998)

    def test_large_n_large_k_2(self):
        self.assertEqual(self.solution.findKthNumber(654321, 123456), 211106)

    def test_large_n_max_k(self):
        self.assertEqual(self.solution.findKthNumber(1000, 1000), 999)

    def test_boundary_case_subtree_jump(self):
        # Total numbers starting with 1 in range [1, 200] is 111.
        # (1, 10-19, 100-199). The 111th number is 199.
        # The 112th number must be 2.
        self.assertEqual(self.solution.findKthNumber(200, 111), 199)
        self.assertEqual(self.solution.findKthNumber(200, 112), 2)

    def test_another_large_case(self):
        self.assertEqual(self.solution.findKthNumber(98765, 54321), 58888)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
