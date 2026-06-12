class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        satisfied_chars = 0
        need = Counter(t)
        have = defaultdict(int)
        min_start = 0
        min_len = float('inf')

        for r in range(len(s)):
            # add r to substr map
            r_char = s[r]
            have[r_char] += 1
            if have[r_char] <= need[r_char]:
                satisfied_chars += 1

            while satisfied_chars == len(t):
                cur_len = r-l+1
                if cur_len < min_len:
                    min_len = cur_len
                    min_start = l
                l_char = s[l]
                have[l_char] -= 1
                l+=1
                if have[l_char] < need[l_char]:
                    satisfied_chars -= 1
                
        return "" if min_len == float('inf') else s[min_start:min_start+min_len]

# l = 0
# for r in range(len(s)):
#     add r to substr map
#     if valid substring: 
#         move left until just before invalid
#         minWindowSubstr = min(minWindowSubstr, substr)
#         increment left
# Can use a freqency maps to represent t and substr
