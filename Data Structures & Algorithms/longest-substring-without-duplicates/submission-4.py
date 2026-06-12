class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        l = 0
        r = 0
        maxLen = 0
        while r < len(s):
            while s[r] in letters:
                letters.remove(s[l])
                l+=1
            letters.add(s[r])
            r+=1
            maxLen = max(maxLen, r-l)
        return maxLen