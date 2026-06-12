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

# (7) 8 9
# 7


# 0 1 2 3
# f.  f. f=none
# s s detach from s.next (2)

# 0 3 1 2

# 0 1 2 3 4
# f.  f   f= None
# s s s detach s.next (3)

# 0 4 1 3 2 

# 3 4

# 4 3 
# 0 1 2

# 0 4 1 3 2

# 1. get halfway through the list -> slow ptr + fast ptr
# 2. detach from n/2
# 3. reverse that list
# 4. weave reversed and forward lists