class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while True:
            if target > numbers[left] + numbers[right]:
                left += 1
            elif target < numbers[left] + numbers[right]:
                right -= 1
            else:
                return [left + 1, right + 1]
