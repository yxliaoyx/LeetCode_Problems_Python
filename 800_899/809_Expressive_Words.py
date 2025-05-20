from itertools import groupby


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def get_char_groups(word):
            return zip(*[(char, len(list(group))) for char, group in groupby(word)])

        s_chars, s_counts = get_char_groups(s)
        expressive_count = 0

        for word in words:
            w_chars, w_counts = get_char_groups(word)
            if s_chars == w_chars:
                if all(sc >= max(wc, 3) or sc == wc for sc, wc in zip(s_counts, w_counts)):
                    expressive_count += 1

        return expressive_count
