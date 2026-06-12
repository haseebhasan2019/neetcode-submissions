class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < (len(nums)-2):
            j = i+1
            k = len(nums) - 1
            while j < k:
                total = nums[i]+nums[j]+nums[k]
                if total == 0:
                    res.append([nums[i],nums[j],nums[k]])
                if total <= 0:
                    j_num = nums[j]
                    while j<k and nums[j] == j_num:
                        j+=1
                if total >= 0:
                    k_num = nums[k]
                    while k>j and nums[k] == k_num:
                        k-=1
            i_num = nums[i]
            while i < (len(nums)-2) and nums[i] == i_num:
                i+=1
        return res
                    