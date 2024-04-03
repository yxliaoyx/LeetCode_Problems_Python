class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))

        i = next((i for i in reversed(range(len(s) - 1)) if s[i] < s[i + 1]), -1)

        if i == -1:
            return -1

        j = next(j for j in reversed(range(i, len(s))) if s[j] > s[i])

        s[i], s[j] = s[j], s[i]
        s[i + 1 :] = reversed(s[i + 1 :])
        element = int("".join(s))

        return element if element < 2147483648 else -1
