class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = {letter: i for i, letter in enumerate(s)}

        result = []

        for i, letter in enumerate(s):
            if letter not in result:
                while result and i < d[result[-1]] and letter < result[-1]:
                    result.pop()

                result.append(letter)

        return "".join(result)
