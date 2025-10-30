class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0

        for char in typed:
            if i < len(name) and name[i] == char:
                i += 1
            elif i == 0 or char != name[i - 1]:
                return False

        return i == len(name)
