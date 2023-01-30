class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        substring_len = len(words) * word_len
        result = []

        for left in range(word_len):
            d = Counter(words)

            for right in range(left, len(s) - word_len + 1, word_len):
                word = s[right : right + word_len]
                d[word] -= 1

                while d[word] < 0:
                    d[s[left : left + word_len]] += 1
                    left += word_len

                if left + substring_len == right + word_len:
                    result.append(left)

        return result
