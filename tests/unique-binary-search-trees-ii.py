import unittest
from typing import Optional, List, Dict, Any
import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize_tree(root: Optional[TreeNode]) -> List[Optional[int]]:
    """
    Serializes a TreeNode structure into a list representation (level-order traversal).
    Used to compare two generated trees for structural and value equality.
    """
    if not root:
        return [None]

    result = []
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None markers to standardize output
    while result and result[-1] is None:
        result.pop()

    return result


# --- Unit Tests ---


class TestGenerateTrees(unittest.TestCase):
    """
    Unit tests for the generateTrees method.
    """

    def setUp(self):
        self.solution = Solution()

    def assertBSTListsEqual(
        self,
        actual: List[Optional[TreeNode]],
        expected_serializations: List[List[Optional[int]]],
    ):
        """
        Custom assertion to check if the list of generated BSTs matches the expected set.
        It serializes the actual trees and compares the set of serializations to the expected set.
        """
        actual_serializations = sorted([tuple(serialize_tree(tree)) for tree in actual])
        expected_serializations_sorted = sorted(
            [tuple(s) for s in expected_serializations]
        )

        self.assertEqual(
            len(actual_serializations),
            len(expected_serializations_sorted),
            "The number of generated trees does not match the expected count.",
        )
        self.assertEqual(
            actual_serializations,
            expected_serializations_sorted,
            "The structure or values of the generated trees are incorrect.",
        )

    # ----------------------------------
    # ## Edge Cases
    # ----------------------------------

    def test_n_equals_0(self):
        """Edge case: N=0 (The set of nodes is empty, result should be [None])."""
        n = 0
        expected_serializations = [[None]]
        # The canonical solution's helper will be called with start=1, end=0, returning [None].
        self.assertBSTListsEqual(
            self.solution.generateTrees(n), expected_serializations
        )

    def test_n_equals_1(self):
        """Edge case: N=1 (Catalan C1=1 tree: [1])."""
        n = 1
        expected_serializations = [[1]]
        self.assertBSTListsEqual(
            self.solution.generateTrees(n), expected_serializations
        )

    def test_n_equals_2(self):
        """Edge case: N=2 (Catalan C2=2 trees)."""
        n = 2
        expected_serializations = [
            [1, None, 2],  # Root 1 (Standard serialization is [1, None, 2])
            [
                2,
                1,
            ],  # Root 2 (Standard serialization [2, 1, None], which utility simplifies to [2, 1])
        ]
        self.assertBSTListsEqual(
            self.solution.generateTrees(n), expected_serializations
        )

    # ----------------------------------
    # ## Standard Cases
    # ----------------------------------

    def test_n_equals_3(self):
        """Standard case: N=3 (Catalan C3=5 trees)."""
        n = 3
        expected_serializations = [
            [1, None, 2, None, None, None, 3],  # 1(None, 2(None, 3))
            [1, None, 3, 2, None],  # 1(None, 3(2, None))
            [2, 1, 3],  # 2(1, 3)
            [3, 1, None, None, 2],  # 3(1(None, 2), None)
            [3, 2, None, 1, None],  # 3(2(1, None), None)
        ]
        # In standardized serialization:
        expected = [
            [1, None, 2, None, 3],
            [1, None, 3, 2],
            [2, 1, 3],
            [3, 1, None, None, 2],
            [3, 2, None, 1],
        ]
        self.assertBSTListsEqual(self.solution.generateTrees(n), expected)

    def test_n_equals_4(self):
        """Standard case: N=4 (Catalan C4=14 trees). We check the count."""
        n = 4
        # C4 = 14
        expected_count = 14
        result = self.solution.generateTrees(n)
        self.assertEqual(
            len(result), expected_count, f"Expected {expected_count} trees for N={n}"
        )

        # Spot check specific extreme trees:
        result_serializations = [tuple(serialize_tree(t)) for t in result]

        # Fully left-skewed: 4(3(2(1))) -> [4, 3, None, 2, None, 1]
        left_skewed = (4, 3, None, 2, None, 1)
        self.assertIn(left_skewed, result_serializations)

        # Fully right-skewed: 1(None, 2(None, 3(None, 4))) -> [1, None, 2, None, 3, None, 4]
        right_skewed = (1, None, 2, None, 3, None, 4)
        self.assertIn(right_skewed, result_serializations)

    # ----------------------------------
    # ## Large Input Cases
    # ----------------------------------

    def test_large_input_n_equals_7(self):
        """
        Large input (N=7). Catalan C7=429.
        We check the count and the boundary conditions.
        """
        n = 7
        expected_count = 429
        result = self.solution.generateTrees(n)
        self.assertEqual(
            len(result), expected_count, f"Expected {expected_count} trees for N={n}"
        )

        result_serializations = [tuple(serialize_tree(t)) for t in result]

        # Check the fully left-skewed tree (4-node deep)
        # Root 7, Left 6, ... Left 1.
        left_skewed = (7, 6, None, 5, None, 4, None, 3, None, 2, None, 1)
        self.assertTrue(
            any(s[0] == 7 for s in result_serializations),
            "Should contain trees rooted at 7.",
        )
        self.assertTrue(left_skewed[:12] in result_serializations)

        # Check the fully right-skewed tree
        # Root 1, Right 2, ... Right 7.
        right_skewed = (1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7)
        self.assertTrue(
            any(s[0] == 1 for s in result_serializations),
            "Should contain trees rooted at 1.",
        )
        self.assertTrue(right_skewed[:13] in result_serializations)

    def test_large_input_n_equals_8(self):
        """
        Maximum practical large input (N=8). Catalan C8=1430.
        We check the count.
        """
        n = 8
        expected_count = 1430
        result = self.solution.generateTrees(n)
        self.assertEqual(
            len(result), expected_count, f"Expected {expected_count} trees for N={n}"
        )


if __name__ == "__main__":
    unittest.main()
