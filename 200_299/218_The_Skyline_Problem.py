class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        h = []
        skyline = []
        stack = [0]

        for left, right, height in buildings:
            h.append([left, -height])
            h.append([right, height])

        for x, y in sorted(h):
            current_height = max(stack)

            if y < 0:
                stack.append(-y)
                if abs(y) > current_height:
                    skyline.append([x, max(stack)])
            else:
                stack.remove(y)
                if current_height != max(stack):
                    skyline.append([x, max(stack)])

        return skyline
