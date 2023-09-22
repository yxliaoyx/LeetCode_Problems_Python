class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = 2147483647

        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True

        return False
