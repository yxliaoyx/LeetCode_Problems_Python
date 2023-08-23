class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        if len(pattern) != len(s):
            return False

        if len(set(pattern)) != len(set(s)):
            return False

        match = {}

        for i in range(len(s)):
            if pattern[i] not in match:
                match[pattern[i]] = s[i]

            elif match[pattern[i]] != s[i]:
                return False

        return True
