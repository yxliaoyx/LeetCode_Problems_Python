from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        wordList = set(wordList)

        while queue:
            word, level = queue.popleft()

            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    w = word[:i] + char + word[i + 1:]

                    if w in wordList and w not in visited:
                        if w == endWord:
                            return level + 1

                        queue.append((w, level + 1))
                        visited.add(w)

        return 0
