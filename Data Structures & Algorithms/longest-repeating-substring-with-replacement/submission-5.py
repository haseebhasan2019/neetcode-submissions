class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_window = [0] * 26
        l = 0
        r = 0
        max_len = 0
        while r < len(s):
            # Adding frequency to window
            c = s[r]
            freq_window[ord(c) - ord('A')] += 1
            # Valid window or not
            max_freq = 0
            max_freq_index = 0
            window_len = 0
            for i, freq in enumerate(freq_window):
                window_len += freq
                if freq > max_freq:
                    max_freq = freq
                    max_freq_index = i
            #Invalid window
            if window_len - max_freq > k:
                # Removing from frequency window
                char = s[l]
                char_index = ord(char) - ord('A')
                freq_window[char_index] -= 1
                l+=1
            # Compare curr len to max_len
            max_len = max(max_len, r-l+1)
            r+=1
        return max_len
