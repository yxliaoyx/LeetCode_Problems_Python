class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left = right = 0
        result = set()

        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                if left > 0:
                    left -= 1
                else:
                    right += 1

        def recurse(string, index, left_count, right_count, left_remain, right_remain, expr):
            if index == len(string):
                if left_remain == 0 and right_remain == 0:
                    result.add("".join(expr))
            else:
                if (string[index] == "(" and left_remain > 0) or (string[index] == ")" and right_remain > 0):
                    recurse(string,
                            index + 1,
                            left_count,
                            right_count,
                            left_remain - (string[index] == "("),
                            right_remain - (string[index] == ")"),
                            expr)

                expr.append(string[index])

                if string[index] != "(" and string[index] != ")":
                    recurse(string,
                            index + 1,
                            left_count,
                            right_count,
                            left_remain,
                            right_remain,
                            expr)

                elif string[index] == "(":
                    recurse(string,
                            index + 1,
                            left_count + 1,
                            right_count,
                            left_remain,
                            right_remain,
                            expr)

                elif string[index] == ")" and left_count > right_count:
                    recurse(string,
                            index + 1,
                            left_count,
                            right_count + 1,
                            left_remain,
                            right_remain,
                            expr)

                expr.pop()

        recurse(s, 0, 0, 0, left, right, [])

        return result
