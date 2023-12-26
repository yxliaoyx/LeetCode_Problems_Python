# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        # record of preorder traversal path
        result = []

        def dfs(node):
            if node:
                result.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else:
                result.append("N")

        dfs(root)

        return ",".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        val_list = data.split(",")

        def dfs(i):
            if val_list[i] == "N":
                return None, i + 1

            node = TreeNode(int(val_list[i]))
            node.left, i = dfs(i + 1)
            node.right, i = dfs(i)

            return node, i

        return dfs(0)[0]

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
