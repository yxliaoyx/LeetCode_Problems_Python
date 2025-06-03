# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        num_set = set(nums)
        count = 0

        while head:
            if head.val in num_set and (not head.next or head.next.val not in num_set):
                count += 1
            head = head.next

        return count
