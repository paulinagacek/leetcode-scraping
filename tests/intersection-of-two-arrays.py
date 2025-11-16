import unittest


class TestIntersection(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_basic_case_1(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        expected = [2]
        self.assertCountEqual(self.solution.intersection(nums1, nums2), expected)

    def test_basic_case_2(self):
        nums1 = [4, 9, 5]
        nums2 = [9, 4, 9, 8, 4]
        expected = [4, 9]
        self.assertCountEqual(self.solution.intersection(nums1, nums2), expected)

    def test_no_intersection(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        expected = []
        self.assertCountEqual(self.solution.intersection(nums1, nums2), expected)

    def test_empty_first_list(self):
        nums1 = []
        nums2 = [1, 2, 3]
        expected = []
        self.assertCountEqual(self.solution.intersection(nums1, nums2), expected)

    def test_empty_second_list(self):
        nums1 = [1, 2, 3]
        nums2 = []
        expected = []
        self.assertCountEqual(self.solution.intersection(nums1, nums2), expected)

    def test_both_lists_empty(self):
        nums1 = []
        nums2 = []
        expected = []
        self.assertCountEqual(self.solution.intersection(nums1, nums2), expected)

    def test_identical_lists(self):
        nums1 = [1, 2, 3, 4, 5]
        nums2 = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertCountEqual(self.solution.intersection(nums1, nums2), expected)

    def test_one_list_is_subset(self):
        nums1 = [1, 2]
        nums2 = [1, 2, 3, 4]
        expected = [1, 2]
        self.assertCountEqual(self.solution.intersection(nums1, nums2), expected)

    def test_with_duplicates(self):
        nums1 = [1, 1, 2, 2, 3, 3]
        nums2 = [2, 2, 3, 3, 4, 4]
        expected = [2, 3]
        self.assertCountEqual(self.solution.intersection(nums1, nums2), expected)

    def test_with_negative_numbers(self):
        nums1 = [-1, -2, 0, 5]
        nums2 = [0, -2, 8, -10]
        expected = [-2, 0]
        self.assertCountEqual(self.solution.intersection(nums1, nums2), expected)

    def test_with_zero(self):
        nums1 = [0, 0, 1]
        nums2 = [0, 2]
        expected = [0]
        self.assertCountEqual(self.solution.intersection(nums1, nums2), expected)

    def test_single_element_lists(self):
        nums1 = [1]
        nums2 = [1]
        expected = [1]
        self.assertCountEqual(self.solution.intersection(nums1, nums2), expected)

    def test_single_element_no_intersection(self):
        nums1 = [1]
        nums2 = [2]
        expected = []
        self.assertCountEqual(self.solution.intersection(nums1, nums2), expected)

    def test_large_input_with_intersection(self):
        nums1 = list(range(1000))
        nums2 = list(range(500, 1500))
        expected = list(range(500, 1000))
        self.assertCountEqual(self.solution.intersection(nums1, nums2), expected)

    def test_large_input_no_intersection(self):
        nums1 = list(range(10000))
        nums2 = list(range(10000, 20000))
        expected = []
        self.assertCountEqual(self.solution.intersection(nums1, nums2), expected)

    def test_large_input_with_duplicates(self):
        nums1 = [i for i in range(500) for _ in range(3)]
        nums2 = [i for i in range(250, 750) for _ in range(5)]
        expected = list(range(250, 500))
        self.assertCountEqual(self.solution.intersection(nums1, nums2), expected)

    def test_large_input_one_element_intersection(self):
        nums1 = list(range(10000))
        nums2 = list(range(9999, 20000))
        expected = [9999]
        self.assertCountEqual(self.solution.intersection(nums1, nums2), expected)

    def test_large_input_full_overlap(self):
        nums1 = list(range(5000))
        nums2 = list(range(5000))
        expected = list(range(5000))
        self.assertCountEqual(self.solution.intersection(nums1, nums2), expected)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
