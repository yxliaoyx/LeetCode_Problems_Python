from collections import Counter
from heapq import heappop, heappush


class FreqStack:
    def __init__(self):
        self.counter = Counter()
        self.idx = 0
        self.heap = []

    def push(self, val):
        self.counter[val] += 1
        heappush(self.heap, (-self.counter[val], -self.idx, val))
        self.idx += 1

    def pop(self):
        val = heappop(self.heap)[2]
        self.counter[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
