class TreeNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}

class PrefixTree:
    
    head = None
    
    def __init__(self):
        self.head = TreeNode()

    def insert(self, word: str) -> None:
        ptr = self.head
        for letter in word:
            if letter not in ptr.children:
                ptr.children[letter] = TreeNode()
            ptr = ptr.children[letter]
        ptr.isEnd = True

    def search(self, word: str) -> bool:
        ptr = self.head
        for letter in word:
            if letter not in ptr.children:
                return False
            ptr = ptr.children[letter]
        return ptr.isEnd

    def startsWith(self, prefix: str) -> bool:
        ptr = self.head
        for letter in prefix:
            if letter not in ptr.children:
                return False
            ptr = ptr.children[letter]
        return True
        
        