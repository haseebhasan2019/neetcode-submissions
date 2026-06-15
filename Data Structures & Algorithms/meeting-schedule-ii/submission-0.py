"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [interval.start for interval in intervals]
        ends = [interval.end for interval in intervals]
        starts.sort()
        ends.sort()
        start = 0
        end = 0
        rms = 0
        curr_rms = 0
        while start < len(starts):
            if starts[start] < ends[end]:
                curr_rms+=1
                rms = max(rms, curr_rms)
                start+=1
            elif starts[start] > ends[end]:
                curr_rms-=1
                end+=1
            else:
                start+=1
                end+=1
        return rms
