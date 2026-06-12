class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in '[{(':
                stack.append(char)
            else:
                if (len(stack)==0 or ((char == ']' and stack.pop() != '[') or 
                (char == '}' and stack.pop() != '{') or 
                (char == ')' and stack.pop() != '('))):
                    return False
        return len(stack) == 0