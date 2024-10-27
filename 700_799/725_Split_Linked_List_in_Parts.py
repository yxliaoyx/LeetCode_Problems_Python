# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, node = 0, head

        while node:
            length += 1
            node = node.next

        part_length, longer_parts = divmod(length, k)
        parts = []
        node = head

        for i in range(k):
            part_head = node

            for _ in range(part_length + (i < longer_parts) - 1):
                if node:
                    node = node.next

            if node:
                node.next, node = None, node.next

            parts.append(part_head)

        return parts
