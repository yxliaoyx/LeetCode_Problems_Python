class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        backward = {}
        result = []

        for i, word in enumerate(words):
            backward[word[::-1]] = i

        for i, word in enumerate(words):
            if word in backward and backward[word] != i:
                result.append([i, backward[word]])

            if word != "" and "" in backward and word == word[::-1]:
                result.extend([[i, backward[""]], [backward[""], i]])

            for j in range(len(word)):
                if word[j:] in backward and word[:j] == word[j - 1::-1]:
                    result.append([backward[word[j:]], i])

                if word[:j] in backward and word[j:] == word[:j - 1:-1]:
                    result.append([i, backward[word[:j]]])

        return result
