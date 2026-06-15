"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals])
        start = end = max_rms = curr_rms = 0
        while start < len(starts):
            if starts[start] < ends[end]:
                curr_rms+=1
                max_rms = max(max_rms, curr_rms)
                start+=1
            elif starts[start] > ends[end]:
                curr_rms-=1
                end+=1
            else:
                start+=1
                end+=1
        return max_rms
