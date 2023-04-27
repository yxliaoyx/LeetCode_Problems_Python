"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root

        while node:
            kid = temp = Node()

            while node:
                if node.left:
                    kid.next = node.left
                    kid = kid.next
                if node.right:
                    kid.next = node.right
                    kid = kid.next
                node = node.next

            node = temp.next

        return root
