class Solution:
    def works(self, s):
        return s == str(int(s)) and int(s) <= 255

    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        addresses = []

        for i in range(1, n):
            if not self.works(s[:i]):
                continue
            for j in range(i + 1, n):
                if not self.works(s[i:j]):
                    continue
                for k in range(j + 1, n):
                    if self.works(s[j:k]) and self.works(s[k:]):
                        addresses.append(f'{s[:i]}.{s[i:j]}.{s[j:k]}.{s[k:]}')

        return addresses
