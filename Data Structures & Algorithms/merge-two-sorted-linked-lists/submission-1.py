# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ptr = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next
            ptr.next.next = None
            ptr = ptr.next
        ptr.next = list1 or list2
        return res.next

# 1 -> 2 -> 4
# 1 -> 3 -> 5

# compare list1 and list2
# res.next