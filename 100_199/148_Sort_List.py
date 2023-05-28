# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []

        while head:
            nodes.append(head.val)
            head = head.next

        return ListNode(','.join(map(str, sorted(nodes))))
