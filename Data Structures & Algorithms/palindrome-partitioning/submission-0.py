class Solution:
    def partition(self, s: str) -> List[List[str]]:
        curr_partition = []
        total_partitions = []
        
        def valid_palindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True

        def backtrack(i):
            if i == len(s):
                total_partitions.append(curr_partition.copy())
                return
            # Can we get a valid pal from i to somewhere before the end 
            for j in range(i, len(s)):
                # are these valid palindromes [i,j]
                if valid_palindrome(i, j):
                    curr_partition.append(s[i:j+1])
                    backtrack(j+1)
                    curr_partition.pop()
        
        backtrack(0)
        return total_partitions
# aba -> 
# i = 0 j = 0 
# i = 1 j = 1
# i = 2 j = 2
# i = 3
# i = 2 j = 3x
# i = 1 j = 2
# i = 0 j = 1
# i = 0 j = 2 VALID
# curr_partition = ['aba']
# total_partitions = [['a','b','a']['aba']]

# aba -> [[a,b,a],[aba]]
# aaba -> [[a,a,b,a],[aa,b,a],[a,aba]]
# res = [[a,a,b],[aa,b]]

# abaa -> [[a,b,a,a],[a,b,aa],[aba,a]]
# curr_partition = [a,b,a,a] , [a,b,aa]

# res = [a,b]

# every letter should be added to every list
# res = list of lists - each list represents a possible partitioning
# [[c,a,t]]