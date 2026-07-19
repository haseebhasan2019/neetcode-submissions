class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        children = defaultdict(list) # node -> [(child, time), ...]

        # create graph
        for src, dest, time in times:
            children[src].append((dest, time))

        # min heap
        heap = [] # (time, node)
        heapq.heappush(heap, (0, k))
        visited = set()
        time = 0

        while heap and len(visited) < n:
            time, curr_node = heapq.heappop(heap)
            if curr_node in visited:
                continue
            visited.add(curr_node)
            for child, child_time in children[curr_node]:
                if child not in visited:
                    heapq.heappush(heap, (time + child_time, child))

        return time if len(visited) == n else -1

# times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1
# children = {
#     1: (2,1) (4,4)
#     2: (3,1)
#     3: (4,1)
#     4: 
# }
# heap (time, node) = [(3,4) (4,4)]
# time = 0 -> 1 -> 2 -> 3
# visited = 1, 2, 3, 4