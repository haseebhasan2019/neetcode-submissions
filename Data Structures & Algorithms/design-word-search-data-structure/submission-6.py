class TrieNode:
    def __init__(self):
        self.children = {} # character -> TrieNode
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True

    def search(self, word: str) -> bool:

        def rec_search(node, start):
            for i in range(start, len(word)):
                c = word[i]
                if c == '.':
                    for child in node.children.values():
                        if rec_search(child, i+1):
                            return True
                    return False
                elif c not in node.children:
                    return False
                node = node.children[c]
            return node.isEnd

        return rec_search(self.root, 0)
