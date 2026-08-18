"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [x.start for x in intervals]
        starts.sort()
        ends = [x.end for x in intervals]
        ends.sort()
        i = 0
        j = 0
        max_rooms = 0
        curr_rooms = 0
        while i < len(starts):
            if starts[i] < ends[j]:
                curr_rooms += 1
                max_rooms = max(max_rooms, curr_rooms)
                i += 1
            elif starts[i] > ends[j]:
                curr_rooms -= 1
                j += 1
            else:
                i += 1
                j += 1
        return max(max_rooms, curr_rooms)


# starts = 0 5 15
# ends = 10 20 40

# need to return the max overlapping intervals
# 1-4
# 3-6
# 4-9
# = 2
# starts = 1 3 4
# ends = 4 6 9

# keep track of the number of meetings taking place at every hour [start,end)
# return the max concurrent meetings