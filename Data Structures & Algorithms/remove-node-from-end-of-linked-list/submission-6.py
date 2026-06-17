# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s = f = head
        # move f n steps
        for i in range(n):
            f = f.next
        if not f:
            return s.next
        # keep iterating until f.next is none
        while f.next:
            s = s.next
            f = f.next
        s.next = s.next.next
        return head

# 1 2 3 4 5 n=2
# s
#     f
#   s
#       f
#     s
#         f
# when ahead node.next == null: remove s.next

# 5 n=1
# s
# f

# 1 2 n =2
# s
#   f
# in first iteration, when setting f to n steps, if f.next is None: return s.next

# 1 2 3 n = 2
