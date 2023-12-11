from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        queue = deque([(startGene, 0)])

        while queue:
            gene, count = queue.popleft()

            for i in range(8):
                for char in ("A", "C", "G", "T"):
                    mutation = gene[:i] + char + gene[i + 1:]

                    if mutation in bank:
                        if mutation == endGene:
                            return count + 1

                        queue.append((mutation, count + 1))
                        bank.remove(mutation)

        return -1
