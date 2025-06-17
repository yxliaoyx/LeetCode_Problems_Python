class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            name, domain = s.lower().split("@")
            return f"{name[0]}*****{name[-1]}@{domain}"

        digits = "".join(c for c in s if c.isdigit())

        if len(digits) == 10:
            return f"***-***-{digits[-4:]}"

        return f"+{'*' * (len(digits) - 10)}-***-***-{digits[-4:]}"
