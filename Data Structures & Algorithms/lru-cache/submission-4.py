class Node:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key -> Node

        # back <=> front
        self.front = Node(None, None)
        self.back = Node(None, None)
        self.front.prev = self.back
        self.back.next = self.front
    
    def addToFront(self, node):
        prev = self.front.prev
        prev.next = node
        node.prev = prev
        node.next = self.front
        self.front.prev = node

    def moveToFront(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.addToFront(node)

    def removeFromBack(self):
        target = self.back.next
        self.back.next = target.next
        target.next.prev = self.back
        return target.key

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.moveToFront(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.moveToFront(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.addToFront(node)
            if len(self.cache) > self.cap:
                k = self.removeFromBack()
                del self.cache[k]
        
# get 
#     input - key
#     output - value or -1 if not in cache
#     req - need to mark that key as most recently used and move it to the front of the cache

# put
#     input - key, value
#     output - none
#     reqs
#         - update value if key exists - make MRU
#         - otherwise add to the cache - make MRU
#         - if adding, makes cache larger than capacity, remove LRU

# O(1) insertion and deletion = doubly LL of Node objects
# cache = key -> [Node]
# Node = val

