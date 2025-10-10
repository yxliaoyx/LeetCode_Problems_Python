class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        d_len, n_len = len(digits), len(str(n))
        ans = sum(d_len**i for i in range(1, n_len))

        for i, c in enumerate(str(n)):
            ans += sum(digit < c for digit in digits) * (d_len ** (n_len - i - 1))
            if c not in digits:
                break
        else:
            ans += 1

        return ans
