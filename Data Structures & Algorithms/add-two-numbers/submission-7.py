# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ptr = ListNode()
        rem = 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            total = l1_val + l2_val + rem
            rem = 0
            if total > 9:
                rem = total // 10
                total = total % 10
            node = ListNode(total)
            ptr.next = node
            ptr = ptr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if rem:
            ptr.next = ListNode(rem)

        return res.next