class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        chain_end = -1001
        chain_len = 0

        pairs.sort(key=lambda x: x[1])

        for pair in pairs:
            if chain_end < pair[0]:
                chain_end = pair[1]
                chain_len += 1

        return chain_len
