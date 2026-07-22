class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman-Ford O(E * k)
        prices = [float('inf')] * n
        prices[src] = 0

        # Iterate k+1 times (relaxes k+1 times)
        for _ in range(k+1):
            # Copy prices array
            temp = prices.copy()
            # Iterate through all edges and see if we can relax prices
            for fro, to, price in flights:
                if prices[fro] != float('inf'):
                    temp[to] = min(temp[to], prices[fro] + price)
            # set prices to copy
            prices = temp

        return prices[dst] if prices[dst] != float('inf') else -1

# k is the max number of stops (intermediate cities), so a valid path has up to k+1 edges. 
# Each round relaxes one edge's worth of path length, so you need k+1 rounds.
