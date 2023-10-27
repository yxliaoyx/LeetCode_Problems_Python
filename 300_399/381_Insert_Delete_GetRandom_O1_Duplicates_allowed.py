from collections import defaultdict
from random import choice


class RandomizedCollection:
    def __init__(self):
        self.data_dict = defaultdict(set)
        self.data_list = []

    def insert(self, val: int) -> bool:
        self.data_dict[val].add(len(self.data_list))
        self.data_list.append(val)

        return len(self.data_dict[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.data_dict[val]:
            return False

        index, last_val = self.data_dict[val].pop(), self.data_list[-1]

        self.data_list[index] = last_val
        self.data_dict[last_val].add(index)
        self.data_dict[last_val].discard(len(self.data_list) - 1)

        self.data_list.pop()

        return True

    def getRandom(self) -> int:
        return choice(self.data_list)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
