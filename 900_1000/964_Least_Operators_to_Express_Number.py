class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        pos = neg = k = 0

        while target:
            target, cur = divmod(target, x)
            if k:
                pos, neg = min(cur * k + pos, (cur + 1) * k + neg), min((x - cur) * k + pos, (x - cur - 1) * k + neg)
            else:
                pos = cur * 2
                neg = (x - cur) * 2

            k += 1

        return min(pos, k + neg) - 1
