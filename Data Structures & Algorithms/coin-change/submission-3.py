class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [float('inf')] * (amount + 1)
        arr[0] = 0

        for target in range(len(arr)):
            for coin in coins:
                if target >= coin and arr[target-coin] < float('inf'):
                    arr[target] = min(arr[target], arr[target-coin] + 1)
        return arr[amount] if arr[amount] < float('inf') else -1

# coins=[1,2,5]
# amount=11
# [0  1  1  2  2  1  2  2  3  3  2  3]
#  0  1  2  3  4  5  6  7  8  9  10 11 
# Have an array from 0 to amount where each element in the array represents the fewest number of coins needed to make that amount

# For each index in amount, iterate through all coins and make it equal to the min of that