class MagicDictionary:
    def __init__(self):
        self.dictionary = set()

    def buildDict(self, dictionary: List[str]) -> None:
        self.dictionary = set(dictionary)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c != searchWord[i] and searchWord[:i] + c + searchWord[i + 1 :] in self.dictionary:
                    return True

        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
