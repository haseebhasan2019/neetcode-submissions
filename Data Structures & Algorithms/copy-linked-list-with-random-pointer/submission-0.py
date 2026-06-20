"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        mp = {} # original node -> new node
        new_head = ptr = Node(head.val)
        mp[head] = new_head
        prev = head
        head = head.next
        while prev:
            # Check Next
            if head:
                if head in mp: # next node alr in map
                    node = mp[head]
                else: # create it
                    node = Node(head.val)
                    mp[head] = node # orig -> new
                ptr.next = node
                head = head.next
            # Check random
            if prev.random:
                if prev.random in mp:
                    rand = mp[prev.random] # get new node
                else:
                    rand = Node(prev.random.val)
                    mp[prev.random] = rand
                ptr.random = rand
            ptr = ptr.next
            prev = prev.next
        return new_head

# val-next-random

# 1-2-5 -> 2-3-4 -> 3-2-1 -> 4-5-3 -> 5-None-1

# 2 -> 4 -> 3 -> 1 <-> 5

# as we iterate through the list we just create the next nodes and 
#     store them in a map of original node -> new node
# Then iterate again and point the next node to the appropriate node

# Can we do this in a single pass?
# Create both the next node AND the random node and store them 
# issue is that node values are not guaranteed to be unique

# for each node:
#     create its copy

# HOW would you deep copy a normal linked list:

# 1 -> 4 -> 6 -> None
# for each node, you have to duplicate each node
# new list is always one node behind the original list
