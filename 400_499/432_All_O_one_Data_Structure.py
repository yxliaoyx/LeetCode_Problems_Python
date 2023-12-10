from collections import defaultdict


class AllOne:
    def __init__(self):
        self.bucket = defaultdict(set)
        self.counter = defaultdict(int)
        self.max_count = 0

    def inc(self, key: str) -> None:
        self.bucket[self.counter[key]].discard(key)
        self.counter[key] += 1
        self.bucket[self.counter[key]].add(key)
        self.max_count = max(self.max_count, self.counter[key])

    def dec(self, key: str) -> None:
        if self.max_count == self.counter[key] and len(self.bucket[self.counter[key]]) == 1:
            self.max_count -= 1

        self.bucket[self.counter[key]].discard(key)

        if self.counter[key] > 1:
            self.counter[key] -= 1
            self.bucket[self.counter[key]].add(key)
        else:
            del self.counter[key]

    def getMaxKey(self) -> str:
        return next(iter(self.bucket[self.max_count])) if self.max_count else ""

    def getMinKey(self) -> str:  # run in O(n) average time complexity
        if self.max_count == 0:
            return ""

        for min_count in iter(self.bucket):
            if self.bucket[min_count]:
                return next(iter(self.bucket[min_count]))

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
