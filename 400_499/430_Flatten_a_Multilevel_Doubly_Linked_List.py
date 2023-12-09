"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        prev_node = None
        stack = [head]

        while stack:
            node = stack.pop()

            if prev_node:
                prev_node.next, node.prev = node, prev_node

            prev_node = node

            if node.next:
                stack.append(node.next)

            if node.child:
                stack.append(node.child)
                node.child = None

        return head
