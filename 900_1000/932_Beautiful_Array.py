class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        array = [1]

        while len(array) < n:
            array = [x * 2 - 1 for x in array] + [x * 2 for x in array]

        return [x for x in array if x <= n]
