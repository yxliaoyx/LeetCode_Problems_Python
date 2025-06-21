from collections import defaultdict


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = defaultdict(list)
        answer = [0] * n
        count = [1] * n

        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        def post(node, parent):
            for child in tree[node]:
                if child != parent:
                    post(child, node)
                    count[node] += count[child]
                    answer[node] += answer[child] + count[child]

        def pre(node, parent):
            for child in tree[node]:
                if child != parent:
                    answer[child] = answer[node] - count[child] + (n - count[child])
                    pre(child, node)

        post(0, -1)
        pre(0, -1)
        return answer
