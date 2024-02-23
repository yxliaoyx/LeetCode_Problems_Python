# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_streak = 0
        self.streak = 0
        self.prev_val = 0
        self.result = []

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return

            dfs(node.left)

            if node.val == self.prev_val:
                self.streak += 1
            else:
                self.streak = 1
                self.prev_val = node.val

            if self.streak > self.max_streak:
                self.result = []
                self.max_streak = self.streak

            if self.streak == self.max_streak:
                self.result.append(node.val)

            dfs(node.right)

        dfs(root)

        return self.result
