"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: (x.start, x.end))
        heap = [] # end times
        heapq.heappush(heap, intervals[0].end)
        for i in range(1, len(intervals)):
            start = intervals[i].start
            end = intervals[i].end
            # if start can come after the min end time, pop, add new end
            if start >= heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, end)
            else:
                heapq.heappush(heap, end)
        return len(heap)

