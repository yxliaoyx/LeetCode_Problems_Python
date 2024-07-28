from collections import Counter
from functools import cache


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        def add(sticker, word):
            for char in sticker:
                word = word.replace(char, "", sticker[char])

            return word

        @cache
        def dfs(remaining):
            if not remaining:
                return 0

            min_stickers = float("inf")

            for sticker in stickers:
                if remaining[0] not in sticker:
                    continue

                new_remaining = add(sticker, remaining)
                min_stickers = min(min_stickers, 1 + dfs(new_remaining))

            return min_stickers

        stickers = [Counter(sticker) for sticker in stickers]
        result = dfs(target)

        return result if result != float("inf") else -1
