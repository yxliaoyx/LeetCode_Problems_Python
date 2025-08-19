# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent=None):
            if node:
                parent_map[node] = parent
                dfs(node.left, node)
                dfs(node.right, node)

        def find_nodes(node, distance):
            if not node or node in visited:
                return

            visited.add(node)

            if distance == 0:
                result.append(node.val)
                return

            find_nodes(node.left, distance - 1)
            find_nodes(node.right, distance - 1)
            find_nodes(parent_map.get(node), distance - 1)

        parent_map = {}
        result = []
        visited = set()

        dfs(root)
        find_nodes(target, k)

        return result
