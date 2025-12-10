class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = [1] + [0] * (k - 1)
        total = prefix = 0

        for num in nums:
            prefix = (prefix + num) % k
            total += count[prefix]
            count[prefix] += 1

        return total
