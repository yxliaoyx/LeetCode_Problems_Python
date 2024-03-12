class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_length = 0
        table = {0: -1}

        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1

            if count in table:
                max_length = max(max_length, (i - table[count]))
            else:
                table[count] = i

        return max_length
