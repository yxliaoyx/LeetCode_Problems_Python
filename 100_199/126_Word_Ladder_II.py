from collections import defaultdict


class Solution:
    def __init__(self):
        self.results = []

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def get_path(parent, path):
            for parent_word in parent[path[0]]:
                value = [parent_word] + path

                if parent_word == beginWord:
                    self.results.append(value)
                else:
                    get_path(parent, value)

        if endWord not in wordList:
            return []
        if beginWord == endWord:
            return [beginWord]

        parent = defaultdict(list)
        next_words = {beginWord}
        wordList = set(wordList)

        while next_words:
            diff1_words = set()
            wordList -= next_words

            for word in next_words:
                for i in range(len(word)):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        w = word[:i] + char + word[i + 1:]

                        if w in wordList:
                            diff1_words.add(w)
                            parent[w].append(word)

            if endWord in next_words:
                break

            next_words = diff1_words

        get_path(parent, [endWord])

        return self.results
