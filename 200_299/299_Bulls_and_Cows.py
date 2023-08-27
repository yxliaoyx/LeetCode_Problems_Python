from operator import eq


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = sum(map(eq, secret, guess))
        cows = sum(min(secret.count(c), guess.count(c)) for c in set(secret))

        return f"{bull}A{cows - bull}B"
