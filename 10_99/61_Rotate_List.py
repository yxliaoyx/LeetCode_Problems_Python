# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        length = 1
        pointer = head

        while pointer.next:
            pointer = pointer.next
            length += 1

        pointer.next = head
        rotate = length - (k % length)

        while rotate > 0:
            pointer = pointer.next
            rotate -= 1

        new_head = pointer.next
        pointer.next = None

        return new_head
