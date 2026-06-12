"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {}
        def dfs(node):
            copy = Node(node.val)
            visited[copy.val] = copy
            for neighbor in node.neighbors:
                if neighbor.val in visited:
                    copy.neighbors.append(visited[neighbor.val])
                else:
                    copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)

# 1: 2
# 2: 1,3
# 3: 2

# visited: 
# 1: (node1)