# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ptr = ListNode()
        rem = 0
        while l1 and l2:
            value = rem + l1.val + l2.val
            ptr.next = ListNode(value % 10)
            rem = value // 10
            ptr = ptr.next
            l1 = l1.next
            l2 = l2.next
        l = l1 or l2
        while l:
            value = rem + l.val
            ptr.next = ListNode(value % 10)
            rem = value // 10
            ptr = ptr.next
            l = l.next
        if rem:
            ptr.next = ListNode(rem)
        return res.next