class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [] # min heap with k largest at the root
        self.k = k
        for num in nums:
            self.add_to_heap(num)

    def add(self, val: int) -> int:
        self.add_to_heap(val)
        return self.heap[0]
    
    def add_to_heap(self, val):
        heapq.heappush(self.heap, val)
        # heap should always be of size k at most
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
