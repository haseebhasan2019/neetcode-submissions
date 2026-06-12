class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        maxlen = 0
        l, r = 0, 0
        while r < len(s):
            char = s[r]
            if char not in hashset:
                hashset.add(char)
            else:
                maxlen = max(maxlen, len(hashset))
                while char in hashset:
                    hashset.remove(s[l])
                    l+=1
                hashset.add(char)
            r+=1
        return max(maxlen, len(hashset))

# Input: s = "zxyzxyz"
# Output: 3
# z
# zx
# zxy
# xyz

# Keep a hashset of the current window
# keep a maxLen int
# keep left and right pointers
# iterate through the string
# if the letter is not in the set, increase right pointer, add to set
# else, 
#     maxlen. = max(r-l, maxlen)
#     increase left pointer until letter is removed from the set




# abccba
# a
# ab
# abc
# c
# cb
# cba

