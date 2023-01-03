class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        start = 0

        for n, elem in enumerate(s):
            try:
                i = s.index(elem, start, n)
            except:
                i = start - 1

            longest = max(longest, n - i)
            start = i + 1

        return longest
