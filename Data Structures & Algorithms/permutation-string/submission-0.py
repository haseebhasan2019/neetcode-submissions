class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1 = defaultdict(int)
        map2 = defaultdict(int)
        for c in s1:
            map1[c]+=1
        start = 0
        for end in range(len(s2)):
            end_char = s2[end]
            if end < len(s1):
                map2[end_char]+=1
            else:
                start_char = s2[start]
                map2[start_char]-=1
                if map2[start_char] == 0:
                    del map2[start_char]
                start+=1
                map2[end_char]+=1
            if map1 == map2:
                return True
        return False

# O(a * b)