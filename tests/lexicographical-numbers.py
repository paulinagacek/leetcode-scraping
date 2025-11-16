import unittest


class TestLexicalOrder(unittest.TestCase):
    def setUp(self):
        """Set up the test case."""
        self.solution = Solution()

    def _get_expected_result(self, n: int) -> List[int]:
        """Helper to generate expected result via a simple method."""
        return [int(s) for s in sorted([str(i) for i in range(1, n + 1)])]

    def test_example_1(self):
        n = 13
        expected = [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(self.solution.lexicalOrder(n), expected)

    def test_example_2(self):
        n = 2
        expected = [1, 2]
        self.assertEqual(self.solution.lexicalOrder(n), expected)

    def test_edge_case_n_1(self):
        n = 1
        expected = [1]
        self.assertEqual(self.solution.lexicalOrder(n), expected)

    def test_single_digit_range(self):
        n = 9
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(self.solution.lexicalOrder(n), expected)

    def test_boundary_n_10(self):
        n = 10
        expected = [1, 10, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(self.solution.lexicalOrder(n), expected)

    def test_boundary_n_99(self):
        n = 99
        expected = self._get_expected_result(n)
        self.assertEqual(self.solution.lexicalOrder(n), expected)

    def test_boundary_n_100(self):
        n = 100
        expected = self._get_expected_result(n)
        self.assertEqual(self.solution.lexicalOrder(n), expected)

    def test_intermediate_case(self):
        n = 205
        expected = self._get_expected_result(n)
        result = self.solution.lexicalOrder(n)
        self.assertEqual(len(result), n)
        self.assertEqual(result, expected)

    def test_transition_case(self):
        n = 199
        expected = self._get_expected_result(n)
        result = self.solution.lexicalOrder(n)

        # Check transition from 1... to 2...
        idx_2 = result.index(2)
        self.assertEqual(result[idx_2 - 1], 199)
        self.assertEqual(result, expected)

    def test_large_input(self):
        n = 50000
        result = self.solution.lexicalOrder(n)

        # Basic property checks for large inputs
        self.assertEqual(len(result), n)
        self.assertEqual(result[0], 1)

        # Check order of some early elements
        self.assertEqual(result[1], 10)
        self.assertEqual(result[2], 100)
        self.assertEqual(result[3], 1000)
        self.assertEqual(result[4], 10000)

        # Verify major transitions
        # From numbers starting with 1 to 2
        idx_2 = result.index(2)
        # The last number starting with '1' should be 19999
        self.assertEqual(result[idx_2 - 1], 19999)

        # From numbers starting with 2 to 3
        idx_3 = result.index(3)
        # The last number starting with '2' should be 29999
        self.assertEqual(result[idx_3 - 1], 29999)

        # From numbers starting with 4 to 5
        idx_5 = result.index(5)
        # The last number starting with '4' should be 49999
        self.assertEqual(result[idx_5 - 1], 49999)

        # Verify some numbers around the limit
        # n = 50000. The numbers 5 and 50 and 500 and 5000 and 50000 should be present
        self.assertIn(5, result)
        self.assertIn(50, result)
        self.assertIn(500, result)
        self.assertIn(5000, result)
        self.assertIn(50000, result)

        # Number 50001 should not be present
        self.assertNotIn(50001, result)

        # Check the last element in the sequence
        # The last generated group will start with 9. The largest number <= 50000 starting with 9 is 9999.
        self.assertEqual(result[-1], 9999)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
