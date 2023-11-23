class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        pairs = set()

        for char in s:
            if char in pairs:
                length += 2
                pairs.remove(char)
            else:
                pairs.add(char)

        if pairs:
            return length + 1
        else:
            return length
