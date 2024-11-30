from itertools import accumulate

from sortedcontainers import SortedDict


class MyCalendarThree:
    def __init__(self):
        self.lines = SortedDict()

    def book(self, startTime: int, endTime: int) -> int:
        self.lines[startTime] = self.lines.get(startTime, 0) + 1
        self.lines[endTime] = self.lines.get(endTime, 0) - 1

        return max(accumulate(self.lines.values()))


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
