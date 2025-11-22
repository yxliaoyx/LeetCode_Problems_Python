from collections import Counter


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        max_num = max(nums)
        parents = list(range(max_num + 1))
        nums = set(nums)

        def find(u):
            if parents[u] != u:
                parents[u] = find(parents[u])
            return parents[u]

        for i in range(2, max_num + 1):
            for j in range(i, max_num + 1, i):
                if j in nums:
                    parents[find(i)] = find(j)

        return max(Counter(find(num) for num in nums).values())
