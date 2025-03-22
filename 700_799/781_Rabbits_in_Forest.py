from collections import Counter
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        return sum((answer + num) // (answer + 1) * (answer + 1) for answer, num in count.items())
