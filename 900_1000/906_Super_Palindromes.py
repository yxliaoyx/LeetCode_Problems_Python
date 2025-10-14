class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left, right = int(left), int(right)
        count = 0

        for s in range(1, 100000):
            s = str(s)
            for p in [s + s[::-1], s[:-1] + s[::-1]]:
                square = int(p) ** 2
                if left <= square <= right and str(square) == str(square)[::-1]:
                    count += 1

        return count
