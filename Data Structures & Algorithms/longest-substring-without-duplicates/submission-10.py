class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = r = 0
        max_window = 0
        while r < len(s):
            c = s[r]
            if c in mp:
                l = max(l, mp[c] + 1)
            mp[c] = r
            r += 1
            max_window = max(max_window, r-l)
        return max_window

# abba
# l = 0, r = 0 -> 1, mw = 0 -> 1 c = a
# mp = {
#     c: 0
# }
# l = 0, r = 1 -> 2, mw = 1 -> 2 c = b
# mp = {
#     c: 0
#     b: 1
# }
# l = 0 -> 2, r = 2 -> 3, mw = 2, c = b
# mp = {
#     c: 0
#     b: 1 -> 2
# }
# l = 2, r = 3, mw = 2, c = b
# mp = {
#     c: 0
#     b: 2
# }