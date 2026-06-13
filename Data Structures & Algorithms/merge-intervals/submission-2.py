class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            # prev ends before curr starts
            if prev[1] < intervals[i][0]:
                res.append(prev)
                prev = intervals[i]
            # prev ends after curr starts AND prev starts before curr ends
            else:
                prev[1] = max(prev[1], intervals[i][1])
        res.append(prev)
        return res