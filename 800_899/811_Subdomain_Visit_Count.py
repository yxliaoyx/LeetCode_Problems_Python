from collections import Counter


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = Counter()

        for entry in cpdomains:
            count, domain = entry.split()
            count = int(count)
            parts = domain.split(".")

            for i in range(len(parts)):
                counts[".".join(parts[i:])] += count

        return [f"{count} {domain}" for domain, count in counts.items()]
