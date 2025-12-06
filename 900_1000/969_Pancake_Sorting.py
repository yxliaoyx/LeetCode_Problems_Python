class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flip = []

        for size in range(len(arr), 1, -1):
            i = arr.index(size) + 1

            arr[:i] = reversed(arr[:i])
            arr[:size] = reversed(arr[:size])

            flip += [i, size]

        return flip
