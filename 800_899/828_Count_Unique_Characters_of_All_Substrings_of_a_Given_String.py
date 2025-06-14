from string import ascii_uppercase


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        count = 0
        index = {c: [-1, -1] for c in ascii_uppercase}

        for i, c in enumerate(s):
            prev, curr = index[c]
            count += (i - curr) * (curr - prev)
            index[c] = [curr, i]

        for prev, curr in index.values():
            count += (len(s) - curr) * (curr - prev)

        return count
