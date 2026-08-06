class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int) # character -> frequency
        max_window = 0
        l = r = 0
        for r in range(len(s)):
            # add character at r
            char = s[r]
            freq[char] += 1
            # is it a valid window
            curr_window = r - l + 1
            most_freq = max(freq.values())
            # make it a valid window
            while curr_window - most_freq > k:
                removed_char = s[l]
                if freq[removed_char] == 1:
                    del freq[removed_char]
                else:
                    freq[removed_char] -= 1
                l += 1
                curr_window -= 1
                most_freq = max(freq.values())
            max_window = max(max_window, curr_window)
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