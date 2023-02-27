# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current_node = head

        for _ in range(k):
            if not current_node:
                return head

            current_node = current_node.next

        previous_node = None
        current_node = head

        for i in range(k):
            previous_node, previous_node.next, current_node = (
                current_node,
                previous_node,
                current_node.next,
            )

        head.next = self.reverseKGroup(current_node, k)

        return previous_node
