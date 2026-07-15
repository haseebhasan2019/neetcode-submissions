class Solution:
    def isHappy(self, n: int) -> bool:        
        def sum_of_squares(num):
            res = 0
            while num:
                digit = num % 10
                num //= 10
                res += digit ** 2
            return res

        l = n
        r = sum_of_squares(n)
        while l != r:
            if l == 1 or r == 1:
                return True
            l = sum_of_squares(l)
            r = sum_of_squares(r)
            r = sum_of_squares(r)
        return l == 1
