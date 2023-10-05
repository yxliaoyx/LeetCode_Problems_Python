from sortedcontainers import SortedSet


class SummaryRanges:
    def __init__(self):
        self.treemap = SortedSet()

    def addNum(self, value: int) -> None:
        self.treemap.add(value)

    def getIntervals(self) -> List[List[int]]:
        result = []

        for num in self.treemap:
            if result and result[-1][1] + 1 == num:
                result[-1][1] = num
            else:
                result.append([num, num])

        return result

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
