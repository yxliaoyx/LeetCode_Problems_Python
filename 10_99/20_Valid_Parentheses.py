class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracket = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        for char in s:
            if char in bracket:
                stack.append(char)
            else:
                try:
                    if char != bracket[stack.pop()]:
                        return False
                except IndexError:
                    return False

        return not bool(stack)
