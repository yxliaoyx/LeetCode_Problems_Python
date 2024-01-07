from collections import defaultdict, OrderedDict


class LFUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.frequency_dict = defaultdict(OrderedDict)
        self.min_frequency = 0
        self.capacity = capacity

    def insert(self, key, frequency, value):
        self.cache[key] = (frequency, value)
        self.frequency_dict[frequency][key] = value

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        frequency, value = self.cache[key]
        del self.frequency_dict[frequency][key]

        if not self.frequency_dict[frequency]:
            del self.frequency_dict[frequency]
            if frequency == self.min_frequency:
                self.min_frequency += 1

        self.insert(key, frequency + 1, value)

        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.cache:
            frequency = self.cache[key][0]
            self.cache[key] = (frequency, value)
            self.get(key)
            return

        if self.capacity == len(self.cache):
            key_to_delete, frequency = self.frequency_dict[self.min_frequency].popitem(last=False)
            del self.cache[key_to_delete]

        self.min_frequency = 1
        self.insert(key, 1, value)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
