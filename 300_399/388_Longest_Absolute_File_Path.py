class Solution:
    def lengthLongestPath(self, input: str) -> int:
        result = 0
        stack = [0]

        for path in input.split("\n"):
            p = path.split("\t")
            depth, name = len(p) - 1, p[-1]

            while len(stack) > depth + 1:
                stack.pop()

            if "." in name:
                result = max(result, stack[-1] + len(name))
            else:
                stack.append(stack[-1] + len(name) + 1)

        return result
