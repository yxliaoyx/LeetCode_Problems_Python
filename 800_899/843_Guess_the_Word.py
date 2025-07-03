# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:


class Solution:
    def findSecretWord(self, words: List[str], master: "Master") -> None:
        candidates = set(words)

        while candidates:
            word = candidates.pop()
            matches = master.guess(word)
            if matches == 6:
                return

            candidates = {w for w in candidates if sum(a == b for a, b in zip(word, w)) == matches}
