from bisect import bisect
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.meta = defaultdict(list)
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.meta[key].append(timestamp)
        self.data[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect(self.meta[key], timestamp)
        return self.data[key][i - 1] if i else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
