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
                next_i += 1
            # Overlap
            else:
                if intervals[curr_i][1] < intervals[next_i][1]:
                    next_i += 1
                else:
                    curr_i = next_i
                    next_i += 1
                count += 1
        return count