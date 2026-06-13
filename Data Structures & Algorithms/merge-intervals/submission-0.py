class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        i = 1
        n = len(intervals)
        prev = intervals[0]
        while i < n:
            # Can curr merge with prev?
            # If yes: update prev, no: add prev, set
            
            # prev ends before curr starts
            if prev[1] < intervals[i][0]:
                res.append(prev)
                prev = intervals[i]
            # prev ends after curr starts
            # prev starts before curr ends
            elif prev[0] <= intervals[i][1]:
                prev[0] = min(prev[0], intervals[i][0])
                prev[1] = max(prev[1], intervals[i][1])
            # prev starts after curr ends
            else:
                res.append(prev)
                prev = intervals[i]
            i+=1
        res.append(prev)
        return res