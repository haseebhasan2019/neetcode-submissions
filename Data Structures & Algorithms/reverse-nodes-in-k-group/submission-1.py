# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_group(head):
            ptr = None
            for i in range(k): # while head
                temp = head
                head = head.next
                temp.next = ptr
                ptr = temp
            # print(ptr.val)
            return (ptr, head)

        ptr = dummy_head = ListNode()
        ptr.next = head
        group_size = 0

        while head:
            group_ptr = head
            while group_ptr and group_size < k:
                group_ptr = group_ptr.next
                group_size+=1
            group_ptr = head
            # print(group_size)
            if group_size != k:
                ptr.next = head
                break
            group_size = 0
            ptr.next, head = reverse_group(head)
            for i in range(k):
                ptr = ptr.next
        return dummy_head.next


# 1 2 3 4 5 6 7 8 k =5
# 5 4 3 2 1 6 7 8

# Iterate k steps
# If it makes it all the way through - reverse the linkedlist
        # Move group ptr until group_size is k
        # if ptr becomes null, return head
        # else, reverse the group

