class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        cur = set()

        for a in arr:
            cur = {a} | {a | b for b in cur}
            res.update(cur)

        return len(res)
