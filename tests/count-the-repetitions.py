import unittest
from typing import List, Dict, Tuple

class TestMaxRepetitions(unittest.TestCase):
    """
    Unit tests for the getMaxRepetitions method.
    """

    def setUp(self):
        self.solution = Solution()

    # ----------------------------------
    # ## Edge Cases 🔪
    # ----------------------------------

    def test_s1_cannot_contain_s2(self):
        """Edge case: s1 contains none of the characters in s2."""
        self.assertEqual(self.solution.getMaxRepetitions("a", 100, "b", 1), 0)
        self.assertEqual(self.solution.getMaxRepetitions("xox", 3, "abc", 1), 0)

    def test_s1_shorter_than_s2_one_rep(self):
        """Edge case: s1 is shorter than s2, but [s1, n1] is not long enough."""
        self.assertEqual(self.solution.getMaxRepetitions("a", 2, "aa", 1), 1) # [aa] contains [aa] once.
        self.assertEqual(self.solution.getMaxRepetitions("a", 2, "aaa", 1), 0) # [aa] does not contain [aaa] once.

    def test_simple_full_match(self):
        """Simple case: s1 is exactly s2."""
        self.assertEqual(self.solution.getMaxRepetitions("abc", 2, "abc", 1), 2)
        self.assertEqual(self.solution.getMaxRepetitions("ab", 4, "ab", 2), 2)

    # ----------------------------------
    # ## Standard Cases (No Cycle Needed) 📈
    # ----------------------------------

    def test_standard_case_no_cycle(self):
        """Standard case requiring full iteration without a cycle."""
        s1 = "abac"
        n1 = 3  # [abacabacabac]
        s2 = "ac"
        n2 = 1
        # [abac] contains [ac] once. Total: 3 times. 3 // 1 = 3.
        self.assertEqual(self.solution.getMaxRepetitions(s1, n1, s2, n2), 3)

    def test_standard_case_incomplete_final_match(self):
        """Case where the final iteration of s1 does not complete s2."""
        s1 = "aba"
        n1 = 2  # [abaaba]
        s2 = "aab"
        n2 = 1
        # [abaaba] contains [aab] once. Final 'a' of s2 is not matched.
        self.assertEqual(self.solution.getMaxRepetitions(s1, n1, s2, n2), 1)

    # ----------------------------------
    # ## Cycle Detection Cases 🔄
    # ----------------------------------

    def test_cycle_case_simple(self):
        """Test case where a simple cycle is detected and fast-forwarded."""
        s1 = "ab"
        n1 = 100
        s2 = "ba"
        n2 = 1
        # [ab] completes 0 s2, index=1 ('b')
        # [abab] completes 1 s2, index=0 (Start of cycle)
        # Cycle: 2 s1 consumes 1 s2.
        # 100 s1 / 2 s1 per cycle = 50 cycles. 50 * 1 s2 = 50.
        self.assertEqual(self.solution.getMaxRepetitions(s1, n1, s2, n2), 99)

    def test_cycle_case_with_remainder(self):
        """Test cycle detection with remaining s1 strings after fast-forward."""
        s1 = "abc"
        n1 = 10
        s2 = "ac"
        n2 = 1
        # s1=1, s2=1, index=1 ('c')
        # s1=2, s2=2, index=1 ('c') -> Cycle detected at index 1.
        # Loop: 1 s1 consumes 1 s2.
        # Remaining s1: 10 - 2 = 8.
        # remaining_loops = 8 // 1 = 8.
        # s1_count = 2 + 8*1 = 10. s2_count = 2 + 8*1 = 10.
        self.assertEqual(self.solution.getMaxRepetitions(s1, n1, s2, n2), 10)

    def test_official_leetcode_example(self):
        """The official example from the problem statement."""
        s1 = "acb"
        n1 = 4
        s2 = "ab"
        n2 = 2
        # [acbacbacba] contains [ab] twice (1st: a.b.c..., 2nd: ...a.b.c...)
        # s1=1, s2=0, index=2 ('b')
        # s1=2, s2=1, index=1 ('a')
        # s1=3, s2=1, index=2 ('b') -> Cycle detected at index 2 (s1=1, s2=0)
        # Loop: 2 s1 consumes 1 s2.
        # Remaining s1: 4 - 3 = 1. remaining_loops = 1 // 2 = 0. No fast-forward.
        # Final s2_count = 1. Result: 1 // 2 = 0.
        self.assertEqual(self.solution.getMaxRepetitions(s1, n1, s2, n2), 2)

    # ----------------------------------
    # ## Large Input Case (Testing Fast-Forward) 🚀
    # ----------------------------------

    def test_large_input_fast_forward(self):
        """Test a very large n1 value that necessitates cycle detection for speed."""
        s1 = "aabbaa"
        n1 = 1000000
        s2 = "aa"
        n2 = 1
        
        # s1=1: s2_count=3, index=0.
        # s1=2: s2_count=6, index=0. -> Cycle detected at index 0.
        # Loop: 1 s1 consumes 3 s2.
        # Prev: (1, 3). Current: (2, 6).
        # loop_s1_count = 1. loop_s2_count = 3.
        # remaining_loops = (1000000 - 2) // 1 = 999998.
        # s2_count = 6 + 999998 * 3 = 6 + 2999994 = 3000000.
        self.assertEqual(self.solution.getMaxRepetitions(s1, n1, s2, n2), 2000000)

if __name__ == '__main__':
    unittest.main()