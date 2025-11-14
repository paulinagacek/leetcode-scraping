import unittest
from typing import Optional, List

# --- Solution Code ---

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Utility function to build a binary tree from a list (level order with None for nulls).
    Example: [1, 2, 3, None, None, 4, 5]
    """
    if not nodes or nodes[0] is None:
        return None

    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        current_node = queue.pop(0)

        # Left child
        if i < len(nodes) and nodes[i] is not None:
            current_node.left = TreeNode(nodes[i])
            queue.append(current_node.left)
        i += 1

        # Right child
        if i < len(nodes) and nodes[i] is not None:
            current_node.right = TreeNode(nodes[i])
            queue.append(current_node.right)
        i += 1
        
    return root

# --- Unit Tests ---

class TestInorderTraversal(unittest.TestCase):
    """
    Unit tests for the inorderTraversal method of the Solution class.
    """

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    # ----------------------------------
    # ## Standard Cases
    # ----------------------------------

    def test_standard_case_full_tree(self):
        """Standard case: A simple full binary tree."""
        # Tree: [1, 2, 3] -> (2, 1, 3)
        root = build_tree([1, 2, 3])
        expected = [2, 1, 3]
        self.assertEqual(self.solution.inorderTraversal(root), expected)

    def test_standard_case_complex_tree(self):
        """Case from LeetCode example 1: [1, None, 2, 3] -> (1, 3, 2)"""
        # Tree: [1, None, 2, 3]
        #      1
        #       \
        #        2
        #       /
        #      3
        root = build_tree([1, None, 2, 3])
        expected = [1, 3, 2]
        self.assertEqual(self.solution.inorderTraversal(root), expected)

    def test_standard_case_mixed_subtrees(self):
        """Tree with both left and right branches and nulls."""
        # Tree: [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
        # Inorder: [7, 11, 2, 4, 5, 13, 8, 5, 4, 1]
        nodes = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
        root = build_tree(nodes)
        expected = [7, 11, 2, 4, 5, 13, 8, 5, 4, 1]
        self.assertEqual(self.solution.inorderTraversal(root), expected)

    # ----------------------------------
    # ## Edge Cases
    # ----------------------------------

    def test_empty_tree(self):
        """Edge case: Root is None."""
        root = None
        expected = []
        self.assertEqual(self.solution.inorderTraversal(root), expected)

    def test_single_node(self):
        """Edge case: Tree with only one node."""
        root = build_tree([42])
        expected = [42]
        self.assertEqual(self.solution.inorderTraversal(root), expected)

    def test_skewed_left(self):
        """Edge case: A tree skewed completely to the left."""
        # Tree: [1, 2, None, 3, None, 4] -> (4, 3, 2, 1)
        # The list representation needs to be precise: [1, 2, None, 3, None, None, None, 4]
        # To simplify, we'll build it manually for this complex skew:
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        expected = [4, 3, 2, 1]
        self.assertEqual(self.solution.inorderTraversal(root), expected)

    def test_skewed_right(self):
        """Edge case: A tree skewed completely to the right."""
        # Tree: [1, None, 2, None, 3, None, 4] -> (1, 2, 3, 4)
        root = build_tree([1, None, 2, None, 3, None, 4])
        expected = [1, 2, 3, 4]
        self.assertEqual(self.solution.inorderTraversal(root), expected)

    def test_negative_values(self):
        """Case with negative node values."""
        root = build_tree([-10, -5, 5, -1, 0, None, 1])
        expected = [-1, -5, 0, -10, 5, 1]
        self.assertEqual(self.solution.inorderTraversal(root), expected)

    # ----------------------------------
    # ## Large Input Case
    # ----------------------------------

    def test_large_input_full_tree(self):
        """Test a large, relatively full binary tree (Depth 10)."""
        # A tree of depth D has 2^(D+1) - 1 nodes.
        # Depth 10 is too large for the list builder. We'll stick to a simpler large case.
        N = 1000  # Number of nodes
        
        # Create a completely left-skewed tree for a long, linear traversal.
        root = TreeNode(1)
        current = root
        expected_values = [1]
        for i in range(2, N + 1):
            current.left = TreeNode(i)
            current = current.left
            expected_values.append(i)
        
        # Inorder traversal of a left-skewed tree: [N, N-1, ..., 2, 1]
        expected = sorted(expected_values, reverse=True)
        self.assertEqual(self.solution.inorderTraversal(root), expected)

    def test_large_input_long_right_skew(self):
        """Test a large tree skewed completely to the right."""
        N = 1000
        root = TreeNode(1)
        current = root
        expected_values = [1]
        for i in range(2, N + 1):
            current.right = TreeNode(i)
            current = current.right
            expected_values.append(i)
            
        # Inorder traversal of a right-skewed tree: [1, 2, 3, ..., N]
        expected = expected_values
        self.assertEqual(self.solution.inorderTraversal(root), expected)


if __name__ == '__main__':
    # Due to the recursive nature of the solution, a high recursion limit is 
    # helpful for large skewed trees (like N=1000).
    import sys
    sys.setrecursionlimit(2000)
    unittest.main()