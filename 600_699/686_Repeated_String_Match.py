class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        min_repeat = (len(b) - 1) // len(a) + 1

        for i in range(min_repeat, min_repeat + 2):
            if b in a * i:
                return i

        return -1
