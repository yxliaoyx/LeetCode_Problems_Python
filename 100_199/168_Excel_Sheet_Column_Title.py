class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ""

        while columnNumber > 0:
            title = f"{chr(65 + (columnNumber - 1) % 26)}{title}"  # ord("A") = 65
            columnNumber = (columnNumber - 1) // 26

        return title
