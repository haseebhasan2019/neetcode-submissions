from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(str)
        l = 0
        maxlen = 0
        for r in range(len(s)):
            if s[r] not in d:
                d[s[r]] = 1
            else:
                d[s[r]] = d[s[r]]+1
            if (r-l+1) - max(d.values()) <= k:
                maxlen = max(maxlen, r-l+1)
            else:
                d[s[l]] = d[s[l]]-1
                l+=1
        return maxlen


# left and right pointers
# keep incrementing right pointer
# longest substr will be len - most frequent char <= k
# if that condition isnt met l++ and decrement the dictionary     

# a a b 1
# a

# a b a 1
# a a a

# a b b 1
# b b b

# a b b 2
# b b b

# aabcdbaa 2
# aaaaaa

# if no not a repeat, use k's