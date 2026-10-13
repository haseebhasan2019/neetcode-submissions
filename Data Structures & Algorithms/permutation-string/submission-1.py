class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        freq_s1 = Counter(s1)
        freq_window = defaultdict(int)
        i = 0
        window = len(s1)
        while i < window:
            c = s2[i]
            freq_window[c] += 1
            i += 1
        if freq_s1 == freq_window:
            return True
        while i < len(s2):
            start_window = i-window
            start_char = s2[start_window]
            freq_window[start_char] -= 1
            if freq_window[start_char] == 0:
                del freq_window[start_char]
            c = s2[i]
            freq_window[c] += 1
            if freq_s1 == freq_window:
                return True
            i += 1
        return False

'''
s1 = "abc", s2 = "lecabee"
freq_s1 = {
a: 1
b: 1
c: 1
}
freq_window = {
l = 0
e = 0
c = 1
a = 1
b = 1
}


looking for a permutation of s1 in s2

maintain a freq map of our target string (s1)
maintain an active window map 
for each window, compare the two maps
space = O(26) = O(1)
time = O(len(s2) * 26)

'''