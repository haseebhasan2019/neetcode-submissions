# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = None
        while head != None:
            temp = head
            head = head.next
            temp.next = ptr
            ptr = temp
        return ptr

#  0 -> 1 -> 2 -> 3
#  0  1 -> 2 -> 3
#  ptr = 0

#  0 <- 1  2 -> 3
#     ptr  head
#  ptr = 1

#  0 <- 1 <- 2  3

#  ptr = 2
#   0 <- 1 <- 2 <- 3

# return head (3)