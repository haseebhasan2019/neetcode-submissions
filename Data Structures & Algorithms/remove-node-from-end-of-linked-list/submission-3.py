# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        back = front = head
        for i in range(n):
            front = front.next
        if not front:
            return back.next
        while front.next:
            front = front.next
            back = back.next
        back.next = back.next.next
        return head

# 1 2 3 4 5 (2)
# len = 5
# index before removal: len-n-1


# 1 2 3 4 5 (2)
# b.  f
#   b.  f 
#     b.  f
#     if front.next == None:
#         detach nth last node