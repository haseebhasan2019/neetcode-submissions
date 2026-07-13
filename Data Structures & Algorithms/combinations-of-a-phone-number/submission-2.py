class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # map digit -> letters
        # branch out for all possible letters and append to result

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
        
        def backtrack(i, curr_str):
            if i == len(digits):
                combos.append(curr_str)
                return
            for letter in letters[digits[i]]:
                backtrack(i+1, curr_str+letter)
        if digits:
            backtrack(0, "")
        return combos
    