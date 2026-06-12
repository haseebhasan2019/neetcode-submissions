class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        for c in s:
            if c in smap:
                smap[c]+=1
            else:
                smap[c] = 1;
        for c in t:
            if c in tmap:
                tmap[c]+=1
            else:
                tmap[c] = 1;
        for key, value in smap.items():
            if key not in tmap or smap[key] != tmap[key]:
                return False
            else:
                tmap.pop(key)
        return len(tmap) == 0