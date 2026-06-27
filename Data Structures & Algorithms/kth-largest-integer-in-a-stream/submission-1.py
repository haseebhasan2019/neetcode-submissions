class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.heap, num)
            if len(self.heap) > k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0] if self.heap else -1
        
# 1 2 3 4 5
# k = 2

# minheap of size k

# 1 2 3 3
# k = 3

# heap = [3 3 5]
# add, pop, return check head