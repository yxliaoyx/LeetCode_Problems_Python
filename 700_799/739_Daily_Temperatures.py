class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        warmer = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                warmer[stack.pop()] = i - stack[-1]

            stack.append(i)

        return warmer
