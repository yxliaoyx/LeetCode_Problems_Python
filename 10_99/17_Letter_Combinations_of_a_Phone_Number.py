import itertools


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        if not digits:
            return []

        return list(map(''.join, [i for i in itertools.product(*(mapping[n] for n in digits))]))


print(Solution().letterCombinations('23'))
