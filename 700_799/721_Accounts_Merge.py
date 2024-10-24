from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        parent = {}
        email_owner = {}

        for name, *emails in accounts:
            for email in emails:
                email_owner[email] = name
                if email not in parent:
                    parent[email] = email

            for email in emails[1:]:
                union(emails[0], email)

        merged = defaultdict(list)

        for email in parent:
            merged[find(email)].append(email)

        return [[email_owner[emails[0]]] + sorted(emails) for emails in merged.values()]
