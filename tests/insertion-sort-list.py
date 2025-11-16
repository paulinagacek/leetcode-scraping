import unittest
import random


# Helper functions for tests
def list_to_linkedlist(items):
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head


def linkedlist_to_list(head):
    items = []
    current = head
    while current:
        items.append(current.val)
        current = current.next
    return items


# Unit tests
class TestInsertionSortList(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        head = list_to_linkedlist([])
        sorted_head = self.solution.insertionSortList(head)
        self.assertEqual(linkedlist_to_list(sorted_head), [])

    def test_single_node(self):
        head = list_to_linkedlist([1])
        sorted_head = self.solution.insertionSortList(head)
        self.assertEqual(linkedlist_to_list(sorted_head), [1])

    def test_already_sorted_list(self):
        head = list_to_linkedlist([1, 2, 3, 4, 5])
        sorted_head = self.solution.insertionSortList(head)
        self.assertEqual(linkedlist_to_list(sorted_head), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        head = list_to_linkedlist([5, 4, 3, 2, 1])
        sorted_head = self.solution.insertionSortList(head)
        self.assertEqual(linkedlist_to_list(sorted_head), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        head = list_to_linkedlist([4, 2, 1, 3])
        sorted_head = self.solution.insertionSortList(head)
        self.assertEqual(linkedlist_to_list(sorted_head), [1, 2, 3, 4])

    def test_list_with_duplicates(self):
        head = list_to_linkedlist([4, 2, 1, 3, 2, 4, 1])
        sorted_head = self.solution.insertionSortList(head)
        self.assertEqual(linkedlist_to_list(sorted_head), [1, 1, 2, 2, 3, 4, 4])

    def test_list_with_negative_numbers(self):
        head = list_to_linkedlist([-1, 5, 3, 4, 0])
        sorted_head = self.solution.insertionSortList(head)
        self.assertEqual(linkedlist_to_list(sorted_head), [-1, 0, 3, 4, 5])

    def test_all_same_elements(self):
        head = list_to_linkedlist([5, 5, 5, 5, 5])
        sorted_head = self.solution.insertionSortList(head)
        self.assertEqual(linkedlist_to_list(sorted_head), [5, 5, 5, 5, 5])

    def test_two_elements_unsorted(self):
        head = list_to_linkedlist([2, 1])
        sorted_head = self.solution.insertionSortList(head)
        self.assertEqual(linkedlist_to_list(sorted_head), [1, 2])

    def test_large_reverse_sorted_list(self):
        input_list = list(range(1000, 0, -1))
        expected_list = list(range(1, 1001))
        head = list_to_linkedlist(input_list)
        sorted_head = self.solution.insertionSortList(head)
        self.assertEqual(linkedlist_to_list(sorted_head), expected_list)

    def test_large_random_list(self):
        input_list = [random.randint(-1000, 1000) for _ in range(500)]
        expected_list = sorted(input_list)
        head = list_to_linkedlist(input_list)
        sorted_head = self.solution.insertionSortList(head)
        self.assertEqual(linkedlist_to_list(sorted_head), expected_list)

    def test_insertion_at_beginning(self):
        head = list_to_linkedlist([10, 5])
        sorted_head = self.solution.insertionSortList(head)
        self.assertEqual(linkedlist_to_list(sorted_head), [5, 10])

    def test_insertion_in_middle(self):
        head = list_to_linkedlist([10, 20, 15])
        sorted_head = self.solution.insertionSortList(head)
        self.assertEqual(linkedlist_to_list(sorted_head), [10, 15, 20])

    def test_insertion_at_end(self):
        head = list_to_linkedlist([10, 15, 20])
        sorted_head = self.solution.insertionSortList(head)
        self.assertEqual(linkedlist_to_list(sorted_head), [10, 15, 20])


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
