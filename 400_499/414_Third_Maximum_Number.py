class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = -2147483649

        for num in nums:
            if num in {first, second, third}:
                continue

            if num > first:
                first, second, third = num, first, second
            elif num > second:
                second, third = num, second
            elif num > third:
                third = num

        if third == -2147483649:
            return first

        return third
