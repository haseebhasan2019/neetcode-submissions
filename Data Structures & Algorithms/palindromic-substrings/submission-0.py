class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for center in range(len(s)):
            count+=1 # single character
            left = right = center
            while right+1 < len(s) and s[right+1] == s[left]:
                right+=1
                count+=1 # duplicate chars
            while left-1 >= 0 and right+1 < len(s) and s[left-1] == s[right+1]:
                left-=1
                right+=1
                count+=1 # new palindrome
        return count