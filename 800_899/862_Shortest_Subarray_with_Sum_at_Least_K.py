from collections import deque
from itertools import accumulate
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        dq = deque()
        result = float("inf")
        prefix_sums = [0] + list(accumulate(nums))

        for i, current_sum in enumerate(prefix_sums):
            while dq and current_sum - prefix_sums[dq[0]] >= k:
                result = min(result, i - dq.popleft())

            while dq and current_sum <= prefix_sums[dq[-1]]:
                dq.pop()

            dq.append(i)

        return result if result != float("inf") else -1
