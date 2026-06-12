class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        end = len(s) - 1
        while front < end:
            if not s[front].isalnum():
                front+=1
            elif not s[end].isalnum():
                end-=1
            else:
                if s[front].lower() == s[end].lower():
                    front+=1
                    end-=1
                else:
                    return False
        return True