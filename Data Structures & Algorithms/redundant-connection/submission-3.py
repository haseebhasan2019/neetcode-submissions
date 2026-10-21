class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges)+1))

        def find(node):
            # keep traversing up parent until node is its own parent
            rank = 1
            while node != parent[node]:
                node = parent[node]
                rank+=1
            return (node, rank)

        # return true if unconnected, false if already connected
        def union(u, v):
            u_par, u_rank = find(u)
            v_par, v_rank = find(v)

            if u_par == v_par:
                return False
            else:
                # parent of lower rank should become higher rank
                if u_rank < v_rank:
                    parent[u_par] = v_par
                else:
                    parent[v_par] = u_par
                return True

        for u, v in edges:
            if not union(u,v):
                return [u,v]

        return []

        
'''
each node originally starts as unconnected
iterate through edges
    check if the two nodes share the same parent, 
        if not, connect 2 nodes within the graph
    if those two nodes were already connected we have a redundant cnxn

===EXAMPLE 1===
1 2 3 4
[1,2]
1 1 3 4
[1,3]
1 1 1 4 or 3 1 3 4
[3,4]
1 1 1 1 or 3 1 4 4
[2,4]
parents already match

===EXAMPLE 2===
1 2 3 4 5
[1,2]
1 1 3 4 5
[1,3]
1 1 1 4 5
[1,4]
1 1 1 1 5
[3,4]
1 1 1 1 5 - already connected, safe to assume we can early exit?
[4,5]
'''