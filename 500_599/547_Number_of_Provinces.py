class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            for neighbor, is_connected in enumerate(isConnected[city]):
                if is_connected and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        if not isConnected:
            return 0

        count = 0
        visited = [False] * len(isConnected)

        for i in range(len(isConnected)):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                count += 1

        return count
