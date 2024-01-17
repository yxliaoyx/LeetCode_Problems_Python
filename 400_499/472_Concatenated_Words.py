from functools import cache


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words_set = set(words)

        @cache
        def dfs(word):
            for i in range(1, len(word)):
                if word[:i] in words_set and (word[i:] in words_set or dfs(word[i:])):
                    return True

            return False

        return [word for word in words if dfs(word)]
