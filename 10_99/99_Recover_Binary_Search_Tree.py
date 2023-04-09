# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        current = root
        previous = None

        mistake1 = None
        mistake2 = None

        while current:
            if not current.left:
                if previous and current.val < previous.val:
                    mistake2 = current
                    if not mistake1:
                        mistake1 = previous

                previous, current = current, current.right
            else:
                p = current.left
                while p.right and p.right != current:
                    p = p.right

                if not p.right:
                    p.right = current
                    current = current.left
                else:
                    p.right = None
                    if previous and current.val < previous.val:
                        mistake2 = current
                        if not mistake1:
                            mistake1 = previous

                    previous, current = current, current.right

        mistake1.val, mistake2.val = mistake2.val, mistake1.val
