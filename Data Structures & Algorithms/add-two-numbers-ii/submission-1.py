# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def get_int(head):
            res = []
            while head:
                res.append(str(head.val))
                head = head.next
            return int("".join(res))


        l1_sum = get_int(l1)
        l2_sum = get_int(l2)
        total = str(l1_sum + l2_sum)

        res = ptr = ListNode()
        for digit in total:
            node = ListNode(int(digit))
            ptr.next = node
            ptr = ptr.next
        return res.next

        # 1 -> 2 -> 3
        # dummy -> 1

        # 2 -> 3
        # dummy -> 2 -> 1

# reverse l1 and l2, add them into one of the lists
# O(n+m) time, O(1) space
    
# iterate through l1 and l2, get the numbers as ints, add them, create LL
# O(n+m) time O(max(n, m)) space, O(1) auxillary space
