# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        traversal = []

        while queue:
            if len(traversal) % 2:
                traversal.append([kid.val for kid in queue][::-1])
            else:
                traversal.append([kid.val for kid in queue])

            queue = [kid for node in queue for kid in (node.left, node.right) if kid]

        return traversal
