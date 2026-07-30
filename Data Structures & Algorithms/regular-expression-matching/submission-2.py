class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def chars_match(i, j):
            return s[i] == p[j] or p[j] == '.'

        def backtrack(i, j):
            # String and pattern are done
            if j == len(p):
                return i == len(s)

            # If next character in pattern is star
            if j + 1 < len(p) and p[j+1] == '*':
                # Skip entirely
                if backtrack(i,j+2):
                    return True
                # Use one or more
                if i < len(s) and chars_match(i, j):
                    return backtrack(i+1,j)
                
            # No star and characters match
            elif i < len(s) and chars_match(i, j):
                return backtrack(i+1,j+1)

            return False

        return backtrack(0,0)
"""
s = "aa", p = ".b"
bt(0,0)
    bt(1,1) -> False

s = "nnn", p = "n*"
bt(0,0)
    bt(1,0)
        bt(2,0)
            bt(3,0) -> True

s = "xyz", p = ".*z"
bt(0,0)
    bt(1,0)
        bt(2,0)
.* will steal everything until the end, need to let .* branch in different
ways - let .* branch out every time the next matching character appears
if the next character matches, start with 0 WCs, and increase +1

s = "aa" p = "a*a"
bt(0,0)


"""


"""
* = 0+ prev character
. = any character

s = uuu
p = u*n*
True


anything with .* pattern wins

s = acainewlfibsdb
p = a.*b
need to work backwards

s = axabxxcc
p = .*a.*b.*c

s = a*a.*
p = ab
TRUE
- first a* choose 0
- a is 1 (p moves forward)
- .* matches b

s = a*b
p = aaa
FALSE

s = a*b
p = b
TRUE

need to backtrack with the * character 0-n times



"""