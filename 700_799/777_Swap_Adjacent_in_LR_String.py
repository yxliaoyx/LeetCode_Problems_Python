class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        def filter_x(s):
            return [(index, char) for index, char in enumerate(s) if char != "X"]

        start_filtered = filter_x(start)
        result_filtered = filter_x(result)

        if len(start_filtered) != len(result_filtered):
            return False

        for (i, c), (j, w) in zip(start_filtered, result_filtered):
            if c != w or (c == "L" and i < j) or (c == "R" and i > j):
                return False

        return True
