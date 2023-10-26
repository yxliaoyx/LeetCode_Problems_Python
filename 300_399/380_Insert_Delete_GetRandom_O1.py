from random import choice


class RandomizedSet:
    def __init__(self):
        self.data_dict = {}
        self.data_list = []

    def insert(self, val: int) -> bool:
        if val in self.data_dict:
            return False

        self.data_dict[val] = len(self.data_list)
        self.data_list.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_dict:
            return False

        self.data_dict[self.data_list[-1]] = self.data_dict[val]
        self.data_list[self.data_dict[val]] = self.data_list[-1]

        self.data_dict.pop(val)
        self.data_list.pop()

        return True

    def getRandom(self) -> int:
        return choice(self.data_list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
