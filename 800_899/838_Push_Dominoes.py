class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != "."]
        symbols = [(-1, "L")] + symbols + [(len(dominoes), "R")]
        dominoes = list(dominoes)

        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                dominoes[i + 1 : j] = [x] * (j - i - 1)
            elif x > y:
                mid = (j - i - 1) // 2
                dominoes[i + 1 : i + 1 + mid] = ["R"] * mid
                dominoes[j - mid : j] = ["L"] * mid

        return "".join(dominoes)
