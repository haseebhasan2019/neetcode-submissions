class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remainder = 1
        for i in range(len(digits)-1,-1,-1):
            if remainder:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i]+=1
                    remainder = 0
                    break
        if remainder:
            digits.insert(0,1)
        return digits
# [9,9,9]

# start at last index
# 1+9 > 9
# change that digit to a 0
# carry a 1
# add any leftover remainder to the front of the list

# 3 0 9 9
# 3 0 9 0 remainder = 1
# 3 0 0 0 remainder = 1
# 3 1 0 0 remainder = 0

# when remainder = 0, quit return digits