# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])

        if len(preorder) == 1:
            return root

        i = postorder.index(preorder[1]) + 1

        root.left = self.constructFromPrePost(preorder[1 : i + 1], postorder[:i])
        root.right = self.constructFromPrePost(preorder[i + 1 :], postorder[i:-1])

        return root
