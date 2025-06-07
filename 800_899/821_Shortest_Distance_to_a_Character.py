class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        result = [0] * n
        last_position = -n

        for i in range(n):
            if s[i] == c:
                last_position = i
            result[i] = i - last_position

        last_position = 2 * n

        for i in range(n - 1, -1, -1):
            if s[i] == c:
                last_position = i
            result[i] = min(result[i], last_position - i)

        return result
