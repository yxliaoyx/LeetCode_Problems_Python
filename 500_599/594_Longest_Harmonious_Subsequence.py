from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)

        return max((count[i] + count[i + 1] for i in count if i + 1 in count), default=0)
