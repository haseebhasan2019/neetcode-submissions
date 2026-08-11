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

        while l1_rev and l2_rev:
            val = l1_rev.val + l2_rev.val + carry
            if val > 9:
                node = ListNode(val - 10)
                carry = 1
            else:
                node = ListNode(val)
                carry = 0
            l1_rev = l1_rev.next
            l2_rev = l2_rev.next
            ptr.next = node
            ptr = ptr.next
        l1_rev = l2_rev if l2_rev else l1_rev
        while l1_rev:
            val = l1_rev.val + carry
            if val > 9:
                node = ListNode(val - 10)
                carry = 1
            else:
                node = ListNode(val)
                carry = 0
            l1_rev = l1_rev.next
            ptr.next = node
            ptr = ptr.next
        if carry:
            ptr.next = ListNode(1)
            ptr = ptr.next

        return reverse_ll(res.next)



        # 1 -> 2 -> 3
        # dummy -> 1

        # 2 -> 3
        # dummy -> 2 -> 1

# reverse l1 and l2, add them into one of the lists
# O(n+m) time, O(1) space
    
# iterate through l1 and l2, get the numbers as ints, add them, create LL
# O(n+m) time O(max(n, m)) space, O(1) auxillary space
