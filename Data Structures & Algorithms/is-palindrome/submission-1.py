class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        while start < end:
            a = s[start].lower()
            b = s[end].lower()
            if a.isalnum() and b.isalnum():
                if a != b:
                    return False
                start+=1
                end-=1
            elif a.isalnum():
                end-=1
            else:
                start+=1
        return True