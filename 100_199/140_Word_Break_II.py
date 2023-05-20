from functools import cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @cache
        def helper(s):
            results = []

            if s in wordDict:
                results.append(s)

            for i in range(1, len(s)):
                if s[:i] in wordDict:
                    for sentences in helper(s[i:]):
                        results.extend([f"{s[:i]} {sentences}"])

            return results

        return helper(s)
