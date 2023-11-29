class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        bits = 1
        nums_sum = sum(nums)

        if nums_sum & 1:
            return False

        for num in nums:
            bits |= bits << num

        return bits & (1 << (nums_sum >> 1))
