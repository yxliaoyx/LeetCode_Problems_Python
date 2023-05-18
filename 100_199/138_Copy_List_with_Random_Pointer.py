"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = {}
        node = head

        while node:
            mapping[node] = Node(node.val)
            node = node.next

        for key, val in mapping.items():
            val.next = mapping.get(key.next)
            val.random = mapping.get(key.random)

        return mapping.get(head)
