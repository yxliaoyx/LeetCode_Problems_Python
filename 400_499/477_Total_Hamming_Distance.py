class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        distance = 0

        for i in range(32):
            count_1 = 0

            for num in nums:
                count_1 += num >> i & 1

            distance += (len(nums) - count_1) * count_1

        return distance
