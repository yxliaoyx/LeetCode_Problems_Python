from sortedcontainers import SortedList


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []
        sorted_list = SortedList(nums[: k - 1])

        for i in range(k - 1, len(nums)):
            sorted_list.add(nums[i])

            if k % 2 == 0:
                median = (sorted_list[k // 2 - 1] + sorted_list[k // 2]) / 2
            else:
                median = sorted_list[k // 2]

            result.append(median)
            sorted_list.remove(nums[i - k + 1])

        return result
