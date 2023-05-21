# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            try:
                slow = slow.next
                fast = fast.next.next
            except AttributeError:
                return False

        return True
