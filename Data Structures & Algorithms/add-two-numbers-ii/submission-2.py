# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 999 + 11 = 1010
        # 123 + 456 = 579

        def reverse_ll(head):
            rev = None
            while head:
                node = head
                head = head.next
                node.next = rev
                rev = node
            return rev

        l1_rev = reverse_ll(l1)
        l2_rev = reverse_ll(l2)
        res = ptr = ListNode()
        carry = 0

        while l1_rev or l2_rev or carry:
            val = carry
            if l1_rev:
                val += l1_rev.val
                l1_rev = l1_rev.next
            if l2_rev:
                val += l2_rev.val
                l2_rev = l2_rev.next
            if val > 9:
                node = ListNode(val - 10)
                carry = 1
            else:
                node = ListNode(val)
                carry = 0
            ptr.next = node
            ptr = ptr.next

        return reverse_ll(res.next)