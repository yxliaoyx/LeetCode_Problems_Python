from functools import reduce


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(reduce(int.__xor__, map(ord, s + t)))
