from fractions import Fraction


class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions = list(map(Fraction, expression.replace("+", " +").replace("-", " -").split()))
        result = sum(fractions)

        return str(result.numerator) + "/" + str(result.denominator)
