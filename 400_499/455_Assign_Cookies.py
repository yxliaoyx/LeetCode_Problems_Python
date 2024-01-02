class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        content_children = 0

        for cookie_size in s:
            if content_children >= len(g):
                return content_children

            if cookie_size >= g[content_children]:
                content_children += 1

        return content_children
