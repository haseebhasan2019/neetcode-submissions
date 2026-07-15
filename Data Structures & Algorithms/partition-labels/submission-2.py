class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        partitions = []
        last_index = {}
        
        for i, letter in enumerate(s):
            last_index[letter] = i

        partition_start = 0
        partition_end = 0
        for i, letter in enumerate(s):
            partition_end = max(partition_end, last_index[letter])
            if i == partition_end:
                partitions.append(i - partition_start + 1)
                partition_start = partition_end = i+1

        return partitions    

# "abc" -> 1,1,1
# last_index:
# a:0
# b:1
# c:2

# i = 0 -> 1
# partition_start = 0 -> 1
# partition_end = 0 -> 1
