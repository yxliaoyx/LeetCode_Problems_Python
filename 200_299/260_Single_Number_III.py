class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = single = 0

        for num in nums:
            x ^= num

        mask = x & -x

        for num in nums:
            if num & mask:
                single ^= num

        return [single, single ^ x]
