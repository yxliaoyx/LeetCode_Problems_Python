class Solution:
    def calculate(self, s: str) -> int:
        current = 0
        num = 0
        result = 0

        operator = "+"

        for c in s + "+":
            if c.isdigit():
                num = 10 * num + int(c)

            if c in "+-*/":
                if operator == "+":
                    current += num
                elif operator == "-":
                    current -= num
                elif operator == "*":
                    current *= num
                elif operator == "/":
                    current = int(current / num)

                if c in "+-":
                    result += current
                    current = 0

                operator = c
                num = 0

        return result
