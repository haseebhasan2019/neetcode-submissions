class Node:
    def __init__(self, key, val):
        self.prev = self.next = None
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

    def remove_node(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def add_to_back(self, node):
        prevBack = self.back.prev
        prevBack.next = node
        node.prev = prevBack
        node.next = self.back
        self.back.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove_node(node)
        self.add_to_back(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove_node(node)
            self.add_to_back(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.add_to_back(node)
            if len(self.cache) > self.capacity:
                lru = self.front.next
                del self.cache[lru.key]
                self.remove_node(lru)

        
# front  back
# LRU    MRU
# <-------->

# doubly linked list with front and back pointers
# put - move key to the back of the list and optionally update value
# get - move key to the back of the list