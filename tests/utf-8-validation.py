
import unittest

# Canonical solution
class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """

        # Number of bytes in the current UTF-8 character
        n_bytes = 0

        # For each integer in the data array.
        for num in data:

            # Get the binary representation. We only need the least significant 8 bits
            # for any given number.
            bin_rep = format(num, '#010b')[-8:]

            # If this is the case then we are to start processing a new UTF-8 character.
            if n_bytes == 0:

                # Get the number of 1s in the beginning of the string.
                for bit in bin_rep:
                    if bit == '0': break
                    n_bytes += 1

                # 1 byte characters
                if n_bytes == 0:
                    continue

                # Invalid scenarios according to the rules of the problem.
                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:
                # Else, we are processing integers which represent bytes which are a part of
                # a UTF-8 character. So, they must adhere to the pattern `10xxxxxx`.
                if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                    return False

            # We reduce the number of bytes to process by 1 after each integer.
            n_bytes -= 1

        # This is for the case where we might not have the complete data for
        # a particular UTF-8 character.
        return n_bytes == 0


class TestValidUtf8(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertTrue(self.solution.validUtf8([]))

    def test_valid_single_byte_characters(self):
        self.assertTrue(self.solution.validUtf8([0]))
        self.assertTrue(self.solution.validUtf8([127]))
        self.assertTrue(self.solution.validUtf8([10, 20, 30, 40]))
        self.assertTrue(self.solution.validUtf8([0, 0, 0, 0]))

    def test_valid_two_byte_characters(self):
        self.assertTrue(self.solution.validUtf8([197, 130]))
        self.assertTrue(self.solution.validUtf8([223, 191])) # Max values
        self.assertTrue(self.solution.validUtf8([192, 128])) # Min values
        self.assertTrue(self.solution.validUtf8([197, 130, 200, 150]))

    def test_valid_three_byte_characters(self):
        self.assertTrue(self.solution.validUtf8([224, 130, 130]))
        self.assertTrue(self.solution.validUtf8([239, 191, 191])) # Max values
        self.assertTrue(self.solution.validUtf8([224, 128, 128])) # Min values
        self.assertTrue(self.solution.validUtf8([225, 130, 140, 230, 150, 160]))

    def test_valid_four_byte_characters(self):
        self.assertTrue(self.solution.validUtf8([240, 130, 130, 130]))
        self.assertTrue(self.solution.validUtf8([247, 191, 191, 191])) # Max values
        self.assertTrue(self.solution.validUtf8([240, 128, 128, 128])) # Min values
        self.assertTrue(self.solution.validUtf8([241, 130, 140, 150, 242, 160, 170, 180]))

    def test_valid_mixed_characters(self):
        self.assertTrue(self.solution.validUtf8([197, 130, 1]))
        self.assertTrue(self.solution.validUtf8([240, 159, 146, 150, 10, 226, 130, 172]))

    def test_invalid_incomplete_multibyte(self):
        self.assertFalse(self.solution.validUtf8([197]))
        self.assertFalse(self.solution.validUtf8([224, 130]))
        self.assertFalse(self.solution.validUtf8([240, 130, 130]))
        self.assertFalse(self.solution.validUtf8([10, 20, 30, 241]))

    def test_invalid_continuation_byte_placement(self):
        self.assertFalse(self.solution.validUtf8([130, 130])) # Starts with continuation
        self.assertFalse(self.solution.validUtf8([128])) # Starts with continuation
        self.assertFalse(self.solution.validUtf8([191])) # Starts with continuation
        self.assertFalse(self.solution.validUtf8([10, 20, 130, 40])) # Continuation without start
        self.assertFalse(self.solution.validUtf8([197, 10])) # Invalid second byte
        self.assertFalse(self.solution.validUtf8([224, 130, 10])) # Invalid third byte
        self.assertFalse(self.solution.validUtf8([240, 130, 130, 10])) # Invalid fourth byte
        self.assertFalse(self.solution.validUtf8([235, 140, 4])) # Leetcode example

    def test_invalid_start_byte(self):
        self.assertFalse(self.solution.validUtf8([248, 130, 130, 130, 130])) # 5-byte sequence
        self.assertFalse(self.solution.validUtf8([252, 130, 130, 130, 130, 130])) # 6-byte sequence
        self.assertFalse(self.solution.validUtf8([254])) # Invalid start
        self.assertFalse(self.solution.validUtf8([255])) # Invalid start
        self.assertFalse(self.solution.validUtf8([192])) # Overlong encoding, but invalid by problem's rule of incomplete sequence
        
    def test_values_over_255(self):
        # The solution correctly handles this by only looking at the last 8 bits.
        # 300 % 256 = 44 (00101100, 1-byte char). [44, 130, 1] is invalid.
        self.assertFalse(self.solution.validUtf8([300, 130, 1]))
        # 450 % 256 = 194 (11000010, 2-byte start). [194, 130] is valid.
        self.assertTrue(self.solution.validUtf8([450, 130]))
        # 511 % 256 = 255 (11111111, invalid start).
        self.assertFalse(self.solution.validUtf8([511]))

    def test_large_valid_inputs(self):
        large_single_byte = [100] * 10000
        self.assertTrue(self.solution.validUtf8(large_single_byte))
        large_multi_byte = [240, 130, 130, 130] * 2500
        self.assertTrue(self.solution.validUtf8(large_multi_byte))
        large_mixed = ([197, 130] * 2000) + ([10] * 2000) + ([224, 130, 130] * 2000)
        self.assertTrue(self.solution.validUtf8(large_mixed))

    def test_large_invalid_inputs(self):
        large_valid_prefix = [100] * 10000
        invalid_at_end = large_valid_prefix + [197]
        self.assertFalse(self.solution.validUtf8(invalid_at_end))

        large_valid_prefix_2 = [224, 130, 130] * 5000
        invalid_at_end_2 = large_valid_prefix_2 + [130]
        self.assertFalse(self.solution.validUtf8(invalid_at_end_2))

        large_valid_prefix_3 = [100] * 10000
        invalid_in_middle = [100] * 5000 + [255] + [100] * 5000
        self.assertFalse(self.solution.validUtf8(invalid_in_middle))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
