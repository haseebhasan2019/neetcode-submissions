class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        tickets.sort()
        for src, dst in tickets:
            graph[src].append(dst)
        
        itinerary = []

        def dfs(src):
            while graph[src]:
                node = graph[src].pop(0)
                dfs(node)
            itinerary.append(src)
        
        dfs("JFK")
        itinerary.reverse()
        return itinerary
