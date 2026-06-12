# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast pointer reaches null -> no cycle
        # fast ptr reaches slow ptr -> cycle
        slow = fast = head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                break
            slow = slow.next
            if fast == slow:
                return True
        return False