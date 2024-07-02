class MapSum:
    def __init__(self):
        self.data = {}

    def insert(self, key, val):
        self.data[key] = val

    def sum(self, prefix):
        return sum(val for key, val in self.data.items() if key.startswith(prefix))


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
