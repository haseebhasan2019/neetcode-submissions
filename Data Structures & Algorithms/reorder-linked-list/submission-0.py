# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ptr = head
        length = 0

        while ptr:
            length+=1
            ptr = ptr.next
        length = length // 2
        ptr = head
        for i in range(length):
            ptr = ptr.next
        list2 = ptr.next
        ptr.next = None
                
        # print result
        print("head:")
        point = head
        while point:
            print(str(point.val))
            point = point.next
        print("list2:")
        point = list2
        while point:
            print(str(point.val))
            point = point.next

        # 1 2 3   4 5
        list2 = self.reverse(list2)
        print("list2:")
        point = list2
        while point:
            print(str(point.val))
            point = point.next
            
        # 2 -> 4   8 -> 6
        # 2 -> 8 -> 4   6
        ptr = head
        while ptr and list2:
            temp = ptr.next # 4
            ptr.next = list2 # 2 -> 8
            temp2 = list2.next # 6
            list2.next = temp # 8 -> 4
            list2 = temp2 # 6
            ptr = ptr.next.next 
        print (head)
        # ptr.next = ptr or list2

        # return head
    
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = None
        while head != None:
            temp = head
            head = head.next
            temp.next = ptr
            ptr = temp
        return ptr

# Get the length of the list
# split the list at its midpoint
# reverse the 2nd half
# interlace the two halves until the end

# 1 2 3 4 5
# 1 2 3   4 5
# 1 2 3   5 4
# 1 5 2 4 3