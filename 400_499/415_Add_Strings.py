class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        result = ""

        i1 = len(num1) - 1
        i2 = len(num2) - 1

        while i1 >= 0 or i2 >= 0 or carry:
            n1 = ord(num1[i1]) - ord("0") if i1 >= 0 else 0
            n2 = ord(num2[i2]) - ord("0") if i2 >= 0 else 0

            carry, remainder = divmod(n1 + n2 + carry, 10)
            result = f"{remainder}{result}"

            i1 -= 1
            i2 -= 1

        return result
