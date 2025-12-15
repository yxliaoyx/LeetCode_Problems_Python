from collections import Counter


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        pairs = Counter(a & b for a in nums for b in nums)
        return sum(v for x in nums for k, v in pairs.items() if x & k == 0)
