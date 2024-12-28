class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = [i.lower() for i in licensePlate if i.isalpha()]

        for word in sorted(words, key=len):
            if all(word.count(char) >= licensePlate.count(char) for char in licensePlate):
                return word
