import unittest


class TestTrapRainWaterII(unittest.TestCase):
    def setUp(self):
        """Set up the test case."""
        self.solution = Solution()

    def test_example_1(self):
        """Test the first example from LeetCode."""
        height_map = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
        self.assertEqual(self.solution.trapRainWater(height_map), 4)

    def test_example_2(self):
        """Test the second example from LeetCode."""
        height_map = [
            [3, 3, 3, 3, 3],
            [3, 2, 2, 2, 3],
            [3, 2, 1, 2, 3],
            [3, 2, 2, 2, 3],
            [3, 3, 3, 3, 3],
        ]
        self.assertEqual(self.solution.trapRainWater(height_map), 10)

    def test_edge_case_one_row(self):
        """Test a grid with only one row, which cannot trap water."""
        height_map = [[10, 8, 12, 5, 15]]
        self.assertEqual(self.solution.trapRainWater(height_map), 0)

    def test_edge_case_one_column(self):
        """Test a grid with only one column, which cannot trap water."""
        height_map = [[10], [8], [12], [5], [15]]
        self.assertEqual(self.solution.trapRainWater(height_map), 0)

    def test_edge_case_2xN_grid(self):
        """Test a 2xN grid, which cannot trap water."""
        height_map = [[10, 8, 12, 5], [15, 9, 7, 11]]
        self.assertEqual(self.solution.trapRainWater(height_map), 0)

    def test_flat_surface(self):
        """Test a grid where all cells have the same height."""
        height_map = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
        self.assertEqual(self.solution.trapRainWater(height_map), 0)

    def test_simple_bowl(self):
        """Test a simple 4x4 bowl shape."""
        height_map = [
            [10, 10, 10, 10],
            [10, 2, 2, 10],
            [10, 2, 2, 10],
            [10, 10, 10, 10],
        ]
        self.assertEqual(self.solution.trapRainWater(height_map), 32)  # (10-2)*4

    def test_central_peak(self):
        """Test a grid with a high point in the center, no water trapped."""
        height_map = [
            [1, 2, 3, 2, 1],
            [2, 3, 5, 3, 2],
            [3, 5, 10, 5, 3],
            [2, 3, 5, 3, 2],
            [1, 2, 3, 2, 1],
        ]
        self.assertEqual(self.solution.trapRainWater(height_map), 0)

    def test_descending_slope(self):
        """Test a grid that is a continuous slope, no water trapped."""
        height_map = [[12, 11, 10], [9, 8, 7], [6, 5, 4]]
        self.assertEqual(self.solution.trapRainWater(height_map), 0)

    def test_leaking_bowl(self):
        """Test a bowl shape with a leak on one of the walls."""
        height_map = [[10, 10, 10, 10], [10, 2, 2, 10], [10, 5, 5, 10], [10, 10, 1, 10]]
        # Water level is limited by the '1' leaking point.
        # (5-2)*2 + (5-5)*2 = 6
        self.assertEqual(self.solution.trapRainWater(height_map), 6)

    def test_complex_terrain(self):
        """Test a more complex terrain with multiple peaks and valleys."""
        height_map = [
            [12, 13, 1, 12],
            [13, 4, 13, 12],
            [13, 8, 10, 12],
            [12, 13, 12, 12],
            [13, 13, 13, 13],
        ]
        self.assertEqual(self.solution.trapRainWater(height_map), 14)

    def test_walls_are_lowest(self):
        """Test a case where the boundary walls are the lowest points."""
        height_map = [[5, 5, 5, 5], [5, 10, 10, 5], [5, 10, 10, 5], [5, 5, 5, 5]]
        self.assertEqual(self.solution.trapRainWater(height_map), 0)

    def test_large_bowl(self):
        """Test a large grid forming a bowl to check performance and correctness."""
        size = 50
        wall_height = 100
        floor_height = 10
        height_map = [[floor_height] * size for _ in range(size)]

        for i in range(size):
            height_map[i][0] = wall_height
            height_map[i][size - 1] = wall_height
            height_map[0][i] = wall_height
            height_map[size - 1][i] = wall_height

        expected_water = (size - 2) * (size - 2) * (wall_height - floor_height)
        self.assertEqual(self.solution.trapRainWater(height_map), expected_water)

    def test_large_flat_land_with_random_walls(self):
        """Test a large flat area with high surrounding walls."""
        size = 100
        height_map = [[1] * size for _ in range(size)]

        for i in range(size):
            height_map[i][0] = 50
            height_map[i][size - 1] = 40
            height_map[0][i] = 30
            height_map[size - 1][i] = 20

        # The lowest boundary point is 20, so water will fill up to height 20.
        expected_water = (size - 2) * (size - 2) * (20 - 1)
        self.assertEqual(self.solution.trapRainWater(height_map), expected_water)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
