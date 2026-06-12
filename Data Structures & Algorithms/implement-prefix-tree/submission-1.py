class Node:
    def __init__(self):
        self.end = False
        self.children = {}
class PrefixTree:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        ptr = self.head
        for c in word:
            if c not in ptr.children:
                ptr.children[c] = Node()
            ptr = ptr.children[c]
        ptr.end = True

    def search(self, word: str) -> bool:
        ptr = self.head
        for c in word:
            if c not in ptr.children:
                return False
            ptr = ptr.children[c]
        return ptr.end

    def startsWith(self, prefix: str) -> bool:
        ptr = self.head
        for c in prefix:
            if c not in ptr.children:
                return False
            ptr = ptr.children[c]
        return True
        
        