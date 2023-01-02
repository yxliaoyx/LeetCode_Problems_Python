# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def toString(list_node):
            try:
                return toString(list_node.next) + str(list_node.val)
            except:
                return ''

        def toListNode(val):
            try:
                return ListNode(val=int(val[-1:]), next=toListNode(val[:-1]))
            except:
                return None

        return toListNode(str(int(toString(l1)) + int(toString(l2))))
