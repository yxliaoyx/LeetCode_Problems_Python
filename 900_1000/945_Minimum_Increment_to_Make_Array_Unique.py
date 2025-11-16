class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        next_num = -1

        for num in nums:
            if num <= next_num:
                next_num += 1
                moves += next_num - num
            else:
                next_num = num

        return moves
