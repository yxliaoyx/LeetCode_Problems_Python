import re


class Solution:
    def myAtoi(self, s: str) -> int:
        try:
            return max(-2147483648, min(int(re.search(r'^ *[-+]?\d+', s).group()), 2147483647))
        except:
            return 0
