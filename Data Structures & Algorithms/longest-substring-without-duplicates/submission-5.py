class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        right = 0
        max_window = 0
        while right < len(s):
            if s[right] not in window:
                window.add(s[right])
                right+=1
            else:
                while s[right] in window:
                    window.remove(s[left])
                    left+=1
                window.add(s[right])
                right+=1
            max_window = max(max_window, right-left)
        return max_window
            