class Solution:
    def rob(self, nums: List[int]) -> int:
        back1, back2 = 0, 0
        for num in nums:
            back1, back2 = max(back1, num+back2), back1
        return back1
