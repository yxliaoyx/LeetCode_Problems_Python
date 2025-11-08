class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        A = 4  # 1, 3, 7, 9
        B = 2  # 4, 6
        C = 2  # 2, 8
        D = 1  # 0
        MOD = 1_000_000_007

        for _ in range(n - 1):
            A, B, C, D = 2 * (B + C) % MOD, A, A + 2 * D % MOD, C

        return (A + B + C + D) % MOD
