class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        utf8_bytes = 0

        for num in data:
            if utf8_bytes == 0:
                if num >> 5 == 0b110:
                    utf8_bytes = 1
                elif num >> 4 == 0b1110:
                    utf8_bytes = 2
                elif num >> 3 == 0b11110:
                    utf8_bytes = 3
                elif num >> 7 != 0:
                    return False
            else:
                if num >> 6 != 0b10:
                    return False

                utf8_bytes -= 1

        return utf8_bytes == 0
