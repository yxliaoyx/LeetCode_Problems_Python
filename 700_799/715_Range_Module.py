from bisect import bisect_left, bisect_right


class RangeModule:
    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        i, j = bisect_left(self.ranges, left), bisect_right(self.ranges, right)
        self.ranges[i:j] = [left] * (i % 2 == 0) + [right] * (j % 2 == 0)

    def queryRange(self, left: int, right: int) -> bool:
        i, j = bisect_right(self.ranges, left), bisect_left(self.ranges, right)
        return i == j and i % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        i, j = bisect_left(self.ranges, left), bisect_right(self.ranges, right)
        self.ranges[i:j] = [left] * (i % 2 == 1) + [right] * (j % 2 == 1)


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
