class Solution:
    def myPow(self, x: float, n: int) -> float:
        product = 1
        if n == 0:
            return 1
        if n > 0:
            for i in range(n):
                product *= x
            return product
        else:
            for i in range(-n):
                product *= x
            return 1 / product
            