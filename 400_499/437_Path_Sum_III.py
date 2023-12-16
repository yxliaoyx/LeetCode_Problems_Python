# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, prefix_sum, sum_dict):
            if not node:
                return 0

            prefix_sum += node.val

            count = sum_dict[prefix_sum - targetSum]

            sum_dict[prefix_sum] += 1
            count += dfs(node.left, prefix_sum, sum_dict) + dfs(node.right, prefix_sum, sum_dict)
            sum_dict[prefix_sum] -= 1

            return count

        return dfs(root, 0, defaultdict(int, {0: 1}))
