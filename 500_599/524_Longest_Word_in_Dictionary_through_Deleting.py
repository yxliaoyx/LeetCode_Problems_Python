class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        for word in sorted(dictionary, key=lambda x: (-len(x), x)):
            iter_s = iter(s)

            if all(char in iter_s for char in word):
                return word

        return ""
