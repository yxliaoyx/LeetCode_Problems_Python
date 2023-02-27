class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)

        s_index = p_index = 0
        s_temp = p_temp = -1

        while s_index < s_len:
            if p_index < p_len and (p[p_index] == '?' or p[p_index] == s[s_index]):
                s_index += 1
                p_index += 1
            elif p_index < p_len and p[p_index] == '*':
                s_temp, p_temp = s_index + 1, p_index
                p_index += 1
            elif p_temp != -1:
                s_index, p_index = s_temp, p_temp
            else:
                return False

        return p[p_index:].count("*") == p_len - p_index
