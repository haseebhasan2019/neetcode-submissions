class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combos = []
        curr_str = []
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(i):
            if i == len(digits):
                combos.append("".join(curr_str))
                return
            for letter in letters[digits[i]]:
                curr_str.append(letter)
                backtrack(i+1)
                curr_str.pop()
        if digits:
            backtrack(0)
        return combos
    