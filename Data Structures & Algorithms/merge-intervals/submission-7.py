class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        merged.append(intervals[0])
        for i in range(1, len(intervals)):
            new_start = intervals[i][0]
            new_end = intervals[i][1]
            # new_start will be >= prev start
            # if new_start > prev end -> add the interval
            # otherwise, merge by setting end to max of curr_end and new_end
            if new_start > merged[-1][1]:
                merged.append(intervals[i])
            else:
                merged[-1][1] = max(merged[-1][1], new_end)
        return merged
