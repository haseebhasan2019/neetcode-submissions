class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Each nodes parent is itself
        parent = [i for i in range(n)]
        components = n

        # finds the parent of a node
        def find(node):
            new_node = node
            while new_node != parent[new_node]:
                new_node = parent[new_node]
            return new_node

        # combines connected components
        def union(u, v):
            u_parent = find(u)
            v_parent = find(v)

            if u_parent != v_parent:
                parent[u_parent] = v_parent
                return True
            else:
                return False

        for u, v in edges:
            if union(u, v):
                components -=1
        return components

