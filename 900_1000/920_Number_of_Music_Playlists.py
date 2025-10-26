from functools import cache


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        @cache
        def dp(used, songs):
            if songs == 0:
                return 0 if used else 1

            count = 0
            if used > 0:
                count += dp(used - 1, songs - 1) * (n - used + 1)
            if n - used > k:
                count += dp(used, songs - 1) * (n - used - k)
            return count % 1_000_000_007

        return dp(n, goal)
