import unittest


class TestMyQueue(unittest.TestCase):

    def test_basic_workflow(self):
        """Test the basic sequence of push, peek, pop, and empty."""
        q = MyQueue()
        self.assertTrue(q.empty())

        q.push(1)
        q.push(2)

        self.assertFalse(q.empty())
        self.assertEqual(q.peek(), 1)
        self.assertEqual(q.pop(), 1)

        self.assertFalse(q.empty())
        self.assertEqual(q.peek(), 2)
        self.assertEqual(q.pop(), 2)

        self.assertTrue(q.empty())

    def test_empty_queue_operations(self):
        """Test peeking or popping from an empty queue."""
        q = MyQueue()
        self.assertTrue(q.empty())
        with self.assertRaises(IndexError):
            q.peek()
        with self.assertRaises(IndexError):
            q.pop()

    def test_single_element(self):
        """Test the queue with only one element."""
        q = MyQueue()
        q.push(100)
        self.assertFalse(q.empty())
        self.assertEqual(q.peek(), 100)
        self.assertEqual(q.pop(), 100)
        self.assertTrue(q.empty())

    def test_interleaved_operations(self):
        """Test a mix of push and pop operations."""
        q = MyQueue()
        q.push(1)
        q.push(2)
        self.assertEqual(q.pop(), 1)  # Transfers [1, 2] to out_stk, pops 1. out_stk=[2]

        q.push(3)  # in_stk=[3]

        self.assertEqual(q.peek(), 2)  # out_stk is not empty, peeks 2
        self.assertEqual(q.pop(), 2)  # out_stk becomes empty

        self.assertFalse(q.empty())

        self.assertEqual(q.peek(), 3)  # Transfers [3] to out_stk
        self.assertEqual(q.pop(), 3)
        self.assertTrue(q.empty())

    def test_multiple_transfers(self):
        """Test scenarios that cause multiple transfers between stacks."""
        q = MyQueue()
        # First batch
        q.push(1)
        q.push(2)
        self.assertEqual(q.pop(), 1)
        self.assertEqual(q.pop(), 2)
        self.assertTrue(q.empty())

        # Second batch
        q.push(3)
        q.push(4)
        self.assertFalse(q.empty())
        self.assertEqual(q.peek(), 3)

        # Mix in another push
        q.push(5)
        self.assertEqual(q.pop(), 3)
        self.assertEqual(q.pop(), 4)
        self.assertEqual(q.pop(), 5)
        self.assertTrue(q.empty())

    def test_large_input(self):
        """Test the queue with a large number of elements."""
        q = MyQueue()
        n = 10000
        for i in range(n):
            q.push(i)

        self.assertFalse(q.empty())

        for i in range(n):
            self.assertEqual(q.peek(), i, f"Peek failed at index {i}")
            self.assertEqual(q.pop(), i, f"Pop failed at index {i}")

        self.assertTrue(q.empty())
        with self.assertRaises(IndexError):
            q.peek()

    def test_different_data_types(self):
        """Test the queue with various data types."""
        q = MyQueue()
        q.push("hello")
        q.push(None)
        q.push([1, 2])
        q.push({"a": 1})
        q.push(3.14)

        self.assertEqual(q.pop(), "hello")
        self.assertIsNone(q.pop())
        self.assertEqual(q.pop(), [1, 2])
        self.assertEqual(q.peek(), {"a": 1})
        self.assertEqual(q.pop(), {"a": 1})
        self.assertEqual(q.pop(), 3.14)
        self.assertTrue(q.empty())

    def test_empty_method_states(self):
        """Test the empty() method in all possible internal states."""
        q = MyQueue()

        # State 1: Both stacks empty
        self.assertTrue(q.empty())

        # State 2: in_stk has items, out_stk is empty
        q.push(1)
        self.assertFalse(q.empty())

        # State 3: out_stk has items, in_stk is empty
        q.peek()  # This moves the element from in_stk to out_stk
        self.assertFalse(q.empty())

        # State 4: Both stacks have items
        q.push(2)  # out_stk=[1], in_stk=[2]
        self.assertFalse(q.empty())

        # Back to State 1
        q.pop()  # pops 1
        q.pop()  # pops 2
        self.assertTrue(q.empty())


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
