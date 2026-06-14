class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_end = intervals[0][1]
        count = 0
        for i in range(1,len(intervals)):
            curr_start, curr_end = intervals[i]
            # No overlap
            if prev_end <= curr_start:
                prev_end = curr_end
            # Overlap
            else:
                if prev_end > curr_end:
                    prev_end = curr_end
                count += 1
        return count