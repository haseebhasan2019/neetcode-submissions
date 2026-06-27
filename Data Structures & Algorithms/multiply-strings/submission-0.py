class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product = 0
        mult = 1
        for dig1 in reversed(num1):
            temp_num = 0
            temp_mult = mult
            for dig2 in reversed(num2):
                dig1_int = ord(dig1) - ord('0')
                dig2_int = ord(dig2) - ord('0')
                temp_num += temp_mult * dig1_int * dig2_int
                temp_mult *= 10
            product += temp_num
            mult *= 10
        return str(product)

#   111
# x 222
# -----
#   222
#  2220
# 22200
# 24642

# time = O(n*m)
# spce = O(min(m,n))

