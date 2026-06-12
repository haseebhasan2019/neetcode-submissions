class TrieNode:
    def __init__(self):
        self.word = ""
        self.children = {} # letter -> TrieNode

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        DIRECTIONS = ((0,1),(0,-1),(1,0),(-1,0))
        
        def createTrie():
            head = TrieNode()
            for word in words:
                ptr = head
                for c in word:
                    if c not in ptr.children:
                        ptr.children[c] = TrieNode()
                    ptr = ptr.children[c]
                ptr.word = word
            return head

        def wordSearch(row, col, node):
            if (0 <= row < len(board) and 
                0 <= col < len(board[0]) and
                board[row][col] in node.children):
                c = board[row][col]
                next_node = node.children[c]
                if next_node.word:
                    res.append(next_node.word)
                    next_node.word = ""
                board[row][col] = ""
                for dr, dc in DIRECTIONS:
                    wordSearch(row+dr, col+dc, next_node)
                board[row][col] = c

        head = createTrie()
        for row in range(len(board)):
            for col in range(len(board[0])):
                wordSearch(row, col, head)
        return res