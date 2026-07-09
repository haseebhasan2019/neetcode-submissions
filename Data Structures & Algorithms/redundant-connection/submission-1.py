class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]

        def find(node):
            curr = node
            while curr != parent[curr]:
                curr = parent[curr]
            return curr
        
        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)

            if parent1 == parent2:
                return True
            else:
                parent[parent1] = parent2
                return False
        
        for a, b in edges:
            if union(a, b):
                return [a, b]
        return []
# [0 1 1 1 1 5]
#  0 1 2 3 4 5
#  when both edges have the same parent, that is the edge that needs to be removed