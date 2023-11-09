class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "]":
                number = ""
                word = ""

                while stack[-1] != "[":
                    word = stack.pop() + word
                else:
                    stack.pop()

                while stack and stack[-1].isdigit():
                    number = stack.pop() + number

                stack.append(int(number) * word)
            else:
                stack.append(c)

        return "".join(stack)
