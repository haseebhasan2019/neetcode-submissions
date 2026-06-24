class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        gas_tank = 0
        start = 0
        for i in range(len(gas)):
            if gas_tank + gas[i] - cost[i] < 0:
                gas_tank = 0
                start = i+1
            else:
                gas_tank += gas[i] - cost[i]
        return start