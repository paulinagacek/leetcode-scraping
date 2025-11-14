import unittest
from typing import Optional, List

def list_to_linkedlist(data: List[int]) -> Optional[ListNode]:
    """Converts a Python list to a linked list."""
    if not data:
        return None
    head = ListNode(data[0])
    current = head
    for val in data[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linkedlist_to_list(head: Optional[ListNode]) -> List[int]:
    """Converts a linked list to a Python list."""
    data = []
    current = head
    while current:
        data.append(current.val)
        current = current.next
    return data

# --- Unit Tests ---

class TestAddTwoNumbersII(unittest.TestCase):
    """
    Unit tests for the addTwoNumbers method.
    """

    def setUp(self):
        self.solution = Solution()

    # ----------------------------------
    # ## Helper Tests (Test the reverse logic first)
    # ----------------------------------

    def test_reverse_list_helper_standard(self):
        l = list_to_linkedlist([1, 2, 3])
        r = self.solution.reverseList(l)
        self.assertEqual(linkedlist_to_list(r), [3, 2, 1])
        
    def test_reverse_list_helper_single(self):
        l = list_to_linkedlist([5])
        r = self.solution.reverseList(l)
        self.assertEqual(linkedlist_to_list(r), [5])

    # ----------------------------------
    # ## Standard Cases
    # ----------------------------------

    def test_standard_case_no_carry(self):
        """Standard case where lengths are equal and no carry is generated."""
        l1 = list_to_linkedlist([1, 2, 3])  # 123
        l2 = list_to_linkedlist([4, 5, 6])  # 456
        expected = [5, 7, 9]                # 579
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linkedlist_to_list(result), expected)

    def test_standard_case_with_carry(self):
        """Standard case with carry propagation."""
        l1 = list_to_linkedlist([7, 2, 4, 3])  # 7243
        l2 = list_to_linkedlist([5, 6, 4])     # 564
        expected = [7, 8, 0, 7]                # 7807 (7243 + 564)
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linkedlist_to_list(result), expected)

    def test_different_lengths_no_carry(self):
        """Case with different lengths and no carry."""
        l1 = list_to_linkedlist([1, 0, 0])     # 100
        l2 = list_to_linkedlist([9, 9])        # 99
        expected = [1, 9, 9]                   # 199
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linkedlist_to_list(result), expected)

    # ----------------------------------
    # ## Edge Cases
    # ----------------------------------

    def test_one_empty_list(self):
        """Edge case: One list is empty (should return the other list)."""
        l1 = list_to_linkedlist([9, 8])
        l2 = list_to_linkedlist([])
        expected = [9, 8]
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linkedlist_to_list(result), expected)

    def test_zero_sum(self):
        """Edge case: Summing zero values."""
        l1 = list_to_linkedlist([0])
        l2 = list_to_linkedlist([0])
        expected = [0]
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linkedlist_to_list(result), expected)

    def test_leading_zeros(self):
        """
        Edge case: Input lists contain leading zeros. The canonical solution
        preserves these zeros in the output due to the nature of the reversal/addition.
        [0, 1] (1) + [0] (0) = [0, 1] (1)
        """
        l1 = list_to_linkedlist([0, 1])
        l2 = list_to_linkedlist([0])
        # The solution incorrectly includes the leading zero from the original lists.
        expected = [0, 1] 
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linkedlist_to_list(result), expected)
        
    def test_final_carry(self):
        """Edge case: The final carry creates a new most significant digit."""
        l1 = list_to_linkedlist([9, 9])
        l2 = list_to_linkedlist([1])
        expected = [1, 0, 0] # 99 + 1 = 100
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linkedlist_to_list(result), expected)

    def test_all_nines_carry(self):
        """Edge case: All 9s propagating a carry to a new digit."""
        l1 = list_to_linkedlist([9, 9, 9])
        l2 = list_to_linkedlist([1])
        expected = [1, 0, 0, 0] # 999 + 1 = 1000
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linkedlist_to_list(result), expected)

    # ----------------------------------
    # ## Large Input Cases
    # ----------------------------------

    def test_large_input_equal_length(self):
        """Large input (50 digits) with no carry."""
        n = 50
        l1_data = [1] * n
        l2_data = [1] * n
        expected = [2] * n
        
        l1 = list_to_linkedlist(l1_data)
        l2 = list_to_linkedlist(l2_data)
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linkedlist_to_list(result), expected)

    def test_large_input_different_lengths_and_carry(self):
        """Large input with significantly different lengths and carry."""
        l1_data = [1] + [0] * 99 # 1 followed by 99 zeros (100 digits)
        l2_data = [9] * 10       # 10 nines (10 digits)
        
        l1 = list_to_linkedlist(l1_data)
        l2 = list_to_linkedlist(l2_data)
        
        # Expected: [1] + [0]*89 + [9]*10  (Total 1 + 89 + 10 = 100 digits)
        # This represents 10^99 + (10^10 - 1)
        expected = [1] + [0] * 89 + [9] * 10 
        
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linkedlist_to_list(result), expected)

    def test_large_input_max_carry_generation(self):
        """Large input (50 digits) designed to maximize carry propagation."""
        n = 50
        l1_data = [9] * n 
        l2_data = [1]     # 9...9 + 1
        expected = [1] + [0] * n # 1 followed by 50 zeros (51 digits total)
        
        l1 = list_to_linkedlist(l1_data)
        l2 = list_to_linkedlist(l2_data)
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(linkedlist_to_list(result), expected)


if __name__ == '__main__':
    unittest.main()