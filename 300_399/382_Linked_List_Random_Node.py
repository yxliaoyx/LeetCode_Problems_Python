from random import random


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        i = 1
        node = self.head
        result = 0

        while node:
            if random() < 1 / i:  # capacity of the reservoir is 1, because we just need to return a single num
                result = node.val  # replace result with i-th node.val with probability 1/i

            i += 1
            node = node.next

        return result

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
