class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie

        for w in word:
            node = node.setdefault(w, {})

        node["end"] = False

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if not node:
                return False

            if i == len(word):
                return "end" in node

            if word[i] == ".":
                for child in node.values():
                    if dfs(child, i + 1):
                        return True
            else:
                if word[i] in node:
                    return dfs(node[word[i]], i + 1)
                else:
                    return False

            return False

        return dfs(self.trie, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
