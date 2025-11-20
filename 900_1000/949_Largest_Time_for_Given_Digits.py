from itertools import permutations


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        for h1, h2, m1, m2 in permutations(sorted(arr, reverse=True)):
            if (h1, h2) < (2, 4) and m1 < 6:
                return f"{h1}{h2}:{m1}{m2}"
        return ""
