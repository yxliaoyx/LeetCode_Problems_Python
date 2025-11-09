class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        target = list(target)
        result = []

        def place_stamp(i):
            if all(stamp[j] == target[i + j] or target[i + j] == "?" for j in range(len(stamp))):
                target[i : i + len(stamp)] = ["?"] * len(stamp)
                return [i]
            return []

        for index in range(len(target) - len(stamp) + 1):
            result.extend(place_stamp(index))

        for index in range(len(target) - len(stamp), -1, -1):
            result.extend(place_stamp(index))

        return result[::-1] if all(c == "?" for c in target) else []
