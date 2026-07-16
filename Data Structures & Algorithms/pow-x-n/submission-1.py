class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        product = 1
        for i in range(abs(n)):
            product *= x
        return product if n > 0 else 1 / product
            