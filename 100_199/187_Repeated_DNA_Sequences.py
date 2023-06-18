class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = set()
        sequence_set = set()

        for i in range(len(s) - 9):
            substring = s[i:i + 10]

            if substring in sequence_set:
                result.add(substring)

            sequence_set.add(substring)

        return list(result)
