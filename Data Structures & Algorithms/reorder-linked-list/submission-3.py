# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Use slow ptr fast ptr to split the list
        s = head
        f = head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        list2 = s.next
        prev = s.next = None
        
        # reverse the 2nd half
        while list2:
            temp = list2.next
            list2.next = prev
            prev = list2
            list2 = temp
        list2 = prev
        
        # interlace the two halves until the end
        ptr = head
        while ptr and list2:
            temp = ptr.next 
            ptr.next = list2 
            temp2 = list2.next 
            list2.next = temp
            list2 = temp2
            ptr = ptr.next.next 
    
# 1 2 3 4 5
# 1 2 3   4 5
# 1 2 3   5 4
# 1 5 2 4 3