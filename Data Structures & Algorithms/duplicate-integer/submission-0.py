class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = set()
        for num in nums:
            if num in ans:
                return True
            else:
                ans.add(num)
        return False