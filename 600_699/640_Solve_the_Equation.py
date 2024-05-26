import re


class Solution:
    def solveEquation(self, equation: str) -> str:
        x = a = 0
        side = 1

        for eq, sign, num, isx in re.findall(r"(=)|([-+]?)(\d*)(x?)", equation):
            if eq:
                side = -1
            elif isx:
                x += side * int(sign + "1") * int(num or 1)
            elif num:
                a -= side * int(sign + num)

        return f"x={a // x}" if x else "No solution" if a else "Infinite solutions"
