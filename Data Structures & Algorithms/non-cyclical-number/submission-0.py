class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            if n == 1:
                return True
            seen.add(n)
            string = str(n)
            n = 0
            for digit in string:
                n += pow(int(digit), 2)
        return False