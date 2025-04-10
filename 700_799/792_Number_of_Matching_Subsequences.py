class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def is_subsequence(word):
            pos = 0
            for char in word:
                pos = s.find(char, pos) + 1
                if pos == 0:
                    return False

            return True

        return sum(map(is_subsequence, words))
