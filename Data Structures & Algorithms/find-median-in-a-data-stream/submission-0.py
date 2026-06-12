class MedianFinder:

    def __init__(self):
        self.smaller_nums = [] # max_heap - negatives
        self.larger_nums = [] # min_heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smaller_nums, -num)
        heapq.heappush(self.larger_nums, -heapq.heappop(self.smaller_nums))

        if len(self.larger_nums) > len(self.smaller_nums):
            heapq.heappush(self.smaller_nums, -heapq.heappop(self.larger_nums))

    def findMedian(self) -> float:
        if len(self.smaller_nums) > len(self.larger_nums):
            return -self.smaller_nums[0]
        return (self.larger_nums[0] + 
            -(self.smaller_nums[0])) / 2
        
        