class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        merged.append(intervals[0])
        for i in range(1, len(intervals)):
            this_start = intervals[i][0]
            this_end = intervals[i][1]
            prev_end = merged[-1][1]
            if prev_end < this_start:
                merged.append(intervals[i])
            else:
                merged[-1][1] = max(merged[-1][1], this_end)
        return merged