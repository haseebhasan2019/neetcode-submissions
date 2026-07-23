class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {} # Stores the min REMAINING edits per (i, j) combo

        def backtrack(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(word1):
                # insert
                memo[(i, j)] = 1 + backtrack(i, j+1)
            elif j == len(word2):
                # delete
                memo[(i, j)] = 1 + backtrack(i+1, j)
            elif word1[i] == word2[j]:
                # no op
                memo[(i, j)] = backtrack(i+1, j+1)
            else:
                insert = backtrack(i, j+1)
                delete = backtrack(i+1, j)
                replace = backtrack(i+1, j+1)
                memo[(i, j)] = 1 + min(insert, delete, replace)
            return memo[(i, j)]
        return backtrack(0, 0)


# input = current word, target word
# output = min ops to change current word into target

# ops = 
#     1. insert character
#     2. delete character
#     3. replace character

# woxxrd -> word
# deleting is more optimal than replacing
# deleting = 2
# replacing = 4

# monxkeys -> monckey
# replacing is more optimal than deleting even though there are
# more characters in the first word

# backtrack with the different decisions when the characters differ

# oat -> at
# maybe we can store matching substrings