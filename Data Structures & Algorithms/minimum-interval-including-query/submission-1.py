class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals_heap = [] # (length, end)
        sorted_queries = sorted(queries)
        intervals.sort()
        min_length = {} # query -> min length
        i = 0

        # for each query in order:
        for query in sorted_queries:
            # add valid intervals to the heap: start <= query <= end until start > query
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                heapq.heappush(intervals_heap, (end-start+1, end))
                i += 1
            # pop from heap until first valid interval, if empty return -1
            while intervals_heap:
                length, end = intervals_heap[0]
                if end < query:
                    heapq.heappop(intervals_heap)
                    continue
                min_length[query] = length
                break
            if query not in min_length:
                min_length[query] = -1
        
        return [min_length[q] for q in queries]

# Input: intervals = [[1,3],[2,3],[3,7],[6,6]], queries = [2,3,1,7,6,8]
# intervals_heap = [] # (length, end)
# sorted_queries = [1,2,3,6,7,8]
# intervals = [[1,3],[2,3],[3,7],[6,6]]
# min_length = {} # query -> min length
# i = 0

# query = 1
# heap = (3,3)
# i = 1
# min_length = {
#     1: 3
# }

# query = 2
# heap = (2,3) (3,3)
# i = 2
# min_length = {
#     1: 3
#     2: 2
# }

# query = 3
# heap = (2,3) (3,3) (5,7)
# i = 3
# min_length = {
#     1: 3
#     2: 2
#     3: 2
# }

# query = 6
# heap = (1,6) (2,3) (3,3) (5,7)
# i = 4
# min_length = {
#     1: 3
#     2: 2
#     3: 2
#     6: 1
# }

# query = 7
# heap = (5,7)
# i = 4
# min_length = {
#     1: 3
#     2: 2
#     3: 2
#     6: 1
#     7: 5
# }

# query = 8
# heap =
# i = 4
# min_length = {
#     1: 3
#     2: 2
#     3: 2
#     6: 1
#     7: 5
#     8: -1
# }

# [2,3,1,7,6,8]
# return [2,2,3,5,1,-1]

# 2 3 1 7 6 8

# q 1 2 3 6 7 8
# l 3 2 2 1 5 -1




# Q - do we need to reset the pointers through intervals and queries? intervals can be re-used. How can we avoid 
#     iterating all the way back through them

# Let's say we do need pointers through intervals and queries. How would we write this? 
# 1. for each interval, move through all the valid queries and update their min_length
# 2. then for the next interval, start only at valid queries - set this in the previous iteration

# 2 3 1 7 6 8

# q 1 2 3 6 7 8
# l 3 2 2 1 5 -1
# store this in a map, retrieve as you iterate through queries to get result via list comp

# only move the left pointer forward when end_i is too small (might have duplicate )
# l and r pointers through intervals