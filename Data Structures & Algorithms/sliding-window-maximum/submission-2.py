class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        l = 0
        maxes = []

        for r in range(len(nums)):
            # Remove indices of elements smaller than the current num from the queue
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            # Add current index
            queue.append(r)
            # 
            if queue[0] < l:
                queue.popleft()
            if r >= k-1:
                maxes.append(nums[queue[0]])
                l+=1

        return maxes
