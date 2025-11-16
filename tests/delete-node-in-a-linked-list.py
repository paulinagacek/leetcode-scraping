import unittest


class TestDeleteNode(unittest.TestCase):

    def _create_linked_list(self, items):
        if not items:
            return None
        head = ListNode(items[0])
        current = head
        for item in items[1:]:
            current.next = ListNode(item)
            current = current.next
        return head

    def _linked_list_to_list(self, head):
        items = []
        current = head
        while current:
            items.append(current.val)
            current = current.next
        return items

    def _get_node_by_value(self, head, val):
        current = head
        while current:
            if current.val == val:
                return current
            current = current.next
        return None

    def test_basic_case_delete_middle_node(self):
        solution = Solution()
        head = self._create_linked_list([4, 5, 1, 9])
        node_to_delete = self._get_node_by_value(head, 5)
        if node_to_delete:
            solution.deleteNode(node_to_delete)
        self.assertEqual(self._linked_list_to_list(head), [4, 1, 9])

    def test_basic_case_delete_another_middle_node(self):
        solution = Solution()
        head = self._create_linked_list([4, 5, 1, 9])
        node_to_delete = self._get_node_by_value(head, 1)
        if node_to_delete:
            solution.deleteNode(node_to_delete)
        self.assertEqual(self._linked_list_to_list(head), [4, 5, 9])

    def test_delete_node_before_tail(self):
        solution = Solution()
        head = self._create_linked_list([1, 2, 3, 4])
        node_to_delete = self._get_node_by_value(head, 3)
        if node_to_delete:
            solution.deleteNode(node_to_delete)
        self.assertEqual(self._linked_list_to_list(head), [1, 2, 4])

    def test_delete_in_two_node_list(self):
        solution = Solution()
        head = self._create_linked_list([1, 2])
        node_to_delete = self._get_node_by_value(head, 1)
        if node_to_delete:
            solution.deleteNode(node_to_delete)
        self.assertEqual(self._linked_list_to_list(head), [2])

    def test_with_negative_and_zero_values(self):
        solution = Solution()
        head = self._create_linked_list([-3, 5, 0, -99])
        node_to_delete = self._get_node_by_value(head, 0)
        if node_to_delete:
            solution.deleteNode(node_to_delete)
        self.assertEqual(self._linked_list_to_list(head), [-3, 5, -99])

    def test_with_duplicate_values_delete_first_occurrence(self):
        solution = Solution()
        # Problem statement assumes unique values, but testing robustness is good.
        # This will get the first node with value 7.
        head = self._create_linked_list([1, 7, 3, 7, 5])
        node_to_delete = self._get_node_by_value(head, 7)
        if node_to_delete:
            solution.deleteNode(node_to_delete)
        self.assertEqual(self._linked_list_to_list(head), [1, 3, 7, 5])

    def test_large_list(self):
        solution = Solution()
        input_list = list(range(1000))
        head = self._create_linked_list(input_list)
        node_to_delete = self._get_node_by_value(head, 500)

        if node_to_delete:
            solution.deleteNode(node_to_delete)

        expected_list = list(range(500)) + list(range(501, 1000))
        self.assertEqual(self._linked_list_to_list(head), expected_list)

    def test_large_list_delete_node_near_start(self):
        solution = Solution()
        input_list = list(range(5000))
        head = self._create_linked_list(input_list)
        node_to_delete = self._get_node_by_value(head, 1)

        if node_to_delete:
            solution.deleteNode(node_to_delete)

        expected_list = [0] + list(range(2, 5000))
        self.assertEqual(self._linked_list_to_list(head), expected_list)

    def test_large_list_delete_node_near_end(self):
        solution = Solution()
        input_list = list(range(5000))
        head = self._create_linked_list(input_list)
        # Node to delete is one before the tail
        node_to_delete = self._get_node_by_value(head, 4998)

        if node_to_delete:
            solution.deleteNode(node_to_delete)

        expected_list = list(range(4998)) + [4999]
        self.assertEqual(self._linked_list_to_list(head), expected_list)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
