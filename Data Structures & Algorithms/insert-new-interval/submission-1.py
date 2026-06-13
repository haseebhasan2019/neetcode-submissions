class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        new_start, new_end = newInterval
        i = 0
        # Add intervals before new start
        while i < len(intervals):
            interval = intervals[i]
            if new_start > interval[1]:
                res.append(interval)
                i += 1
            else:
                break
        # Merge overlapping intervals
        while i < len(intervals):
            interval = intervals[i]
            if (interval[0] <= new_start <= interval[1] or
                interval[0] <= new_end <= interval[1]):
                new_start = min(new_start, interval[0])
                new_end = max(new_end, interval[1])
                i += 1
            elif (new_start <= interval[0] and 
                    new_end >= interval[1]):
                i += 1
                continue
            else:
                break
        res.append([new_start,new_end])
        # Add remaining intervals
        while i < len(intervals):
            res.append(intervals[i])
            i+=1
        return res