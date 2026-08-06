class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int) # character -> frequency
        max_window = 0
        l = r = 0
        max_freq = 0
        for r in range(len(s)):
            # add character at r
            new_char = s[r]
            freq[new_char] += 1
            max_freq = max(max_freq, freq[new_char])
            # make it a valid window
            if (r - l + 1) - max_freq > k:
                removed_char = s[l]
                freq[removed_char] -= 1
                l += 1
            max_window = max(max_window, r - l + 1)
        return max_window

# s = AAAB k = 0
# ans = 3
# k = 1
# ans = 4

# s = AABAA k = 0
# ans = 2
# k = 1
# ans = 5

# aabbba k = 2

# maintain the freq of all characters in the window

# len of window - most freq character freq ≤ k
# otherwise shift window until that is true

# keep track of max window