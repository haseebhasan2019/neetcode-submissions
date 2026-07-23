class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        cache = {}
        def backtrack(i, j):
            if i == len(s1) and j == len(s2):
                cache[(i,j)] = True
            elif (i, j) in cache:
                return cache[(i,j)]
            elif i == len(s1):
                # compare s2
                if s2[j] == s3[i+j]:
                    cache[(i,j)] = backtrack(i, j+1)
                else:
                    cache[(i,j)] = False
            elif j == len(s2):
                # compare s1
                if s1[i] == s3[i+j]:
                    cache[(i,j)] = backtrack(i+1, j)
                else:
                    cache[(i,j)] = False
            # both indices valid
            elif s1[i] == s2[j]: # same char
                if s1[i] == s3[i+j]:
                    # branch to both
                    cache[(i,j)] = backtrack(i+1, j) or backtrack(i, j+1)
                else:
                    cache[(i,j)] = False
            elif s1[i] == s3[i+j]:
                cache[(i,j)] =  backtrack(i+1, j)
            elif s2[j] == s3[i+j]:
                cache[(i,j)] =  backtrack(i, j+1)
            else:
                cache[(i,j)] = False
            return cache[(i,j)]

        return backtrack(0, 0)

# s1 = "aaaa", s2 = "bbbb", s3 = "aabbbbaa"
# bt(0,0)
#     bt(1,0)
#         bt(2,0)


# ac, aab, aabac

# - length check
# branch decisions on s1 and s2 when they have the same next character
# save false paths to not revisit

# if we reach the end and |n-m| > 1 where n is the parts of s1 and m is the parts of s2 then return False there too
