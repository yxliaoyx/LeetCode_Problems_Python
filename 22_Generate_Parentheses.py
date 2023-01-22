class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]

        combinations = ["()"]

        for i in range(1, n):
            parentheses = []
            for c in combinations:
                for j in range(i - 1, len(c)):
                    parentheses.append(c[:j] + "()" + c[j:])
            combinations = list(set(parentheses))

        return combinations
