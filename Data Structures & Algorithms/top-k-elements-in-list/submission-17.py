class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # array of frequencies
        freq_array = [[] for _ in range(len(nums)+1)]
        # dictionary of frequency
        freq_map = Counter(nums)
        for num, freq in freq_map.items():
            freq_array[freq].append(num)
        res = []
        for i in range(len(freq_array)-1,-1,-1):
            if freq_array[i]:
                res.extend(freq_array[i])
                if len(res) == k:
                    return res
        return []