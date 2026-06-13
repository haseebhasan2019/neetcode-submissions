class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        new_start, new_end = newInterval
        i = 0
        n = len(intervals)
        # Add intervals before new start
        while i < n and new_start > intervals[i][1]:
            res.append(intervals[i])
            i += 1
        # Merge overlapping intervals
        while i < n and new_end >= intervals[i][0]:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1
        res.append([new_start,new_end])
        # Add remaining intervals
        while i < n:
            res.append(intervals[i])
            i+=1
        return res