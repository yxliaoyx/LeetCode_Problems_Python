# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sum_map = defaultdict(int)

        def find(node):
            if not node:
                return 0

            tree_sum = node.val + find(node.left) + find(node.right)
            sum_map[tree_sum] += 1

            return tree_sum

        find(root)
        frequent = max(sum_map.values())

        return [k for k, v in sum_map.items() if v == frequent]
