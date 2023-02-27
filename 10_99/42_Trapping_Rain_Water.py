class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0

        for i, h in enumerate(height):
            while stack and h >= height[stack[-1]]:
                right_h = height[stack.pop()]

                if stack:
                    left = stack[-1]
                    water += min(height[left] - right_h, h - right_h) * (i - left - 1)

            stack.append(i)

        return water
