class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        current = []
        justified = []
        word_len_sum = 0

        for word in words:
            if word_len_sum + len(word) + len(current) > maxWidth:
                for i in range(maxWidth - word_len_sum):
                    current[i % (len(current) - 1 or 1)] += ' '

                justified.append(''.join(current))
                current = []
                word_len_sum = 0

            current += [word]
            word_len_sum += len(word)

        return justified + [' '.join(current).ljust(maxWidth)]
