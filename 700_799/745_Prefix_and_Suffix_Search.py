from collections import defaultdict


class WordFilter:
    def __init__(self, words: List[str]):
        self.prefix_map = defaultdict(list)
        self.suffix_map = defaultdict(list)

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                self.prefix_map[word[:j]].append(i)
                self.suffix_map[word[j:]].append(i)

    def f(self, pref: str, suff: str) -> int:
        prefix_indices = self.prefix_map[pref]
        suffix_indices = self.suffix_map[suff]
        i = len(prefix_indices) - 1
        j = len(suffix_indices) - 1

        while i >= 0 and j >= 0:
            if prefix_indices[i] == suffix_indices[j]:
                return prefix_indices[i]

            if prefix_indices[i] > suffix_indices[j]:
                i -= 1
            else:
                j -= 1

        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
