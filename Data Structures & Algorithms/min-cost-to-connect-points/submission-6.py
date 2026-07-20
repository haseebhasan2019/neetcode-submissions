class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # PRIM'S O(n^2)
        # points are nodes from 0... len(points)-1
        n = len(points)
        costs = [float("inf")] * n
        visited = [False] * n
        total = 0

        def distance(i, j):
            return abs(i[0]-j[0]) + abs(i[1]-j[1])

        current = 0
        for _ in range(n-1):
            visited[current] = True
            closest = -1
            for i in range(n):
                if visited[i]:
                    continue
                w = distance(points[current], points[i])
                costs[i] = min(costs[i], w)
                # update closest if i's cost is less than the current closest
                if closest == -1 or costs[i] < costs[closest]:
                    closest = i
            total += costs[closest]
            current = closest

        return total

# iterate until edges == n-1
# add current node to tree
# find the closest node not currently in the tree
#    update the cheapest edges to their possible new mins
#    update closest node
# update total cost with cost of closest
# move to closest node