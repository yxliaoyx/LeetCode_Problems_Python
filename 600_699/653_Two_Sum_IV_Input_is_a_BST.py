# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        q = deque([root])
        seen = set()

        while q:
            node = q.popleft()

            if node:
                if k - node.val in seen:
                    return True

                seen.add(node.val)
                q.extend([node.left, node.right])

        return False
