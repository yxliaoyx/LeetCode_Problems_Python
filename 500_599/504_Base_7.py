class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        if num < 0:
            sign = "-"
            num = -num
        else:
            sign = ""

        digits = []

        while num > 0:
            digits.append(str(num % 7))
            num //= 7

        return sign + "".join(reversed(digits))
