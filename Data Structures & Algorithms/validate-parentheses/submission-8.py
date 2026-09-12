class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stk = []
        for c in s:
            if c not in mp:
                stk.append(c)
            else:
                op = mp[c]
                if not stk or op != stk.pop():
                    return False
            
        return not stk


'''
for each bracket
  push open brackets
  if close bracket
    check top of stack on close bracket, ensure it matches
map close bracket to open
 
'''