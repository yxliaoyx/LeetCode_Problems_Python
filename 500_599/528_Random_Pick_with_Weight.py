from random import choices


class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        self.index_list = list(range(len(w)))

    def pickIndex(self) -> int:
        return choices(self.index_list, weights=self.w)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
