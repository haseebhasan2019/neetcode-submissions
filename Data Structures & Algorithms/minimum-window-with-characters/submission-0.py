class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        t_map = self.createMap(t)
        subst_map = defaultdict(int)
        substr = ""
        minWindowSubstr = ""

        for r in range(len(s)):
            # add r to substr map
            r_char = s[r]
            subst_map[r_char] += 1
            substr+=r_char

            if self.validSubstring(subst_map, t_map): 
                last_char = ""
                while self.validSubstring(subst_map, t_map):
                    l_char = s[l]
                    subst_map[l_char] -= 1
                    l+=1
                    last_char = substr[0]
                    substr = substr[1:]
                if len(minWindowSubstr) > len(last_char+substr) or len(minWindowSubstr) == 0:
                    minWindowSubstr = last_char+substr
        return minWindowSubstr

    def validSubstring(self, subst_map, target_map) -> bool:
        for letter, freq in target_map.items():
            if subst_map[letter] < freq:
                return False
        return True

    def createMap(self, string) -> defaultdict(int):
        mp = defaultdict(int)
        for char in string:
            mp[char] += 1
        return mp


# l = 0
# for r in range(len(s)):
#     add r to substr map
#     if valid substring: 
#         move left until just before invalid
#         minWindowSubstr = min(minWindowSubstr, substr)
#         increment left
# Can use a freqency maps to represent t and substr
