class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = [""]

        for char in s:
            if char.isalpha():
                res = [item + c for item in res for c in (char.lower(), char.upper())]
            else:
                res = [item + char for item in res]

        return res
