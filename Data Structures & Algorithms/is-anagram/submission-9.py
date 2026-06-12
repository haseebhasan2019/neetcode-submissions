class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ct = defaultdict(int)
        t_ct = defaultdict(int)
        for c in s:
            s_ct[c] += 1
        for c in t:
            t_ct[c] += 1
        return s_ct == t_ct