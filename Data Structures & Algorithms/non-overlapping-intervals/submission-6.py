class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[1]))
        last_end = intervals[0][0]
        removed = 0
        for start, end in intervals:
            if start >= last_end:
                last_end = end
            else:
                removed += 1
        return removed

'''
1,10 2,3 4,5 7,8

2 4 7 1
3 5 8 10


1,3 5,7 2,6

1 2 5
3 6 7

sort increaasing by ends, then starts
greedily choose and then skip until next valid interval

intervals=[]

[-100,-2],[1,2],[2,3],[3,4],[5,7]


'''