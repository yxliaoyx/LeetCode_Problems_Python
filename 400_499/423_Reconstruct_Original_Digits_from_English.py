from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        counter = Counter(s)
        result = [0] * 10

        result[0] = counter["z"]
        result[2] = counter["w"]
        result[4] = counter["u"]
        result[6] = counter["x"]
        result[8] = counter["g"]
        result[1] = counter["o"] - result[0] - result[2] - result[4]
        result[3] = counter["r"] - result[0] - result[4]
        result[5] = counter["f"] - result[4]
        result[7] = counter["v"] - result[5]
        result[9] = counter["i"] - result[5] - result[6] - result[8]

        return "".join(str(digit) * count for digit, count in enumerate(result))
