class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # O(n) approach:
        # - maintain a double ended queue of the window
        # - store the indices
        # - left is max, right is min
        # - when you insert a new element, remove all the smaller elements that came before it
        # - pop from the front until it is within the window
        # - add the front to result

        queue = deque()
        res = []
        for i, num in enumerate(nums):
            while queue and nums[queue[-1]] <= num:
                queue.pop()
            queue.append(i)
            while queue[0] < (i-k+1):
                queue.popleft()
            if i >= (k-1):
                res.append(nums[queue[0]])
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

O(n) approach:
- maintain a double ended queue of the window
- store the indices
- left is max, right is min
- when you insert a new element, remove all the smaller elements that came before it
- pop from the front until it is within the window
- add the front to result


'''