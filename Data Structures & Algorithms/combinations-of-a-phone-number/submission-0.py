class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i: int, subst: str) -> List[str]:
            if len(subst) == len(digits):
                res.append(subst)
                return
            # Iterate through each letter for that digit
            digit = digits[i]
            for letter in digitToChar[digit]:
                backtrack(i+1, subst+letter)
        
        if digits:
            backtrack(0, "")
        return res