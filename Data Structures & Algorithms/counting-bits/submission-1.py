class Solution:
    def countBits(self, n: int) -> List[int]:    
        def countOnes(num):
            count = 0
            for i in range(32):
                if num & 1:
                    count+=1
                num = num >> 1
            return count
        curr_num = 0
        res = []
        while curr_num <= n:
            res.append(countOnes(curr_num))
            curr_num+=1
        return res

