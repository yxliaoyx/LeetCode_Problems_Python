class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        ones = [i for i, d in enumerate(arr) if d == 1]

        if not ones:
            return [0, 2]
        if len(ones) % 3 != 0:
            return [-1, -1]

        i, j, k = ones[0], ones[len(ones) // 3], ones[len(ones) // 3 * 2]
        length = len(arr) - k

        if arr[i : i + length] == arr[j : j + length] == arr[k:]:
            return [i + length - 1, j + length]

        return [-1, -1]
