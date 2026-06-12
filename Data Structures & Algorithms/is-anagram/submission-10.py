class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(ord('b') - ord('a'))
        s_ct = [0] * 26
        t_ct = [0] * 26
        for c in s:
            s_ct[ord(c) -ord('a')] += 1
        for c in t:
            t_ct[ord(c) - ord('a')] += 1
        return s_ct == t_ct