class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        ptr = self.head
        for c in word:
            if c not in ptr.children:
                ptr.children[c] = TrieNode()
            ptr = ptr.children[c]
        ptr.end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.end
            c = word[i]
            if c == '.':
                for child in node.children.values():
                    if dfs(child, i+1):
                        return True
                return False
            else: # 'm'
                if c not in node.children:
                    return False
                return dfs(node.children[c], i+1)
        return dfs(self.head, 0)
