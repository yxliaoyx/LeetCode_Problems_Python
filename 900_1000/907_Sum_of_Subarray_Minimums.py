class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        dp = [0] * len(arr)

        for i, num in enumerate(arr):
            while stack and num < arr[stack[-1]]:
                stack.pop()

            prev_i = stack[-1] if stack else -1
            dp[i] = dp[prev_i] + (i - prev_i) * num
            stack.append(i)

        return sum(dp) % 1_000_000_007
