class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {c: i for i, c in enumerate(s)}
        partitions, end = [0], 0

        for i, c in enumerate(s):
            end = max(end, last_index[c])

            if end == i:
                partitions.append(1 + end - sum(partitions))

        return partitions[1:]
