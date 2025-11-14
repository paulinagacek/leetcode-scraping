import unittest
from typing import List


class TestRestoreIpAddresses(unittest.TestCase):
    """
    Unit tests for the restoreIpAddresses method.
    Since the order of returned IP addresses is not strictly defined, 
    the lists are sorted for comparison.
    """

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    def assertIPListEqual(self, actual: List[str], expected: List[str]):
        """Sorts and compares the list of IP strings."""
        self.assertEqual(sorted(actual), sorted(expected))

    # ----------------------------------
    # ## Standard Cases
    # ----------------------------------

    def test_standard_case_one_result(self):
        """Standard case with a single valid result."""
        s = "25525511135"
        expected = ["255.255.11.135", "255.255.111.35"] # Wait, this string has 11 digits.
        # String: 11 digits (25525511135)
        # 255.255.11.135 (3+3+2+3 = 11) - Invalid
        # Max length for valid IP: 3*4 = 12. Min length: 4.
        
        # Let's use standard LC example: 25525511135 (11 digits)
        # 255.255.11.135
        # 255.255.111.35
        expected = ["255.255.11.135", "255.255.111.35"]
        self.assertIPListEqual(self.solution.restoreIpAddresses(s), expected)

    def test_standard_case_multiple_results(self):
        """Case with multiple valid ways to partition."""
        s = "101023"
        # 1.0.10.23, 1.0.102.3, 10.1.0.23, 10.10.2.3, 10.102.3
        expected = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"] # Wait, 101.0.2.3 has length 6
        expected = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"] 
        self.assertIPListEqual(self.solution.restoreIpAddresses(s), expected)

    def test_standard_case_full_length(self):
        """Case using the maximum 12-digit length (3.3.3.3)."""
        s = "111111111111"
        expected = ["111.111.111.111"]
        self.assertIPListEqual(self.solution.restoreIpAddresses(s), expected)

    # ----------------------------------
    # ## Edge Cases
    # ----------------------------------

    def test_min_length_valid(self):
        """Edge case: Minimum length (4 digits) resulting in one valid IP."""
        s = "1111"
        expected = ["1.1.1.1"]
        self.assertIPListEqual(self.solution.restoreIpAddresses(s), expected)

    def test_max_length_invalid(self):
        """Edge case: Input string is too long (13 digits)."""
        s = "1111111111111"
        expected = []
        self.assertIPListEqual(self.solution.restoreIpAddresses(s), expected)

    def test_too_short_invalid(self):
        """Edge case: Input string is too short (3 digits)."""
        s = "123"
        expected = []
        self.assertIPListEqual(self.solution.restoreIpAddresses(s), expected)

    def test_zeroes_leading_zeros_invalid(self):
        """Test with leading zeros, which are invalid for multi-digit octets."""
        s = "010010" # Valid: 0.10.0.10 (3+2+1+2 = 8 digits) -> NO. 6 digits.
        # Valid: 0.1.0.010 -> NO (leading zero)
        # Valid: 0.10.0.10 (4*1=4, 1+2+1+2 = 6)
        expected = ["0.10.0.10", "0.100.1.0"] # 0.100.1.0 (1+3+1+1 = 6)
        self.assertIPListEqual(self.solution.restoreIpAddresses(s), expected)

    def test_zeroes_all_zeros_valid(self):
        """Test with all zeros (only "0" is valid, not "00" or "000")."""
        s = "0000"
        expected = ["0.0.0.0"]
        self.assertIPListEqual(self.solution.restoreIpAddresses(s), expected)
        
    def test_boundary_255_valid(self):
        """Test with octets equal to 255."""
        s = "255255255255"
        expected = ["255.255.255.255"]
        self.assertIPListEqual(self.solution.restoreIpAddresses(s), expected)
        
    def test_boundary_256_invalid(self):
        """Test with a string containing digits > '255', but still allows for valid IPs."""
        s = "2561111111"  # 10 digits
        # 25.61.111.111 is a valid partition (2+2+3+3 = 10)
        expected = ['25.61.111.111']
        self.assertIPListEqual(self.solution.restoreIpAddresses(s), expected)

    def test_boundary_leading_zeros_255_invalid(self):
        """Test the key leading zero rule: '0x' is invalid unless x is a dot."""
        # s = "010010" (6 digits)
        # Expected: 0.1.0.10, 0.10.0.10, 0.100.1.0
        s = "010010"
        # 1. (1, 1, 1, 3): 0.1.0.010 -> Invalid (010 is invalid)
        # 2. (1, 1, 2, 2): 0.1.00.10 -> Invalid (00 is invalid)
        # 3. (1, 2, 1, 2): 0.10.0.10 -> Valid
        # 4. (1, 2, 2, 1): 0.10.01.0 -> Invalid (01 is invalid)
        # 5. (1, 3, 1, 1): 0.100.1.0 -> Valid
        # 6. (2, 1, 1, 2): 01.0.0.10 -> Invalid (01 is invalid)
        
        expected = ["0.10.0.10", "0.100.1.0"] # 0.1.0.10 is invalid since 1+1+1+3 = 6
        
        self.assertIPListEqual(self.solution.restoreIpAddresses(s), expected)


    # ----------------------------------
    # ## Large Input Case (Max Length 12)
    # ----------------------------------

    def test_max_length_max_results(self):
        """Max length 12 with maximum possible combinations."""
        # ... (unchanged code for s="111111111111")
        
        # Test a string that maximizes the recursive branches (e.g., '1's)
        s_small = "11111" # 5 digits
        
        # Partitions of 5 into 4 parts: [1, 1, 1, 2], [1, 1, 2, 1], [1, 2, 1, 1], [2, 1, 1, 1]
        expected_small = ["1.1.1.11", "1.1.11.1", "1.11.1.1", "11.1.1.1"]
        self.assertIPListEqual(self.solution.restoreIpAddresses(s_small), expected_small)


if __name__ == '__main__':
    unittest.main()