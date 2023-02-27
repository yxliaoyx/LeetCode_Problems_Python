class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest = 0

        left = right = 0
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1

            if left == right:
                longest = max(longest, left + right)
            elif left < right:
                left = right = 0

        left = right = 0
        for char in s[::-1]:
            if char == '(':
                left += 1
            else:
                right += 1

            if left == right:
                longest = max(longest, left + right)
            elif left > right:
                left = right = 0

        return longest
