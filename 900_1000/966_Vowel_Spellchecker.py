class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        answer = []
        word_set = set(wordlist)
        lower_map = {}
        vowel_map = {}

        def devowel(w):
            return "".join("*" if c in "aeiou" else c for c in w)

        for word in wordlist:
            low = word.lower()
            lower_map.setdefault(low, word)
            vowel_map.setdefault(devowel(low), word)

        for q in queries:
            low = q.lower()

            if q in word_set:
                answer.append(q)
            elif low in lower_map:
                answer.append(lower_map[low])
            else:
                answer.append(vowel_map.get(devowel(low), ""))

        return answer
