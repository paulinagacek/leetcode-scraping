import unittest


class TestLFUCache(unittest.TestCase):

    def test_leetcode_example(self):
        cache = LFUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 3)
        cache.put(4, 4)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_capacity_zero(self):
        cache = LFUCache(0)
        cache.put(1, 1)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(len(cache.key2val), 0)

    def test_capacity_one(self):
        cache = LFUCache(1)
        cache.put(1, 10)
        self.assertEqual(cache.get(1), 10)
        cache.put(2, 20)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 20)
        cache.put(2, 22)
        self.assertEqual(cache.get(2), 22)

    def test_update_existing_key(self):
        cache = LFUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.put(1, 10)
        self.assertEqual(cache.get(1), 10)
        # At this point, freq of 1 is 3, freq of 2 is 1. minf is 1.
        cache.put(3, 3)  # Should evict key 2
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 10)
        self.assertEqual(cache.get(3), 3)

    def test_get_non_existent_key(self):
        cache = LFUCache(2)
        cache.put(1, 1)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 1)
        # Ensure getting a non-existent key does not alter the state
        self.assertEqual(cache.minf, 2)

    def test_lfu_eviction_logic(self):
        cache = LFUCache(3)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        # All have freq 1.
        cache.get(1)  # freq(1)=2
        cache.get(1)  # freq(1)=3
        cache.get(2)  # freq(2)=2
        # Frequencies: {1:3, 2:2, 3:1}
        # minf is 1
        cache.put(4, 4)  # Should evict key 3 (LFU)
        self.assertEqual(cache.get(3), -1)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(4), 4)

    def test_lru_tie_breaking(self):
        cache = LFUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        # Both keys have frequency 1. Key 1 was inserted first, so it's the LRU.
        cache.put(3, 3)  # Should evict key 1
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(3), 3)

    def test_lru_tie_breaking_after_get(self):
        cache = LFUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(1)  # Freq(1)=2, Freq(2)=1. Key 1 is now most frequent.
        cache.put(3, 3)  # Should evict key 2 (LFU)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(3), 3)

    def test_lru_tie_breaking_complex(self):
        cache = LFUCache(3)
        cache.put(1, 1)  # Freq {1:1}
        cache.put(2, 2)  # Freq {1:1, 2:1}
        cache.put(3, 3)  # Freq {1:1, 2:1, 3:1}
        # LRU in freq 1 list: 1, 2, 3
        cache.get(1)  # Freq {2:1, 3:1}, {1:2}. minf=1. LRU in freq 1: 2, 3
        cache.get(2)  # Freq {3:1}, {1:2, 2:2}. minf=1. LRU in freq 2: 1, 2
        cache.put(4, 4)  # Evict LFU key 3
        self.assertEqual(cache.get(3), -1)
        # Freq {4:1}, {1:2, 2:2}. minf=1. LRU in freq 2: 1, 2
        cache.put(5, 5)  # Evict LFU key 4
        self.assertEqual(cache.get(4), -1)
        # Freq {5:1}, {1:2, 2:2}. minf=1. LRU in freq 2: 1, 2
        cache.put(6, 6)  # Evict LFU key 5
        self.assertEqual(cache.get(5), -1)
        # Freq {6:1}, {1:2, 2:2}. minf=1. LRU in freq 2: 1, 2
        cache.put(7, 7)  # Evict LFU key 6
        self.assertEqual(cache.get(6), -1)
        # Freq {7:1}, {1:2, 2:2}. minf=1. LRU in freq 2: 1, 2
        cache.put(8, 8)  # Evict LFU key 7
        self.assertEqual(cache.get(7), -1)
        # Freq {8:1}, {1:2, 2:2}. minf=1. LRU in freq 2: 1, 2
        cache.put(9, 9)  # Evict LFU key 8
        self.assertEqual(cache.get(8), -1)
        # Freq {9:1}, {1:2, 2:2}. minf=1. LRU in freq 2: 1, 2
        cache.put(10, 10)  # Evict LFU key 9
        self.assertEqual(cache.get(9), -1)
        # Freq {10:1}, {1:2, 2:2}. minf=1. LRU in freq 2: 1, 2
        cache.put(11, 11)  # Evict LFU key 10
        self.assertEqual(cache.get(10), -1)
        # Freq {11:1}, {1:2, 2:2}. minf=1. LRU in freq 2: 1, 2
        cache.put(12, 12)  # Evict LFU key 1, LRU of freq 2
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), 2)

    def test_large_capacity(self):
        capacity = 1000
        cache = LFUCache(capacity)
        # Fill the cache
        for i in range(capacity):
            cache.put(i, i)

        # Check if all items are present
        for i in range(capacity):
            self.assertEqual(cache.get(i), i)

        # Now all items have frequency 2.
        # Access first half again to make them more frequent
        for i in range(capacity // 2):
            cache.get(i)

        # Frequencies: 0 to 499 have freq 3, 500 to 999 have freq 2. minf = 2
        # LRU of freq 2 is key 500.
        cache.put(capacity, capacity)  # Add a new item

        # Key 500 should be evicted
        self.assertEqual(cache.get(500), -1)
        self.assertEqual(cache.get(499), 499)
        self.assertEqual(cache.get(501), 501)
        self.assertEqual(cache.get(capacity), capacity)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
