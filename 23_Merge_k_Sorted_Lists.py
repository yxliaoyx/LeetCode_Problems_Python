# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap_nodes = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(heap_nodes)
        head = prev = None

        while heap_nodes:
            val, i, node = heap_nodes[0]

            try:
                heapq.heapreplace(heap_nodes, (node.next.val, i, node.next))
            except AttributeError:
                heapq.heappop(heap_nodes)

            try:
                prev.next = node
            except AttributeError:
                head = node

            prev = node

        if prev:
            prev.next = None

        return head
