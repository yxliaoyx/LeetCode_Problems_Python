class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = {}

        for i in range(len(arr)):
            dp[arr[i]] = 1

            for j in range(i):
                if arr[i] % arr[j] == 0:
                    right = arr[i] // arr[j]

                    if right in dp:
                        dp[arr[i]] += dp[arr[j]] * dp[right]

        return sum(dp.values()) % 1_000_000_007
