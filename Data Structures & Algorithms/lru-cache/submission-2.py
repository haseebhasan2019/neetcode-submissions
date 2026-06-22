class Node:
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> Node()
        self.front = Node(0, 0)
        self.back = Node(0, 0)
        self.front.next = self.back
        self.back.prev = self.front

    def moveToBack(self, node):
        # Disconnect
        node.prev.next, node.next.prev = node.next, node.prev
        node.prev = node.next = None
        self.addToBack(node)

    def addToBack(self, node):
        prevBack = self.back.prev
        # prev
        prevBack.next = node
        node.prev = prevBack
        # next
        node.next = self.back
        self.back.prev = node

    def removeFront(self):
        prevFront = self.front.next
        del self.cache[prevFront.key]
        prevFront.next.prev = self.front
        self.front.next = prevFront.next

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.moveToBack(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.moveToBack(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.addToBack(node)
            if len(self.cache) > self.capacity:
                self.removeFront()        
        
# front  back
# LRU    MRU
# <-------->

# doubly linked list with front and back pointers
# put - move key to the back of the list and optionally update value
# get - move key to the back of the list