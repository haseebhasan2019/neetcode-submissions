# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ptr = head
        # length = 0

        # # Get the length of the list
        # while ptr:
        #     length+=1
        #     ptr = ptr.next
        
        # # split the list at its midpoint
        # length = length // 2
        # ptr = head
        # for i in range(length):
        #     ptr = ptr.next
        # list2 = ptr.next
        # ptr.next = None

        # Use slow ptr fast ptr to split the list
        s = head
        f = head.next
        while s and f and f.next:
            s = s.next
            f = f.next.next
        list2 = s.next
        s.next = None
        
        # reverse the 2nd half
        list2 = self.reverse(list2)
        
        # interlace the two halves until the end
        ptr = head
        while ptr and list2:
            temp = ptr.next 
            ptr.next = list2 
            temp2 = list2.next 
            list2.next = temp
            list2 = temp2
            ptr = ptr.next.next 
    
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = None
        while head != None:
            temp = head
            head = head.next
            temp.next = ptr
            ptr = temp
        return ptr


# 1 2 3 4 5
# 1 2 3   4 5
# 1 2 3   5 4
# 1 5 2 4 3