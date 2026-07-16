class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            half = helper(x, n // 2)
            return half * half * (x if n % 2 else 1)
        
        product = helper(x, abs(n))
        return product if n > 0 else 1 / product