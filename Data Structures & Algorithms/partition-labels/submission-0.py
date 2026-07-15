class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        partitions = []
        ranges = {}
        
        for i, letter in enumerate(s):
            if letter not in ranges:
                ranges[letter] = [i,i]
            else:
                ranges[letter][1] = i
        
        intervals = []
        for key, interval in ranges.items():
            intervals.append(interval)
        
        intervals.sort()
        merged_intervals = []
        for i in range(len(intervals)-1):
            # (1,3) (2,4)         (1,3) (2,2)
            if intervals[i][1] > intervals[i+1][0]:
                intervals[i+1][0] = intervals[i][0]
                intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])
            else:
                merged_intervals.append(intervals[i])
        merged_intervals.append(intervals[len(intervals)-1])
        for interval in merged_intervals:
            partitions.append(interval[1]-interval[0]+1)
        return partitions    











