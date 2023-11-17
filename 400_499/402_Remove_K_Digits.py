class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"

        stack = []

        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        return "".join(stack[:len(stack) - k]).lstrip("0") or "0"
