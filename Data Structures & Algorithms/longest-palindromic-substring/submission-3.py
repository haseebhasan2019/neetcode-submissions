class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        center = 0
        start = 0
        maxLen = 0

        while center < len(s):
            # Add duplicates to the curr substring
            left = center
            while center < len(s)-1 and s[center+1] == s[left]:
                center+=1
            # Check left and right of center
            right = center
            while left > 0 and right < len(s)-1 and s[left-1] == s[right+1]:
                left-=1
                right+=1
            # Set res to curr if it is larger
            if (right-left+1) > maxLen: 
                start = left
                maxLen = right-left+1
            center+=1
            
        return s[start:start+maxLen]