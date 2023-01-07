class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            r = int('-' + str(x)[:0:-1])
            if r >= -2147483648:
                return r
        else:
            r = int(str(x)[::-1])
            if r <= 2147483647:
                return r

        return 0
