import unittest


class TestRandomizedCollection(unittest.TestCase):

    def setUp(self):
        """Set up a new RandomizedCollection for each test."""
        self.rc = RandomizedCollection()
        # Use a fixed seed for reproducible tests involving randomness
        seed(42)

    def test_initialization(self):
        """Test if the collection is initialized correctly."""
        self.assertEqual(self.rc.lst, [])
        self.assertIsInstance(self.rc.idx, defaultdict)

    def test_insert_new_element(self):
        """Test inserting a new, unique element."""
        self.assertTrue(self.rc.insert(1))
        self.assertEqual(self.rc.lst, [1])
        self.assertEqual(self.rc.idx, {1: {0}})
        self.assertTrue(self.rc.insert(2))
        self.assertEqual(self.rc.lst, [1, 2])
        self.assertEqual(self.rc.idx, {1: {0}, 2: {1}})

    def test_insert_duplicate_element(self):
        """Test inserting an element that already exists."""
        self.rc.insert(1)
        self.assertFalse(self.rc.insert(1))
        self.assertEqual(self.rc.lst, [1, 1])
        self.assertEqual(self.rc.idx, {1: {0, 1}})
        self.assertFalse(self.rc.insert(1))
        self.assertEqual(self.rc.lst, [1, 1, 1])
        self.assertEqual(self.rc.idx, {1: {0, 1, 2}})

    def test_remove_from_empty_collection(self):
        """Test removing from an empty collection."""
        self.assertFalse(self.rc.remove(1))

    def test_remove_single_instance(self):
        """Test removing an element that appears once."""
        self.rc.insert(1)
        self.rc.insert(2)
        self.assertTrue(self.rc.remove(1))
        self.assertEqual(self.rc.lst, [2])
        self.assertEqual(self.rc.idx[1], set())
        self.assertEqual(self.rc.idx[2], {0})

    def test_remove_one_of_duplicates(self):
        """Test removing one instance of a duplicated element."""
        self.rc.insert(1)
        self.rc.insert(2)
        self.rc.insert(1)
        # self.lst is [1, 2, 1], self.idx is {1: {0, 2}, 2: {1}}
        self.assertTrue(self.rc.remove(1))
        # After removing one '1', we expect two elements to remain.
        # The exact state depends on which '1' was removed.
        # If '1' at index 0 is removed, last element ('1' at index 2) moves to index 0.
        # lst becomes [1, 2], idx becomes {1: {0}, 2: {1}}
        # If '1' at index 2 is removed, it's a simple pop.
        # lst becomes [1, 2], idx becomes {1: {0}, 2: {1}}
        self.assertEqual(len(self.rc.lst), 2)
        self.assertEqual(self.rc.lst.count(1), 1)
        self.assertEqual(self.rc.lst.count(2), 1)
        self.assertEqual(len(self.rc.idx[1]), 1)
        self.assertEqual(len(self.rc.idx[2]), 1)

    def test_remove_when_val_is_last_element(self):
        """Test removal when the element to be removed is the last one in the list."""
        self.rc.insert(1)
        self.rc.insert(2)
        # lst is [1, 2]
        self.assertTrue(self.rc.remove(2))
        self.assertEqual(self.rc.lst, [1])
        self.assertEqual(self.rc.idx, {1: {0}, 2: set()})

    def test_remove_when_swapped_element_is_same_as_removed(self):
        """Test case where the last element is the same as the one being removed."""
        self.rc.insert(1)
        self.rc.insert(2)
        self.rc.insert(1)
        # lst is [1, 2, 1], idx is {1: {0, 2}, 2: {1}}
        # If remove(1) picks index 0 to remove, it will be swapped with the last element, which is also 1.
        self.assertTrue(self.rc.remove(1))
        self.assertEqual(len(self.rc.lst), 2)
        self.assertEqual(self.rc.lst.count(1), 1)
        self.assertEqual(self.rc.lst.count(2), 1)
        self.assertEqual(len(self.rc.idx[1]), 1)

    def test_get_random_single_element(self):
        """Test getRandom when there is only one element."""
        self.rc.insert(100)
        self.assertEqual(self.rc.getRandom(), 100)
        self.assertEqual(self.rc.getRandom(), 100)

    def test_get_random_on_empty_raises_error(self):
        """Test that getRandom on an empty collection raises an IndexError."""
        with self.assertRaises(IndexError):
            self.rc.getRandom()

    def test_get_random_distribution(self):
        """Test if getRandom's distribution seems correct."""
        self.rc.insert(1)
        self.rc.insert(1)
        self.rc.insert(1)
        self.rc.insert(2)
        # We have [1, 1, 1, 2]. We expect '1' approx 75% of the time.
        counts = collections.Counter(self.rc.getRandom() for _ in range(1000))
        self.assertIn(1, counts)
        self.assertIn(2, counts)
        self.assertGreater(counts[1], 650)  # Should be ~750
        self.assertLess(counts[1], 850)
        self.assertGreater(counts[2], 150)  # Should be ~250
        self.assertLess(counts[2], 350)

    def test_get_random_after_removals(self):
        """Test getRandom after elements have been removed."""
        self.rc.insert(1)
        self.rc.insert(2)
        self.rc.insert(3)
        self.rc.insert(3)
        self.rc.remove(1)
        self.rc.remove(3)
        # Collection should now contain one 2 and one 3.
        # lst could be [3, 2] or [2, 3]
        self.assertEqual(len(self.rc.lst), 2)
        allowed_values = {2, 3}
        for _ in range(50):
            self.assertIn(self.rc.getRandom(), allowed_values)

    def test_complex_sequence(self):
        """Test a longer, more complex sequence of operations."""
        self.assertTrue(self.rc.insert(0))
        self.assertTrue(self.rc.insert(1))
        self.assertTrue(self.rc.remove(0))
        # lst is [1], idx is {0: set(), 1: {0}}
        self.assertTrue(self.rc.insert(2))
        self.assertFalse(self.rc.insert(1))
        # lst is [1, 2, 1], idx is {1: {0, 2}, 2: {1}}
        self.assertEqual(self.rc.getRandom(), 1)  # seeded random choice([1,2,1]) -> 1
        self.assertTrue(self.rc.remove(1))
        # lst is now some permutation of [1, 2]
        self.assertEqual(len(self.rc.lst), 2)
        self.assertTrue(self.rc.remove(1))
        # lst is [2]
        self.assertEqual(self.rc.lst, [2])
        self.assertTrue(self.rc.remove(2))
        self.assertEqual(self.rc.lst, [])
        self.assertFalse(self.rc.remove(2))

    def test_large_inputs(self):
        """Test with a large number of insertions and removals."""
        n = 10000
        # Insert n unique elements
        for i in range(n):
            self.assertTrue(self.rc.insert(i))

        # Insert n duplicates
        for i in range(n):
            self.assertFalse(self.rc.insert(i))

        self.assertEqual(len(self.rc.lst), 2 * n)

        # Remove half of the first copies
        for i in range(n // 2):
            self.assertTrue(self.rc.remove(i))

        self.assertEqual(len(self.rc.lst), 2 * n - (n // 2))

        # Check random is still valid
        for _ in range(100):
            val = self.rc.getRandom()
            self.assertIn(val, self.rc.idx)
            self.assertNotEqual(len(self.rc.idx[val]), 0)

        # Remove the rest
        all_keys = list(self.rc.idx.keys())
        for key in all_keys:
            while self.rc.idx[key]:
                self.assertTrue(self.rc.remove(key))

        self.assertEqual(len(self.rc.lst), 0)
        self.assertFalse(self.rc.remove(0))
        with self.assertRaises(IndexError):
            self.rc.getRandom()


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
