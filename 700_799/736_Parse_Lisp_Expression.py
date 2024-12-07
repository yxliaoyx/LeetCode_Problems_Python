from collections import deque


class Solution:
    def evaluate(self, expression: str) -> int:
        tokens = deque(expression.replace("(", "( ").replace(")", " )").split())

        def eva(tokens, env):
            token = tokens.popleft()

            if token == "(":
                token = tokens.popleft()

                if token in ("add", "mult"):
                    a, b = eva(tokens, env), eva(tokens, env)
                    val = a + b if token == "add" else a * b
                else:  # let expression
                    local = env.copy()

                    while tokens[0] != "(" and tokens[1] != ")":
                        var = tokens.popleft()
                        local[var] = eva(tokens, local)

                    val = eva(tokens, local)

                tokens.popleft()  # remove ')'
            else:
                val = int(token) if token[0] in "-0123456789" else env[token]

            return val

        return eva(tokens, {})
