# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode()

        while head:
            if head.val < prev.val:
                prev = dummy

            while prev.next and head.val > prev.next.val:
                prev = prev.next

            prev.next, head.next, head = head, prev.next, head.next

        return dummy.next
