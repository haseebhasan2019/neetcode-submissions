class Solution:
    def numDecodings(self, s: str) -> int:
        res = [] # list of strings of last number
        res = defaultdict(int) # map of num -> count
        for c in s:
            if c == '0':
                # Can it be appended
                new_res = defaultdict(int)
                for num in res: # 2, 12
                    if 0 < int(num+c) <= 26:
                        new_res[num+c] = res[num]
                if len(new_res) == 0:
                    return 0
                res = new_res
            else:
                # Can it be appended and added
                if len(res) == 0:
                    res[c] = 1
                    continue
                new_res = defaultdict(int)
                for num in res: # 2, 12
                    new_res[c] += res[num]
                    if int(num+c) <= 26:
                        new_res[num+c] = res[num]
                res = new_res
        return sum(res.values())
                    
