class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Kruskal’s Algorithms: Select the minimum cost edge globally unless it forms a cycle. Using a minheap, will run in n logn time
        # O (n^2 log n^2)
        heap = []
        total = 0
        edges = 0
        vertices = len(points)
        parent = [i for i in range(vertices)]

        def distance(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        for i in range(vertices):
            for j in range(i+1, vertices):
                dist = distance(i, j)
                heapq.heappush(heap, (dist, i, j))

        def find(node):
            cur = node
            while cur != parent[cur]:
                cur = parent[cur]
            return cur

        def union(u, w):
            u_parent = find(u)
            v_parent = find(w)

            if u_parent == v_parent:
                return False
            else:
                parent[u_parent] = v_parent
                return True

        while heap and edges < vertices - 1:
            dist, i, j = heapq.heappop(heap)
            if union(i, j):
                total += dist
                edges += 1

        return total

