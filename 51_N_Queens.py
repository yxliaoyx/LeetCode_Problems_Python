class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(queens, xy_sum, xy_dif):
            y = len(queens)

            if y == n:
                result.append(queens)
                return None

            for x in range(n):
                if x not in queens and x + y not in xy_sum and x - y not in xy_dif:
                    dfs(queens + [x], xy_sum + [x + y], xy_dif + [x - y])

        result = []

        dfs([], [], [])

        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]
