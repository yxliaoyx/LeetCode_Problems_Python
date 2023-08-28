from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = [nums.pop(0)]

        for n in nums:
            if n > subsequence[-1]:
                subsequence.append(n)
            else:
                subsequence[bisect_left(subsequence, n)] = n

        return len(subsequence)
