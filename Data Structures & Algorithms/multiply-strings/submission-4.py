class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # longest length of a x b = len(a) + len(b)
        res = [0] * (len(num1) + len(num2))
        # accumulate the sums of each multiplication in their spots
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                # i+1 + j+1 - 1
                res[i+j+1] += int(num1[i]) * int(num2[j])

        # normalize the results by carrying over backwards
        for i in range(len(res)-1,-1,-1):
            carry, val = divmod(res[i], 10)
            res[i-1] += carry
            res[i] = val

        num = ''.join(map(str, res)).lstrip('0')
        return '0' if not num else num