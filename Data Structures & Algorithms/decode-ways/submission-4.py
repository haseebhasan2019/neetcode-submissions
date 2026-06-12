class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        back2, back1 = 1, 1
        for i in range(1, len(s)):
            curr = 0
            # single digit
            if s[i] != '0':
                curr+=back1
            # double digit
            num = int(s[i-1:i+1])
            if 10 <= num <= 26:
                curr+=back2
            back2, back1 = back1, curr
        return back1