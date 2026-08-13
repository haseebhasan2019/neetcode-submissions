class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # hold a result string of size num1 + num2
        result = [0] * (len(num1) + len(num2))
        # iterate backwards through both strings
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                # accumulate the result in position i + j + 1
                result[i+j+1] += int(num1[i]) * int(num2[j])
        # iterate backwards and carry over the carry with divmod 
        print(result)
        carry = 0
        for i in range(len(result)-1,-1,-1):
            carry, result[i] = divmod(result[i] + carry, 10)
        # strip 0s
        res = "".join(map(str, result)).lstrip("0")
        return res or "0"