class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if tx == sx:
                return (ty - sy) % sx == 0
            if ty == sy:
                return (tx - sx) % sy == 0

            if ty > tx:
                ty %= tx
            else:
                tx %= ty

        return False
