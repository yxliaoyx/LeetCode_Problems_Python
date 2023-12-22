# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        total_sum = 0
        result = ListNode()
        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        while stack1 or stack2:
            if stack1:
                total_sum += stack1.pop()
            if stack2:
                total_sum += stack2.pop()

            carry, result.val = divmod(total_sum, 10)
            result = ListNode(carry, next=result)
            total_sum = carry

        return result.next if carry == 0 else result
