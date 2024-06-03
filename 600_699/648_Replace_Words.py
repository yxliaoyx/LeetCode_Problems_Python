class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}

        for word in dictionary:
            node = trie

            for char in word:
                node = node.setdefault(char, {})

            node["#"] = word

        def find_root(word: str) -> str:
            node = trie

            for char in word:
                node = node.get(char, {})

                if "#" in node:
                    return node["#"]

            return word

        return " ".join(find_root(word) for word in sentence.split())
