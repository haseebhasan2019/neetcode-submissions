# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ptr = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next
            ptr = ptr.next
        ptr.next = list1 if list1 else list2
        return res.next

# list1 = [1,2,4], list2 = [1,3,5]
# ptr = res = 1
# list1 = [1,2,4], list2 = [3,5]
# ptr = 1, res = 1
# list1 = [2,4], list2 = [3,5]
# ptr = 2
# list1 = [4], list2 = [3,5]
# ptr = 3
# list1 = [4], list2 = [5]
# ptr = 4
# list1 = [], list2 = [5]
# ptr = 4 -> 5
