class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        prev = intervals[0]
        i = 1
        while i < len(intervals):
            # prev ends before curr starts OR prev starts after curr ends
            if prev[1] < intervals[i][0] or prev[0] > intervals[i][1]:
                res.append(prev)
                prev = intervals[i]
            # prev ends after curr starts AND prev starts before curr ends
            else:
                prev[0] = min(prev[0], intervals[i][0])
                prev[1] = max(prev[1], intervals[i][1])
            i+=1
        res.append(prev)
        return res