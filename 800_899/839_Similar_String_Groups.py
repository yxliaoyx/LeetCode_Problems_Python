from collections import deque


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def similar(s1, s2):
            diff = 0
            for a, b in zip(s1, s2):
                if a != b:
                    diff += 1
                    if diff > 2:
                        return False

            return diff == 2 or diff == 0

        strs = set(strs)
        groups = 0

        while strs:
            queue = deque([strs.pop()])
            while queue:
                cur = queue.popleft()
                for nxt in list(strs):
                    if similar(cur, nxt):
                        strs.remove(nxt)
                        queue.append(nxt)
            groups += 1

        return groups
