class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse = True)
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        
        itinerary = []
        def dfs(src):
            while graph[src]:
                node = graph[src].pop()
                dfs(node)
            itinerary.append(src)
        
        dfs("JFK")
        itinerary.reverse()
        return itinerary