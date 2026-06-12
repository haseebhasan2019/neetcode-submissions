class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_window = defaultdict(int)
        l = 0
        r = 0
        max_len = 0
        max_freq = 0
        for r in range(len(s)):
            # Adding frequency to window
            freq_window[s[r]] += 1
            max_freq = max(max_freq, freq_window[s[r]])
            #Invalid window
            if (r-l+1) - max_freq > k:
                # Removing from frequency window
                freq_window[s[l]] -= 1
                l+=1
            # Compare curr len to max_len
            max_len = max(max_len, r-l+1)
        return max_len
