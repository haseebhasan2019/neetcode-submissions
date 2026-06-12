# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s = f = head
        for i in range(n):
            f = f.next
        if f == None:
            head = head.next
            return head
        while f:
            print(s.val, f.val)
            if f.next == None:
                s.next = s.next.next
                return head
            s = s.next
            f = f.next


# 1 2 3 4, n = 3
# if f = null
#     head = head.next
#     return

# something about using n as the hop size

# s and f pointers separated by a gap of n
# while f
# if f.next = null
#     s .next = s.next.next
#     return