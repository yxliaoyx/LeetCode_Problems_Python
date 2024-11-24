class MyCalendarTwo:
    def __init__(self):
        self.overlaps = []
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.overlaps:
            if startTime < end and start < endTime:
                return False

        for start, end in self.calendar:
            if startTime < end and start < endTime:
                self.overlaps.append((max(startTime, start), min(endTime, end)))

        self.calendar.append((startTime, endTime))

        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
