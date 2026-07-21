class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph = defaultdict(list)

        for src, dst in tickets:
            graph[src].append(dst)
        
        itinerary = ["JFK"]

        def dfs(src):
            if len(itinerary) == len(tickets)+1:
                return True
            temp = list(graph[src])
            for i, node in enumerate(temp):
                graph[src].pop(i)
                itinerary.append(node)
                if dfs(node):
                    return True
                itinerary.pop()
                graph[src].insert(i, node)
            return False
        dfs("JFK")
        return itinerary
