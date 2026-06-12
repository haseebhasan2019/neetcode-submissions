class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums) - 1
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] == target:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                    while j < k and nums[k] == nums[k+1]:
                        k-=1
                elif nums[j] + nums[k] < target:
                    j+=1
                else:
                    k-=1
        return res


# -1 -2 -3 1 2 3
# i for 0 ... n-3
# j for i+1 ... n-2
# k for j+1 ... n-1


# for i 0...n-3
# see if the other two digits sum to -nums[i] (target)
# n^2