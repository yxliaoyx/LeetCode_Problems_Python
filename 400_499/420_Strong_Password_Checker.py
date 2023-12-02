from heapq import heapify, heappop, heappush
from itertools import groupby


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        missing_type = 0 if any([c.isdigit() for c in password]) else 1
        missing_type += 0 if any([c.islower() for c in password]) else 1
        missing_type += 0 if any([c.isupper() for c in password]) else 1

        if len(password) < 6:
            return max(6 - len(password), missing_type)

        repeat = [len(list(g)) for _, g in groupby(password)]
        repeat = [r for r in repeat if r > 2]

        if len(password) > 20:
            repeat = [(r % 3, r) for r in repeat]
            heapify(repeat)

            for i in range(len(password) - 20):
                if not repeat:
                    break

                _, r = heappop(repeat)

                if r > 3:
                    heappush(repeat, ((r - 1) % 3, r - 1))

            repeat = [r for _, r in repeat]

        return max(missing_type, sum(r // 3 for r in repeat)) + max(0, len(password) - 20)
