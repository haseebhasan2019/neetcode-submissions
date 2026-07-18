class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        children = defaultdict(list) # node -> [(child, time), ...]
        nodes = [[float('inf'), None] for _ in range(n+1)] #[dist, prev]

        # create graph
        for src, dest, time in times:
            children[src].append((dest, time))

        # bfs
        q = deque()
        nodes[k][0] = 0
        q.append((k,0))
        # print(children)
        while q:
            curr_node, curr_time = q.popleft()
            print(curr_node, curr_time, children[curr_node])
            for child, child_time in children[curr_node]:
                if curr_time + child_time < nodes[child][0]:
                    nodes[child][0] = curr_time + child_time
                    nodes[child][1] = curr_node
                    q.append((child,curr_time + child_time))

        min_time = max(nodes[i][0] for i in range(1,len(nodes)))
        return min_time if min_time != float('inf') else -1

# [2,1,1],[2,3,1],[3,4,1] 
# 1
# 2: (1,1) (3,1)
# 3: 4(1)
# 4


# Input: times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1

# 1 -1-> 2

# 2 -1-> 3

# 1 -4-> 4

# 3 -1-> 4

# keep track of children AND time
# 1: (2, 1) (4, 1)
# 2: (3, 1)
# 3: (4, 1)
# 4:

# k = 1
# need to explore all paths + keep track of time
# if you reach all nodes, that is a valid path
# update min_time the resultant time from a valid path

# 1 -> 2 -> 3 -> 4 = 3 (1+1+1)
# 1 -> 4 (invalid path - not all nodes visited)

# 1: (2, 3) (3, 1) (4, 1)
# 2: (3, 1) (4, 1)
# 3: (2, 1) (4, 1)
# 4:

# 1 -> 2 -> 3 -> 4 = 3+1+1 = 5
# 1 -> 3 -> 2 -> 4 = 1+1+1 = 3 SOLUTION

