class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        head = TrieNode()
        for word in words:
            ptr = head
            for c in word:
                if c not in ptr.children:
                    ptr.children[c] = TrieNode()
                ptr = ptr.children[c]
            ptr.word = word
        
        def search(row, col, node):
            if (row < 0 or row >= len(board) or 
                col < 0 or col >= len(board[0])):
                return
            c = board[row][col]
            if c not in node.children:
                return
            next_node = node.children[c]
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None
            board[row][col] = ""
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                search(row+dr, col+dc, next_node)
            board[row][col] = c

        res = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                search(row, col, head)
        return res


