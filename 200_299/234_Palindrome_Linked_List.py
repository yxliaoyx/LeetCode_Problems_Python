# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        reverse = None

        while fast and fast.next:
            slow, fast, reverse, reverse.next = slow.next, fast.next.next, slow, reverse

        if fast:
            slow = slow.next

        while reverse and reverse.val == slow.val:
            reverse, slow = reverse.next, slow.next

        return not reverse
