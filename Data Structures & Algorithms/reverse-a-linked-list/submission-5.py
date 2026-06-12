# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse_head = None
        while head:
            ptr = head
            head = head.next
            ptr.next = reverse_head
            reverse_head = ptr
        return reverse_head