class Solution:
    def shortestSuperstring(self, words):
        def get_overlap(word1, word2):
            for i in range(min(len(word1), len(word2)), 0, -1):
                if word1[-i:] == word2[:i]:
                    return word2[i:]
            return word2

        n = len(words)
        overlaps = [[get_overlap(words[i], words[j]) for j in range(n)] for i in range(n)]
        dp = [[""] * n for _ in range(1 << n)]

        for mask in range(1, 1 << n):
            for last in range(n):
                if mask & (1 << last):
                    prev_mask = mask ^ (1 << last)
                    if not prev_mask:
                        dp[mask][last] = words[last]
                    else:
                        dp[mask][last] = min(
                            (dp[prev_mask][k] + overlaps[k][last] for k in range(n) if prev_mask & (1 << k)),
                            key=len,
                        )

        return min(dp[-1], key=len)
