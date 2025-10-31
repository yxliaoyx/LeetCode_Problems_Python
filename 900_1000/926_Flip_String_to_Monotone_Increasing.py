class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = flip = 0

        for c in s:
            if c == "1":
                ones += 1
            elif ones:
                ones -= 1
                flip += 1

        return flip
