class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # consume all edges of a node and when that node has no more 
        # edges to consume, it can be added to the front of the path
        tickets.sort(reverse = True)
        graph = defaultdict(list)
        for fro, to in tickets:
            graph[fro].append(to)

        path = []
        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            path.append(airport)
        dfs("JFK")
        path.reverse()
        return path

