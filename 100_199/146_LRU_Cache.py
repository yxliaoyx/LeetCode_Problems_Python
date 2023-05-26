import collections


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        try:
            self.cache.move_to_end(key)
            return self.cache[key]
        except KeyError:
            return -1

    def put(self, key: int, value: int) -> None:
        try:
            self.cache.move_to_end(key)
            self.cache[key] = value
        except KeyError:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)

            self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
