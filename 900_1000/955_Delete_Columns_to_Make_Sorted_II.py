class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        final = [""] * len(strs)

        for col in zip(*strs):
            temp = [r + c for r, c in zip(final, col)]
            if temp == sorted(temp):
                final = temp

        return len(strs[0]) - len(final[0])
