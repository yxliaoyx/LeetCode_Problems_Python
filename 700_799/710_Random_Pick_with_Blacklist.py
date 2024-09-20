from random import randrange


class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.white_len = n - len(blacklist)
        self.hashmap = {}

        blacklist = set(blacklist)
        n -= 1

        for b in blacklist:
            if b < self.white_len:
                while n in blacklist:
                    n -= 1

                self.hashmap[b] = n
                n -= 1

    def pick(self) -> int:
        seed = randrange(self.white_len)
        return self.hashmap.get(seed, seed)


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
