class Solution:
    def isHappy(self, n: int) -> bool:        
        def sum_of_squares(num):
            res = 0
            while num:
                digit = num % 10
                num //= 10
                res += digit ** 2
            return res

        slow = n
        fast = sum_of_squares(n)
        while slow != fast:
            if slow == 1 or fast == 1:
                return True
            slow = sum_of_squares(slow)
            fast = sum_of_squares(fast)
            fast = sum_of_squares(fast)
        return fast == 1
