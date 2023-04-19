# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        previous = node = mid = head

        while node and node.next:
            previous = mid
            mid = mid.next
            node = node.next.next

        previous.next = None
        return TreeNode(mid.val, self.sortedListToBST(head), self.sortedListToBST(mid.next))
