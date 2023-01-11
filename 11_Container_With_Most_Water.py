class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_amount = 0

        while height:
            if height[0] < height[-1]:
                max_amount = max(max_amount, height.pop(0) * len(height))
            else:
                max_amount = max(max_amount, height.pop(-1) * len(height))

        return max_amount
