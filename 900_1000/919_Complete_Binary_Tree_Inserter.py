# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:
    def __init__(self, root: Optional[TreeNode]):
        self.tree = [root] if root else []
        for node in self.tree:
            if node.left:
                self.tree.append(node.left)
            if node.right:
                self.tree.append(node.right)

    def insert(self, val: int) -> int:
        node = TreeNode(val)
        parent = self.tree[(len(self.tree) - 1) // 2]

        if len(self.tree) % 2:
            parent.left = node
        else:
            parent.right = node

        self.tree.append(node)
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.tree[0] if self.tree else None


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
