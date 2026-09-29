class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [] # max heap of (-value, index)
        res = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        res.append(-heap[0][0])
        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            while heap[0][1] <= (i-k):
                heapq.heappop(heap)
            res.append(-heap[0][0])
        return res
'''
n-k+1 windows of length k
if we scan through all k items for each window it would be O((n-k+1) * k) or ~O(n*k)
if we use a heap to store the elements how do we evict the last element when we shift the window
deleting random element from a heap is O(n)
adding to a heap is O(logn)

we can do lazy deletion - only from the root, map elements to their indices

[1  2  1] 0  4  2  6        2
 1 [2  1  0] 4  2  6        2
 1  2 [1  0  4] 2  6        4
 1  2  1 [0  4  2] 6        4
 1  2  1  0 [4  2  6]       6

O(n * logn) - worst case the heap extends to be as large as n if it is strictly increasing
heap: (2,1), (1,0), (1,1)


1 2 3 4 5 6 7 8 k = 3
1 2 3|4 5 6 7 8

heap = 
3 2 1
4 3 2 1
6 5 4 3 2 1 
'''