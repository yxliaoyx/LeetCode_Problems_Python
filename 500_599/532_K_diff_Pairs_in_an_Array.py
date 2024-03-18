from collections import Counter


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums_counter = Counter(nums)

        if k == 0:
            return sum(count > 1 for count in nums_counter.values())

        return sum(num + k in nums_counter for num in nums_counter.keys())
