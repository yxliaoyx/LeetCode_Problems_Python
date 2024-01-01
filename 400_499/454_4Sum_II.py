from collections import Counter


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sums = Counter(i + j for i in nums1 for j in nums2)
        return sum(sums.get(-k - l, 0) for k in nums3 for l in nums4)
