class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                threeSum = nums[i]+nums[l]+nums[r]
                if threeSum == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                elif threeSum > 0:
                    r-=1
                else:
                    l+=1
        return res
        

# [-1,0,1,2,-1,-4]
# -4 -1 -1 0 1 2