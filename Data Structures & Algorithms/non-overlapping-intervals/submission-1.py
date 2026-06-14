class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        curr_i = 0
        next_i = 1
        intervals.sort()
        count = 0
        while next_i < len(intervals):
            # No overlap
            if intervals[curr_i][1] <= intervals[next_i][0]:
                curr_i = next_i
            # Overlap
            else:
                if intervals[curr_i][1] > intervals[next_i][1]:
                    curr_i = next_i
                count += 1
            next_i += 1
        return count