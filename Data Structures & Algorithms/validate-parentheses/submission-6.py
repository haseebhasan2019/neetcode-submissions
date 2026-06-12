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
                if len(stack) == 0 or mp[stack.pop()] != c:
                    return False
        return len(stack) == 0


# [] {} () [[[]]] [{()}[(){}]]