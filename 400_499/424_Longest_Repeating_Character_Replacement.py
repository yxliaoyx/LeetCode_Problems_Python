from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count = result = 0

        repeat_counter = defaultdict(int)

        for i, char in enumerate(s):
            repeat_counter[char] += 1
            max_count = max(max_count, repeat_counter[char])

            if result - max_count < k:
                result += 1
            else:
                repeat_counter[s[i - result]] -= 1

        return result
