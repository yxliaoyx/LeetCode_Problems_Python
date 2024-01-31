class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s[::-1].replace("-", "").upper()

        return "-".join(s[i : i + k] for i in range(0, len(s), k))[::-1]
