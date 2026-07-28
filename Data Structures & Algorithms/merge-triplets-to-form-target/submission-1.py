class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        res = [0,0,0]
        def maxify(triplet):
            maxed = []
            for i in range(3):
                maxed.append(max(triplet[i], res[i]))
            return maxed

        def valid_triplet(triplet):
            for i in range(3):
                if triplet[i] > target[i]:
                    return False
            return True
        
        for triplet in triplets:
            maxed = maxify(triplet)
            if valid_triplet(maxed):
                res = maxed
        return res == target

#  1,2 3,4 5,7 6,9 
#  target = 6,7

# target = [a,b,c]

#  select the minimal triplet with target a then b then c
#  minimal triplet means triplet where other two nums are lowest
#  and BOTH lower than or equal to target
#     if equal that takes precedence

# then see if merging all of them becomes target

# target = 30 10 20

# [30,40,50] [30,15,15] [30,5,20] [30,5,15]

# [20,10,40] [25,10,15] 