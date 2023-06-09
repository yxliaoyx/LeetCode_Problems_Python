class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'

        result = []

        if numerator * denominator < 0:
            result.append('-')

        numerator, denominator = abs(numerator), abs(denominator)

        quotient, remainder = divmod(numerator, denominator)
        result.append(str(quotient))

        if remainder == 0:
            return ''.join(result)

        result.append('.')

        appeared = {}

        while remainder != 0:
            if remainder in appeared:
                result.insert(appeared[remainder], '(')
                result.append(')')
                break

            appeared[remainder] = len(result)
            quotient, remainder = divmod(remainder * 10, denominator)
            result.append(str(quotient))

        return ''.join(result)
