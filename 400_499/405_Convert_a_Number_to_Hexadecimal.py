class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        if num < 0:
            num += 2 ** 32

        hex_map = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        result = ""

        while num > 0:
            result = hex_map[num % 16] + result
            num //= 16

        return result
