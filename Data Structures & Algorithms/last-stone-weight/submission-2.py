class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            diff = abs(x-y)
            if diff:
                heapq.heappush(maxHeap, -diff)
        return -heapq.heappop(maxHeap) if maxHeap else 0
        