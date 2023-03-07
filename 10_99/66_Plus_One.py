class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return map(int, str(int(''.join(map(str, digits))) + 1))
