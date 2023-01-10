import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        print(re.fullmatch(p, s))
