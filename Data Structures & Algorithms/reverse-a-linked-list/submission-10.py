# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        while head:
            temp = dummy.next
            dummy.next = head
            nxt = head.next
            head.next = temp
            head = nxt

        return dummy.next


# 1 2 3

# head = 1
# dummy = 0
# 0 -> 1
# head = 2


