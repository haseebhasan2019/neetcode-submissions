# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Get to second half
        s = head
        f = head
        while f and f.next:
            f = f.next.next
            s = s.next
        second = s.next
        s.next = None
        # reverse the second half of the LL
        rev = None
        while second:
            temp = second
            second = second.next
            temp.next = rev
            rev = temp
        # interweave the first and second halves
        fwd = head
        while rev:
            tmp1, tmp2 = fwd.next, rev.next
            fwd.next = rev
            rev.next = tmp1
            fwd, rev = tmp1, tmp2
# 1 2 3 4
# 8 7 6 5

# # Get to second half
# 1 2 3 4 5 6 7 8
#       s
#                 f
# # reverse the second half of the LL
# rev/second -> 5 6 7 8

# rev -> 5
# second -> 6 7 8

# 6 5
# 7 8

# 7 6 5
# 8
# # interweave the first and second halves