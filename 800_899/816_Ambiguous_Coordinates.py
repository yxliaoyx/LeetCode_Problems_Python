from itertools import product


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def make(frag):
            for i in range(1, len(frag) + 1):
                left, right = frag[:i], frag[i:]
                if (left == "0" or not left.startswith("0")) and not right.endswith("0"):
                    yield left + (f".{right}" if right else "")

        s = s.strip("()")
        return [f"({a}, {b})" for i in range(1, len(s)) for a, b in product(make(s[:i]), make(s[i:]))]
