class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [] # (-element, index) max heap
        maximums = []
        # Add first k elements to the heap
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        # Add max element from first window to result
        maximums.append(-heap[0][0])
        # Move the window forward until the end of the list
        for r in range(k, len(nums)):
            l = r-k
            heapq.heappush(heap, (-nums[r], r))
            while heap[0][1] <= l:
                heapq.heappop(heap)
            maximums.append(-heap[0][0])
        return maximums