from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []

        for i in range(len(nums)):
            if dq and dq[0] == i - k:
                dq.popleft()

            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()

            dq.append(i)
            result.append(nums[dq[0]])

        return result[k - 1:]
