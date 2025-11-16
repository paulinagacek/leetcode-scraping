import unittest


class TestGetMoneyAmount(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_edge_case_n1(self):
        self.assertEqual(self.solution.getMoneyAmount(1), 0, "Test Case 1: n = 1")

    def test_small_values(self):
        self.assertEqual(self.solution.getMoneyAmount(2), 1, "Test Case 2: n = 2")
        self.assertEqual(self.solution.getMoneyAmount(3), 2, "Test Case 3: n = 3")
        self.assertEqual(self.solution.getMoneyAmount(4), 4, "Test Case 4: n = 4")
        self.assertEqual(self.solution.getMoneyAmount(5), 6, "Test Case 5: n = 5")
        self.assertEqual(self.solution.getMoneyAmount(6), 8, "Test Case 6: n = 6")
        self.assertEqual(self.solution.getMoneyAmount(7), 10, "Test Case 7: n = 7")

    def test_leetcode_example(self):
        self.assertEqual(
            self.solution.getMoneyAmount(10),
            16,
            "Test Case 8: n = 10 (LeetCode Example)",
        )

    def test_medium_values(self):
        self.assertEqual(self.solution.getMoneyAmount(15), 30, "Test Case 9: n = 15")
        self.assertEqual(self.solution.getMoneyAmount(20), 49, "Test Case 10: n = 20")
        self.assertEqual(self.solution.getMoneyAmount(50), 172, "Test Case 11: n = 50")

    def test_large_values(self):
        self.assertEqual(
            self.solution.getMoneyAmount(100), 400, "Test Case 12: n = 100"
        )
        self.assertEqual(
            self.solution.getMoneyAmount(150), 692, "Test Case 13: n = 150"
        )
        self.assertEqual(
            self.solution.getMoneyAmount(199), 946, "Test Case 14: n = 199"
        )
        self.assertEqual(
            self.solution.getMoneyAmount(200),
            952,
            "Test Case 15: n = 200 (Max Constraint)",
        )


if __name__ == "__main__":
    unittest.main()
