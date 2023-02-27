class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ''

        for zip_str in list(zip(*strs)):
            if len(set(zip_str)) == 1:
                s += zip_str[0]
            else:
                break

        return s
