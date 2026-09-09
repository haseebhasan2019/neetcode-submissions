# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        def recurse(node):
            # If at the end of the list, return node itself
            if not node.next:
                return node
            # reverse everything after node - returns new head (original tail)
            new_head = recurse(node.next)
            # tail of reversed portion now points back at node
            node.next.next = node
            node.next = None
            # Return the last node in the chain
            return new_head
        
        return recurse(head)