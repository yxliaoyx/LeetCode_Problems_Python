# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        level = [root]
        traversal = []

        while level:
            traversal.append([node.val for node in level])
            level = [kid for n in level for kid in (n.left, n.right) if kid]

        return traversal
