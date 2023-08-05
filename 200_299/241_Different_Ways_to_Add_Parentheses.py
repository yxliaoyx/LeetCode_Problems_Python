from functools import cache


class Solution:
    @cache
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ways = []

        for i, c in enumerate(expression):
            if c in "+-*":
                for left in self.diffWaysToCompute(expression[:i]):
                    for right in self.diffWaysToCompute(expression[i + 1:]):
                        if c == '+':
                            ways.append(left + right)
                        elif c == '-':
                            ways.append(left - right)
                        else:
                            ways.append(left * right)

        if not ways:
            return [int(expression)]

        return ways
