class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim’s Algorithm: Start with the minimum edge in the graph, greedily choose the next smallest edge connected to the result tree
        # O (n^2)
        vertices = len(points)
        dists = [float('inf')] * vertices
        visited = [False] * vertices
        # dists[0] = 0 # REV?
        curr = 0
        total = 0

        def distance(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        # Start at first point
        # Iterate through all other points and update distances
        # Keep track of min dist point if it is unvisited (-1)
        # Next explore that point
        # Keep going until all points are connected (edges = vertices-1)
        for _ in range(vertices-1):
            visited[curr] = True
            next_ = -1
            for i in range(vertices):
                if visited[i]:
                    continue
                curr_dist = distance(curr, i)
                dists[i] = min(dists[i], curr_dist)
                if next_ == -1 or dists[i] < dists[next_]:
                    next_ = i
            total += dists[next_]
            curr = next_
        
        return total