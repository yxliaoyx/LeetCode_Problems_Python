# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head

        # find mid
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        prev, node = None, slow

        while node:
            node.next, prev, node = prev, node, node.next

        # merge in-place
        first, second = head, prev

        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
