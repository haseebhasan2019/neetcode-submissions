class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # have a counter of count of people that trust this person
        # have a boolean flag array of whether this person trusts anyone
        trusters = [0] * (n+1)
        trusts = [False] * (n+1)

        for a, b in trust:
            trusters[b] += 1
            trusts[a] = True
        
        for i in range(1, n+1):
            if not trusts[i] and trusters[i] == (n-1):
                return i
        return -1



# need to find a person who trusts no one and whom everyone trusts
# can we find the town judge by ruling people out?
# 1 T
# 2 T
# 3 T
# 4 T
# [1,3]
# 1 F
# 2 T
# 3 T
# 4 T
# [4,3]
# 1 F
# 2 T
# 3 T
# 4 

