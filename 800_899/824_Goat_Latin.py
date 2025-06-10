class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        def ma(i, word):
            if word[0] not in "aeiouAEIOU":
                word = word[1:] + word[0]

            return word + "ma" + ("a" * i)

        return " ".join([ma(i, w) for i, w in enumerate(sentence.split(), 1)])
