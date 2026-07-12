class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curr_permutation = []
        curr_set = set()
        all_permutations = []
        
        def backtrack():
            if len(curr_permutation) == len(nums):
                all_permutations.append(curr_permutation.copy())
                return
            for integer in nums:
                if integer not in curr_set:
                    curr_permutation.append(integer)
                    curr_set.add(integer)
                    backtrack()
                    curr_set.remove(integer)
                    curr_permutation.pop()
        backtrack()
        
        return all_permutations
    
# O(n*n!) time complexity - n! permutations and n time to form each permutation
# O(n) auxillary space

# iterating over n vs branching by n - line 12 prunes and stops us from branching n times