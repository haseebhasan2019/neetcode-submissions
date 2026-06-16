class Solution:
    def countBits(self, n: int) -> List[int]:    
        def countOnes(num):
            count = 0
            for i in range(32):
                if num & 1:
                    count+=1
                num = num >> 1
            return count
        return [countOnes(i) for i in range(0,n+1)]

