class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return next((i for i in letters if i > target), letters[0])
