class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # points are nodes from 0... len(points)-1
        num_points = len(points)
        parent = [i for i in range(num_points)]
        total = 0

        def distance(i, j):
            return abs(i[0]-j[0]) + abs(i[1]-j[1])

        edges = []
        for i in range(num_points):
            for j in range(i+1, num_points):
                if i != j:
                    w = distance(points[i], points[j])
                    heapq.heappush(edges, (w, i, j))
        
        def find(node):
            curr = node
            while curr != parent[curr]:
                curr = parent[curr]
            return curr

        def union(u, v):
            u_parent = find(u)
            v_parent = find(v)

            # If already connected, don't add this weight
            if u_parent == v_parent:
                return False
            # if not connected, connect those components
            else:
                parent[v_parent] = u_parent
                return True

        connected_points = 0
        while edges and connected_points < num_points-1:
            # pop smallest edge
            w, u, v = heapq.heappop(edges)
            if union(u, v):
                total += w
                connected_points += 1

        return total
            
# parent = 
#     [0,1,2,3,4]
#     [0,1,1,3,4]
#     [0,1,1,1,4]
#     [0,1,1,1,1]
#     [1,1,1,1,1]
# costs  = 
#     [0,0,0,0,0]
#     [0,0,2,0,0]
#     [0,0,2,2,0]
#     [0,0,2,2,2]
#     [4,0,2,2,2]
# updated_points = 0, 1, 2, 3, 4
# edges  = [
#     (2,1,2) x
#     (2,1,3) x
#     (2,1,4) x
#     (2,2,1) x same parent
#     (2,2,3) x same parent
#     (2,2,4) x same parent
#     (2,3,1) x same parent
#     (2,3,2) x same parent
#     (2,4,1) x same parent (ALL DUPLICATES)
#     (2,4,2) x same parent
#     (4,0,1) x 
#     (4,1,0)
#     (4,3,4)
#     (4,4,3)
#     (6,0,2)
#     (6,0,3)
#     (6,0,4)
#     (6,2,0)
#     (6,3,0)
#     (6,4,0)
# ]

#             0.    1.    2.    3.    4.  
# points = [[0,0],[2,2],[3,3],[2,4],[4,2]]



# # create edges: between all points (weight (dist), u, v)
# # append all edges to the heap
# # begin popping from the heap and connecting components


