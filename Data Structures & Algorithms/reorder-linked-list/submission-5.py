# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = f = fwd = head
        while f and f.next:
            f = f.next.next
            s = s.next
        half = s.next
        s.next = None
        # reverse list
        rev = None
        while half:
            node = half
            half = half.next
            node.next = rev
            rev = node
        res = ListNode()
        ptr = res
        while fwd and rev:
            ptr.next = fwd
            fwd = fwd.next
            ptr = ptr.next
            ptr.next = rev
            rev = rev.next
            ptr = ptr.next
        ptr.next = fwd or rev
        head = res.next