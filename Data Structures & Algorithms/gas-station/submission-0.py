class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_tank = 0
        start = 0
        for i in range(len(gas)):
            if gas_tank + gas[i] - cost[i] < 0:
                gas_tank = 0
                start = i+1 # index out of bounds?
            else:
                gas_tank += gas[i] - cost[i]
        # every element has been checked as a start by now
        # have to iterate from 0 -> index
        for i in range(start):
            if gas_tank + gas[i] - cost[i] < 0:
                return -1
            gas_tank += gas[i] - cost[i]
        return start

#   g  1  2  3  4
#   c  2  2  4  1
#   d -1  0 -1  3
# s = 3
# gt 0 0  0  0. 3  
# s  0 1  1. 3. 3
#      2. 2. 1

# g = 3  2  1
# c = 1  3  2
# d = 2 -1 -1
# s = 0

# g = 3  2  3
# c = 2  4  2
# d = 1 -2  1
# tg. 1 -1  1
#     2  0
# keep a running total, once the total turns negative, we want to restart the start index
# but is it possible that we skip over the best starting point?

# g  4 2 9
# c  2 3 1
# tg 2 1 9