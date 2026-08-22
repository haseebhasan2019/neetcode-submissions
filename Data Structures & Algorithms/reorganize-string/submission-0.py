class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        # map chars to their freq and insert in max_heap
        freq_map = Counter(s)
        heap = [] # max heap - negative count

        for char, freq in freq_map.items():
            heapq.heappush(heap, (-freq, char))
        
        # at each step greedily choose the most frequent character, unless it matches most recent char
        # If there's nothing left in the heap but the most freq char then return ""
        # don't add back to the heap if freq = 0
        while heap:
            freq1, char1 = heapq.heappop(heap) #freq is negative
            if res and res[-1] == char1:
                if not heap:
                    return ""
                freq2, char2 = heapq.heappop(heap)
                res.append(char2)
                if freq2 != -1:
                    heapq.heappush(heap, (freq2 + 1, char2))
                heapq.heappush(heap, (freq1, char1))
            else:
                res.append(char1)
                if freq1 != -1:
                    heapq.heappush(heap, (freq1 + 1, char1))
        
        return "".join(res)


# need to find the most frequent character

# false case:
# aaab
# abaa x
# most frequent character >= len / 2 + 1

# aaaaabbb
# abababaa x
# a = 5
# b = 3
# 8 / 2 + 1 = 5

# aaaabcc
# a = 4
# b = 1
# c = 2
# ceiling(7 / 2) + 1 = 5

# aaabbcc
# a = 3
# b = 2
# c = 2
# abcabca

# aaaabbcc
# a = 4
# b = 2
# c = 2
# abcabcaa x

# at each step greedily choose the most frequent character, unless it matches most recent char
# heap = (4, a), (2, b), (2, c)
# a
# heap = (3, a), (2, b), (2, c)
# ab
# heap = (3, a), (2, c), (1, b)
# aba
# heap = (2, a), (2, c), (1, b)
# abac
# heap = (2, a), (1, b), (1, c)
# abaca
# heap = (1, a), (1, b), (1, c) #don't add back to the heap if freq = 0
# abacb
# heap = (1, a), (1, c)
# abacba
# heap = (1, c)
# abacbac
# heap = []