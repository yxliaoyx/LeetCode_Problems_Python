class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        current = 0

        for c in t:
            if c == s[current]:
                current += 1

                if current == len(s):
                    return True

        return False
