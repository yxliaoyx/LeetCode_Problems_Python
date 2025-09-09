class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {x: i for i, x in enumerate(arr)}
        dp = {}

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                prev = arr[j] - arr[i]

                if prev < arr[i] and prev in index:
                    dp[(i, j)] = dp.get((index[prev], i), 2) + 1

        return max(dp.values()) if dp else 0
