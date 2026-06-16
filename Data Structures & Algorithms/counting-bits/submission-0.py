class Solution:
    def countBits(self, n: int) -> List[int]:    
        def countOnes(num):
            count = 0
            for i in range(32):
                if num & 1:
                    count+=1
                num = num >> 1
            return count
        bin_num = int(bin(n)[2:])
        curr_num = int(bin(0)[2:])
        res = []
        while curr_num <= n:
            print(curr_num)
            res.append(countOnes(curr_num))
            curr_num+=1
        return res

