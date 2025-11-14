import unittest
from typing import Set, Dict

class TestAllOne(unittest.TestCase):
    """
    Unit tests for the AllOne data structure.
    """

    def setUp(self):
        # Set up a new instance for each test
        self.ao = AllOne()

    # ----------------------------------
    # ## Edge Cases
    # ----------------------------------

    def test_empty_structure(self):
        """Test getMaxKey and getMinKey on an empty structure."""
        self.assertEqual(self.ao.getMaxKey(), "")
        self.assertEqual(self.ao.getMinKey(), "")

    def test_single_key_inc_dec(self):
        """Test single key incrementing and decrementing back to 0."""
        self.ao.inc("a")  # Freq 1
        self.ao.inc("a")  # Freq 2
        self.assertEqual(self.ao.getMaxKey(), "a")
        self.assertEqual(self.ao.getMinKey(), "a")
        self.ao.dec("a")  # Freq 1
        self.assertEqual(self.ao.getMaxKey(), "a")
        self.ao.dec("a")  # Freq 0 (removed)
        self.assertEqual(self.ao.getMaxKey(), "")
        self.assertEqual(self.ao.getMinKey(), "")
        self.assertNotIn("a", self.ao.map)

    def test_dec_non_existent_key(self):
        """Test calling dec on a key that doesn't exist."""
        self.ao.inc("b")
        self.ao.dec("a") # Should do nothing
        self.assertEqual(self.ao.getMaxKey(), "b") # Should still have 'b' at Freq 1

    def test_remove_node_on_inc_and_dec(self):
        """Test node removal logic after both inc and dec operations."""
        self.ao.inc("a") # Freq 1: [1: a]
        self.ao.inc("b") # Freq 1: [1: a, b]
        self.ao.inc("a") # Freq 2: [1: b] -> [2: a]
        self.ao.dec("b") # Freq 0: [2: a] (1: b node removed)
        
        # Check that the list is clean (only the node for Freq 2 remains)
        self.assertEqual(self.ao.head.next.freq, 2)
        self.assertEqual(self.ao.head.next.next, self.ao.tail)

    # ----------------------------------
    # ## Standard Cases
    # ----------------------------------

    def test_example_sequence_1(self):
        """Standard sequence: Mixed inc/dec and max/min calls."""
        self.ao.inc("hello")  # F1: [1: hello]
        self.ao.inc("goodbye") # F1: [1: hello, goodbye]
        self.ao.inc("hello")  # F2: [1: goodbye] -> [2: hello]
        self.assertIn(self.ao.getMaxKey(), {"hello"})
        self.assertIn(self.ao.getMinKey(), {"goodbye"})
        
        self.ao.inc("goodbye") # F2: [2: hello, goodbye]
        self.ao.inc("goodbye") # F3: [2: hello] -> [3: goodbye]
        self.ao.inc("hi")      # F1: [1: hi] -> [2: hello] -> [3: goodbye]
        
        self.assertIn(self.ao.getMaxKey(), {"goodbye"})
        self.assertIn(self.ao.getMinKey(), {"hi"})

    def test_example_sequence_2_max_min_switch(self):
        """Test case where max key moves to min key after dec."""
        self.ao.inc("A") # F1: [1: A]
        self.ao.inc("B") # F1: [1: A, B]
        self.ao.inc("A") # F2: [1: B] -> [2: A]
        self.ao.inc("A") # F3: [1: B] -> [3: A] (Node 2 removed)
        
        self.assertIn(self.ao.getMaxKey(), {"A"})
        self.assertIn(self.ao.getMinKey(), {"B"})
        
        self.ao.dec("A") # F2: [1: B] -> [2: A]
        self.assertIn(self.ao.getMaxKey(), {"A"})
        self.assertIn(self.ao.getMinKey(), {"B"})
        
        self.ao.dec("A") # F1: [1: A, B] (Node 2 removed)
        self.assertIn(self.ao.getMaxKey(), {"A", "B"})
        self.assertIn(self.ao.getMinKey(), {"A", "B"})

    # ----------------------------------
    # ## Large Input Cases
    # ----------------------------------
    
    def test_large_input_cycle(self):
        """
        Large sequence of operations designed to stress node creation/removal 
        and map updates across many keys.
        """
        N = 100
        keys = [str(i) for i in range(N)]

        # Phase 1: Ramp up all keys to Freq 50
        for _ in range(50):
            for key in keys:
                self.ao.inc(key)
        
        # All keys should be at Freq 50. Only one node should exist.
        self.assertEqual(self.ao.head.next.freq, 50)
        self.assertEqual(self.ao.head.next.next, self.ao.tail)
        self.assertEqual(len(self.ao.head.next.keys), N)
        self.assertIn(self.ao.getMaxKey(), set(keys))
        
        # Phase 2: Create a cyclic pattern
        # 0-49 dec to Freq 49
        # 50-99 inc to Freq 51
        for i in range(N // 2):
            self.ao.dec(keys[i])
            self.ao.inc(keys[i + N // 2])
        
        # Three nodes should exist: Freq 49, 50, 51
        self.assertEqual(self.ao.head.next.freq, 49) # Min Freq
        self.assertEqual(self.ao.tail.prev.freq, 51) # Max Freq
        
        self.assertEqual(len(self.ao.head.next.keys), 50)  # Keys 0-49
        self.assertEqual(len(self.ao.head.next.next.keys), 50) # Freq 50 node should have been removed
        self.assertEqual(len(self.ao.tail.prev.keys), 50)  # Keys 50-99
        
        self.assertIn(self.ao.getMinKey(), set(keys[:50]))
        self.assertIn(self.ao.getMaxKey(), set(keys[50:]))
        
        # Phase 3: Drive all keys back to 0
        for _ in range(51):
            for key in keys:
                self.ao.dec(key)
                
        # Final state check
        self.assertEqual(self.ao.getMaxKey(), "")
        self.assertEqual(self.ao.getMinKey(), "")
        self.assertEqual(self.ao.head.next, self.ao.tail)
        self.assertEqual(len(self.ao.map), 0)

if __name__ == '__main__':
    unittest.main()