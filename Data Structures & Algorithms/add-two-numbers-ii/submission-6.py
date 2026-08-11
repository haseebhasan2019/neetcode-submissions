# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create stacks of l1 and l2
        stk1 = []
        ptr = l1
        while ptr:
            stk1.append(ptr.val)
            ptr = ptr.next
        stk2 = []
        ptr = l2
        while ptr:
            stk2.append(ptr.val)
            ptr = ptr.next
        # Process stacks
        res = None
        carry = 0

        while stk1 or stk2 or carry:
            val = carry
            if stk1:
                val += stk1.pop()
            if stk2:
                val += stk2.pop()
            carry, digit = divmod(val, 10)
            node = ListNode(digit)
            node.next = res
            res = node

        return res