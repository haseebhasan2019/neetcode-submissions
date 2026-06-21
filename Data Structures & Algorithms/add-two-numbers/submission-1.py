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
            new_node = ListNode()
            value = rem + l1.val + l2.val
            rem = value // 10
            new_node.val = value % 10
            ptr.next = new_node
            ptr = ptr.next
            l1 = l1.next
            l2 = l2.next
        l = l1 or l2
        while l:
            new_node = ListNode()
            value = rem + l.val
            if value >= 10:
                rem = value // 10
            else:
                rem = 0
            new_node.val = value % 10
            ptr.next = new_node
            ptr = ptr.next
            l = l.next
        if rem:
            ptr.next = ListNode(rem)
            ptr = ptr.next
        return res.next

#  9
# +9
# 18

# 19
# +9
# 28

#  999
#  + 9
# 1008