import re
from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        matcher = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)", formula)
        stack = [defaultdict(int)]

        for atom, count, left, right, multiplier in matcher:
            if atom:
                stack[-1][atom] += int(count or 1)
            elif left:
                stack.append(defaultdict(int))
            elif right:
                curr_map = stack.pop()

                for atom, num in curr_map.items():
                    stack[-1][atom] += num * int(multiplier or 1)

        return "".join(f"{atom}{num if num > 1 else ''}" for atom, num in sorted(stack[0].items()))
