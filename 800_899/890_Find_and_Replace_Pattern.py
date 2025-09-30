class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def encode(word):
            mapping = {}
            return tuple(mapping.setdefault(char, len(mapping)) for char in word)

        pattern_code = encode(pattern)

        return [word for word in words if encode(word) == pattern_code]
