from itertools import zip_longest


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(s):
            skip = 0
            for a in reversed(s):
                if a == "#":
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield a

        return all(a == b for a, b in zip_longest(process(s), process(t)))
