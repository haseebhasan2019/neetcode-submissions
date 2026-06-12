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

# (1) -> 2 -> 3
# 1 <- 2 <- (3)

# 3 -> 2 -> 1 issue: O(n) extra space

# 1. ptr will point to the node
# 2. head will be moved fwd
# 3. set ptr.next to reverseHead (start as null)
# 4. set reverseHead to ptr

# 1 -> None