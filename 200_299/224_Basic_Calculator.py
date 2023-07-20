class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        result = 0
        sign = 1
        stack = [sign]

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '(':
                stack.append(sign)
            elif c == ')':
                stack.pop()
            elif c in '+-':
                result += sign * num
                sign = stack[-1] if c == '+' else -stack[-1]
                num = 0

        return result + sign * num
