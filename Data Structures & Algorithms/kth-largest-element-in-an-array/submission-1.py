class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) == k and num > heap[0]:
                heapq.heappop(heap)
            if len(heap) < k:
                heapq.heappush(heap, num)
        return heap[0]

# sort the list and iterate in range k: n log n
# heapify list and pop until we reach k -> O(n) + k * log(n)
# maintain a min heap of size k, root have the kth largest: n * log k

# [2,3,1,5,4], k = 2