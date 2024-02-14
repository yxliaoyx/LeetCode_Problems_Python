from sortedcontainers import SortedList


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        pairs = 0
        sorted_list = SortedList([])

        for i in range(len(nums) - 1):
            sorted_list.add(nums[i])
            pairs += i + 1 - sorted_list.bisect_right(nums[i + 1] * 2)

        return pairs
