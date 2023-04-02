# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        current = head
        previous = dummy

        for _ in range(left - 1):
            current = current.next
            previous = previous.next

        for _ in range(right - left):
            temp = current.next
            current.next = temp.next
            temp.next = previous.next
            previous.next = temp

        return dummy.next
