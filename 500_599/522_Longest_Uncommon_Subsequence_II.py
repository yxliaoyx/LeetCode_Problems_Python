class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_sub(a: str, b: str) -> bool:
            iter_b = iter(b)

            return all(char in iter_b for char in a)


        strs.sort(key=lambda s: -len(s))

        for i, str_i in enumerate(strs):
            if all(not is_sub(str_i, str_j) for j, str_j in enumerate(strs) if j != i):
                return len(str_i)

        return -1
