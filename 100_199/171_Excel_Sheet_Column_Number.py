class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        for i in columnTitle:
            result = result * 26 + ord(i) - 64  # ord("A") - 1 = 64

        return result
