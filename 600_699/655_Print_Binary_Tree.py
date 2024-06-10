# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def update(node, row, left, right):
            if node:
                mid = (left + right) // 2
                result[row][mid] = str(node.val)
                update(node.left, row + 1, left, mid - 1)
                update(node.right, row + 1, mid + 1, right)

        h = self.getHeight(root)
        w = 2**h - 1
        result = [[""] * w for _ in range(h)]
        update(root, 0, 0, w - 1)

        return result

    def getHeight(self, node):
        return 1 + max(self.getHeight(node.left), self.getHeight(node.right)) if node else 0
