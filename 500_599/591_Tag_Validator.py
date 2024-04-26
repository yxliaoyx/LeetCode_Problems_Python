class Solution:
    def isValid(self, code: str) -> bool:
        i = 0
        stack = []

        while i < len(code):
            if i > 0 and not stack:
                return False

            if code.startswith("<![CDATA[", i):
                i = code.find("]]>", i + 9)

                if i < 0:
                    return False

                i += 2

            elif code.startswith("</", i):
                j = i + 2
                i = code.find(">", j)

                if i < 0:
                    return False

                tag = code[j:i]

                if not stack or stack.pop() != tag:
                    return False

                i += 1

            elif code.startswith("<", i):
                j = i + 1
                i = code.find(">", j)

                if i < 0 or i == j or i - j > 9:
                    return False

                tag = code[j:i]

                if not tag.isupper() or not tag.isalpha():
                    return False

                stack.append(tag)
                i += 1

            else:
                i += 1

        return not stack
