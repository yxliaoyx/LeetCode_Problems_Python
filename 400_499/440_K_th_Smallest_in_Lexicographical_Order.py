class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current = 1

        while k > 1:
            step = 0
            first = current
            last = current + 1

            while first <= n:
                step += min(n + 1, last) - first
                first *= 10
                last *= 10

            if step < k:
                k -= step
                current += 1
            else:
                k -= 1
                current *= 10

        return current
