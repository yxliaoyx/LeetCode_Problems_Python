class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        answers = []

        def recurse(index, previous, current, value, string):
            if index == len(num):
                if value == target and current == 0:
                    answers.append("".join(string[1:]))
                return

            current = current * 10 + int(num[index])

            if current > 0:
                recurse(index + 1, previous, current, value, string)

            recurse(index + 1, current, 0, value + current, string + ["+", str(current)])

            if string:
                recurse(index + 1, -current, 0, value - current, string + ["-", str(current)])
                recurse(index + 1, current * previous, 0, value - previous + (current * previous),
                        string + ["*", str(current)])

        recurse(0, 0, 0, 0, [])

        return answers
