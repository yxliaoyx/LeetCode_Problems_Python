class Solution:
    def nearestPalindromic(self, n: str) -> str:
        palindromes = {10 ** len(n) + 1, 10 ** (len(n) - 1) - 1}
        prefix = int(n[: (len(n) + 1) // 2])

        for prefix in (prefix - 1, prefix, prefix + 1):
            prefix = str(prefix)

            if len(n) % 2:
                palindromes.add(int(prefix + prefix[:-1][::-1]))
            else:
                palindromes.add(int(prefix + prefix[::-1]))

        palindromes.discard(int(n))

        return str(min(palindromes, key=lambda x: (abs(int(n) - x), x)))
