# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        stack = [root]

        while stack:
            node = stack.pop()

            if node:
                stack.append(node.right)
                stack.append(node.left)

                results.append(node.val)

        return results
