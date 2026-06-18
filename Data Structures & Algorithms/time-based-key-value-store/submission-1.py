class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.mp[key]
        l = 0
        r = len(vals) - 1
        while l <= r:
            m = (l+r) // 2
            if vals[m][0] == timestamp:
                return vals[m][1]
            elif vals[m][0] < timestamp:
                l = m+1
            else:
                r = m-1
        return "" if r == -1 else vals[l-1][1]
        
