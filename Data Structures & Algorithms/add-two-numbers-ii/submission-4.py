# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_ll(head):
            rev = None
            while head:
                node = head
                head = head.next
                node.next = rev
                rev = node
            return rev

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
        res = ptr = ListNode()
        carry = 0

        while stk1 or stk2 or carry:
            val = carry
            if stk1:
                val += stk1.pop()
            if stk2:
                val += stk2.pop()
            carry, digit = divmod(val, 10)
            ptr.next = ListNode(digit)
            ptr = ptr.next

        return reverse_ll(res.next)