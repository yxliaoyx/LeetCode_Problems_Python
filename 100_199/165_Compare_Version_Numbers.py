class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split('.'), version2.split('.')

        for i in range(max(len(v1), len(v2))):
            try:
                r1 = int(v1[i])
            except IndexError:
                r1 = 0

            try:
                r2 = int(v2[i])
            except IndexError:
                r2 = 0

            if r1 < r2:
                return -1
            elif r1 > r2:
                return 1

        return 0