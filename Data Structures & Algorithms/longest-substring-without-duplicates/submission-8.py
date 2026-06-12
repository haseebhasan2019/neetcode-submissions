class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {} # char -> index
        left = 0
        right = 0
        max_window = 0
        while right < len(s):
            if s[right] in window:
                left = max(left, window[s[right]]+1)
            window[s[right]] = right
            right+=1
            max_window = max(max_window, right-left)
        return max_window
            

# abcacbc
# a
# ab
# abc
# bca
# ac
# acb
# bc