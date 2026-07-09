class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # each node starts off as its own parent
        parent = [i for i in range(n)]

        def find(node):
            cur = node
            while cur != parent[cur]:
                cur = parent[cur]
            return cur
        
        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)

            if parent1 == parent2:
                return 0
            else:
                parent[parent1] = parent2
                return 1
        
        components = n
        for u, v in edges:
            components -= union(u, v)
        return components



# [0 1 2 3 4]
# [0 0 2 3 4]
# [0 0 0 3 4]
# [0 0 0 3 3]
#  0 1 2 3 4

# n = 5, edges = [[0,1],[1,2],[3,4]]


# [0 1 2 3 4]
# [0 0 0 0 0]

#  0 1 2 3 4

# [[0,1],[0,2],[1,2],[2,3],[2,4]]