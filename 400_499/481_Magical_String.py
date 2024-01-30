class Solution:
    def magicalString(self, n: int) -> int:
        magic = [1, 2, 2]

        for i in range(2, n):
            # if magic[-1] == 1:
            #     magic += [2] * magic[i]
            # else:
            #     magic += [1] * magic[i]
            magic += [3 - magic[-1]] * magic[i]

        return magic[:n].count(1)
