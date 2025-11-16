class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 0:
            columnNumber -= 1
            # Get the last character and append it at the end of string.
            ans += chr(columnNumber % 26 + ord("A"))
            columnNumber //= 26

        # Reverse it, as we appended characters in reverse order.
        return ans[::-1]