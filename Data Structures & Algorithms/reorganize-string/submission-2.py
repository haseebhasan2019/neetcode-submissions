class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        # map chars to their freq and insert in max_heap
        freq_map = Counter(s)
        heap = [(-freq, char) for char, freq in freq_map.items()] # max heap - negative count
        heapq.heapify(heap)
        hold = None

        # for char, freq in freq_map.items():
        #     heapq.heappush(heap, (-freq, char))
        
        # at each step greedily choose the most frequent character, unless it matches most recent char
        # If there's nothing left in the heap but the most freq char then return ""
        # don't add back to the heap if freq = 0
        while heap:
            freq1, char1 = heapq.heappop(heap) #freq is negative
            res.append(char1)
            if hold:
                heapq.heappush(heap, hold)
            if freq1 != -1:
                hold = (freq1 + 1, char1)
            else:
                hold = None
        
        return "".join(res) if not hold else ""