class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums) - 1
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] == target:
                    res.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif nums[j] + nums[k] < target:
                    j+=1
                else:
                    k-=1
        return [list(tup) for tup in res]


# -1 -2 -3 1 2 3
# i for 0 ... n-3
# j for i+1 ... n-2
# k for j+1 ... n-1


# for i 0...n-3
# see if the other two digits sum to -nums[i] (target)
# n^2