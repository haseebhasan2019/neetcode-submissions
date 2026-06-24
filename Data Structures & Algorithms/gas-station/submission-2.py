class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_tank = 0
        start = 0
        total = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            gas_tank += diff
            if gas_tank < 0:
                gas_tank = 0
                start = i+1
        return start if total >= 0 else -1