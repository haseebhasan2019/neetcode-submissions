class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for c in s:
            if c in mp:
                stack.append(c)
            else:
                if not stack or c != mp[stack.pop()]:
                    return False
        return not stack
