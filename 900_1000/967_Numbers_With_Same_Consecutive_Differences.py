class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = list(range(1, 10))

        for _ in range(n - 1):
            result = [num * 10 + d for num in result for d in {num % 10 + k, num % 10 - k} if 0 <= d <= 9]

        return result
