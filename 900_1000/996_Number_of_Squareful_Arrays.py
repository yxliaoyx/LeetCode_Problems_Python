from collections import Counter
from math import isqrt


class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def is_square(n):
            r = isqrt(n)
            return r * r == n

        counter = Counter(nums)

        def backtrack(path):
            if len(path) == len(nums):
                return 1
            total = 0
            for num in counter:
                if counter[num] > 0 and (not path or is_square(path[-1] + num)):
                    counter[num] -= 1
                    total += backtrack(path + [num])
                    counter[num] += 1
            return total

        return backtrack([])
