class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # backtrack and optimize for shortest path, then quit path when surpass k or greater than current cheapest price
        # O(n^(k+1)) Where n is the number of cities, m is the number of flights and k is the number of stops.
        cheapest_price = float('inf')
        graph = defaultdict(list)
        for fro, to, price in flights:
            graph[fro].append((price, to))
        
        visited = set()
        visited.add(src)

        def dfs(airport, stops, agg_price):
            nonlocal cheapest_price
            if airport == dst:
                cheapest_price = min(cheapest_price, agg_price)
                return
            if stops > k or agg_price > cheapest_price:
                return
            for next_price, next_stop in graph[airport]:
                if next_stop not in visited:
                    visited.add(next_stop)
                    dfs(next_stop, stops+1, agg_price+next_price)
                    visited.remove(next_stop)
            
        dfs(src, 0, 0)
        return cheapest_price if cheapest_price != float('inf') else -1

# graph = {
#     0: (200, 1)
#     1: (100, 2) (300, 3)
#     2: (100, 3)
# }
# airport, stops, price
# dfs(0, 0, 0)
#     dfs(1, 1, 200)
#         dfs(2, 2, 300) -> return
#         dfs(3, 2, 500)
# visited = (0, 1, 2, 3)