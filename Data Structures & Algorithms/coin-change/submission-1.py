class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [float("inf")]*(amount+1)
        arr[0] = 0
        for i in range(1,len(arr)):
            for coin in coins:
                if i >= coin and arr[i-coin] != float("inf"):
                    arr[i] = min(arr[i], arr[i-coin]+1)
        return arr[amount] if arr[amount] != float("inf") else -1