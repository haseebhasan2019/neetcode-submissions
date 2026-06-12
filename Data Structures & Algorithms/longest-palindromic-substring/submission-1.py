class Solution:
    def longestPalindrome(self, s: str) -> str:
        center = 0
        res = ""
        while center < len(s):
            start = center
            center+=1
            char = s[start]
            curr = char
            # Add duplicates to the curr substring
            while center < len(s) and s[center] == char:
                curr += s[center]
                center+=1
            # Check left and right of center
            left = start-1
            right = center
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr = s[left] + curr + s[right]
                left-=1
                right+=1
            # Set res to curr if it is larger
            if len(curr) > len(res): 
                res = curr
            
        return res