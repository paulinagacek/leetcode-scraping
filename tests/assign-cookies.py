import unittest
from typing import List

class TestFindContentChildren(unittest.TestCase):
    """
    Unit tests for the findContentChildren method.
    """

    def setUp(self):
        self.solution = Solution()

    # ----------------------------------
    # ## Standard Cases 🍪
    # ----------------------------------

    def test_example_1_more_children_than_cookies(self):
        """Standard case where children and cookies are matched."""
        g = [1, 2, 3]
        s = [1, 1]
        # Child 1 (greed 1) gets cookie 1. Child 2 (greed 2) remains unhappy.
        self.assertEqual(self.solution.findContentChildren(g, s), 1)

    def test_example_2_more_cookies_than_children(self):
        """Standard case where more cookies than children exist."""
        g = [1, 2]
        s = [1, 2, 3]
        # Child 1 (greed 1) gets cookie 1. Child 2 (greed 2) gets cookie 2.
        self.assertEqual(self.solution.findContentChildren(g, s), 2)
        
    def test_case_no_perfect_match(self):
        """Case where cookie sizes are sufficient but non-optimal arrangement without sorting."""
        g = [10, 9, 8, 7]
        s = [5, 6, 7, 8]
        # After sorting: g=[7, 8, 9, 10], s=[5, 6, 7, 8]
        # Child 7 gets cookie 7. Child 8 gets cookie 8.
        self.assertEqual(self.solution.findContentChildren(g, s), 2)

    # ----------------------------------
    # ## Edge Cases 🔪
    # ----------------------------------

    def test_empty_children(self):
        """Edge case: No children."""
        g = []
        s = [1, 100]
        self.assertEqual(self.solution.findContentChildren(g, s), 0)

    def test_empty_cookies(self):
        """Edge case: No cookies."""
        g = [1, 5, 10]
        s = []
        self.assertEqual(self.solution.findContentChildren(g, s), 0)

    def test_all_mismatched(self):
        """Edge case: All cookies are too small for all children."""
        g = [10, 11, 12]
        s = [1, 2, 3]
        self.assertEqual(self.solution.findContentChildren(g, s), 0)

    def test_all_cookies_satisfy_all_children(self):
        """Edge case: All cookies are large enough."""
        g = [1, 1, 1]
        s = [10, 20, 30]
        # All 3 children are satisfied by the first 3 cookies.
        self.assertEqual(self.solution.findContentChildren(g, s), 3)

    def test_greed_and_cookies_with_zero(self):
        """Edge case: Zero values (assuming non-negative constraints)."""
        g = [0, 1]
        s = [0, 1]
        # Child 0 gets cookie 0. Child 1 gets cookie 1.
        self.assertEqual(self.solution.findContentChildren(g, s), 2)

    def test_duplicate_values(self):
        """Case with multiple duplicate values in both lists."""
        g = [1, 1, 3, 5]
        s = [2, 2, 4, 4]
        # g=[1, 1, 3, 5], s=[2, 2, 4, 4]
        # Child 1 gets cookie 2. Child 1 gets cookie 2. Child 3 gets cookie 4.
        self.assertEqual(self.solution.findContentChildren(g, s), 3)

    # ----------------------------------
    # ## Large Input Cases 📏
    # ----------------------------------

    def test_large_input_full_match(self):
        """Large input (N=1000) where every child gets a unique cookie."""
        N = 1000
        g = list(range(1, N + 1))  # Greed: 1 to 1000
        s = list(range(1, N + 1))  # Cookie: 1 to 1000
        # Each child is satisfied by their corresponding cookie.
        self.assertEqual(self.solution.findContentChildren(g, s), N)

    def test_large_input_partial_match(self):
        """Large input where only half of the children can be satisfied."""
        N = 5000
        g = list(range(1, N + 1))       # Greed: 1 to 5000
        s = list(range(1, N // 2 + 1))  # Cookie: 1 to 2500
        # The first 2500 children are satisfied.
        self.assertEqual(self.solution.findContentChildren(g, s), N // 2)

    def test_large_input_high_greed_low_cookies(self):
        """Large input with high greed values and small cookie sizes."""
        N = 2000
        g = [1000] * N + [1001] * N # 4000 children
        s = [1000] * (N + 5)        # 2005 cookies, all size 1000
        
        # Only the first 2000 children (greed 1000) are satisfied.
        self.assertEqual(self.solution.findContentChildren(g, s), N)


if __name__ == '__main__':
    unittest.main()