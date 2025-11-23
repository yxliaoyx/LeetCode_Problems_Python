class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        map = {c: i for i, c in enumerate(order)}
        return words == sorted(words, key=lambda w: [map[c] for c in w])
