class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        result = [""] * len(s)
        total_shift = 0

        for i in range(len(s) - 1, -1, -1):
            total_shift += shifts[i]
            result[i] = chr((ord(s[i]) - 97 + total_shift) % 26 + 97)

        return "".join(result)
