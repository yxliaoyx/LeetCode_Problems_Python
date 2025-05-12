class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        possible = set()
        total = sum(nums)
        n = len(nums)

        nums = sorted(num * n - total for num in nums)

        for num in nums[:-1]:
            possible.update({num + x for x in possible if x < 0})
            possible.add(num)

            if 0 in possible:
                return True

        return False
