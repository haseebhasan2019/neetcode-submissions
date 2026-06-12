# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # n * logk where k is number of lists and n is the longest list
        heap = [(node.val, i, node) for i, node in enumerate(lists)]
        heapq.heapify(heap)
        res = ListNode()
        ptr = res

        while heap:
            val, i, min_node = heapq.heappop(heap)
            ptr.next = min_node
            ptr = ptr.next
            if min_node.next:
                heapq.heappush(heap, (min_node.next.val, i, min_node.next))
        return res.next