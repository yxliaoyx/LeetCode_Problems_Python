class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        steps = 0

        while target > startValue:
            target = target // 2 if target % 2 == 0 else target + 1
            steps += 1

        return steps + startValue - target
