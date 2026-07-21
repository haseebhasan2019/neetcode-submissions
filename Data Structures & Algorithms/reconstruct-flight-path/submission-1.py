class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        tickets.sort()

        for src, dest in tickets:
            graph[src].append(dest)
        
        itinerary = ["JFK"]

        def dfs(src):
            if len(itinerary) == len(tickets)+1:
                return True
            if src not in graph:
                return False
            temp_dests = list(graph[src])
            for i, next_stop in enumerate(temp_dests):
                graph[src].pop(i)
                itinerary.append(next_stop)
                if dfs(next_stop):
                    return True
                itinerary.pop()
                graph[src].insert(i, next_stop)
            return False
        dfs("JFK")
        return itinerary

# create adjacency list of src: dests, sort reverse (to pop)
# hop step by step until all edges are added (nodes = edges+1) edges = tickets

# [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
# graph = {
#     NRT: JFK
#     JFK: NRT, KUL
# }
# itinerary = JFK, HOU, JFK, SEA, JFK