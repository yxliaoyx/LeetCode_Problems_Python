class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [n for n in range(left, right + 1) if all(c != "0" and n % int(c) == 0 for c in str(n))]
