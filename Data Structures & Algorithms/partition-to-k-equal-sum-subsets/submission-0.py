class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        nums.sort(reverse=True)
        target = sum(nums) / k
        used = [False] * len(nums)

        def backtrack(i, k, sss) -> bool:
            if k == 0:
                return True
            if sss == target:
                return backtrack(0, k-1, 0)
            
            for j in range(i, len(nums)):
                if used[j] or nums[j] + sss > target:
                    continue
                used[j] = True
                if backtrack(j+1, k, sss + nums[j]):
                    return True
                used[j] = False
                if sss == 0:
                    return False
            return False
        
        return backtrack(0,k,0)