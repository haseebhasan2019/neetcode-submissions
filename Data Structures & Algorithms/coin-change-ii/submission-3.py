class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def backtrack(i, curr_amt):
            if (i, curr_amt) in memo:
                return memo[(i, curr_amt)]
            if curr_amt == amount:
                return 1
            if i == len(coins) or curr_amt > amount:
                return 0
            total = 0
            for j in range(i, len(coins)):
                if curr_amt + coins[j] <= amount:
                    total += backtrack(j, curr_amt + coins[j])
            memo[(i, curr_amt)] = total
            return total

        return backtrack(0, 0)

# We can use backtracking to enumerate all the possible combinations then not add duplicates

# input = 
#     - list coins of different denominations
#     - a target amount
# output = number of ways to make that target amount

# in an array, keep track of the number of ways to make that amount, for each amount, iterate through coins and add up

# v 0 0 0 0 0
# i 0 1 2 3 4

# v 0 0 0 0 0
# i 0[1]2 3 4

# for coin in coins:
#     if i - coin >= 0:
#         amounts[i] += amounts[i-coin]
# v 0 1 0 0 0
# i 0 1[2]3 4

# v 1 1 2 0 0
# i 0 1 2[3]4

# v 1 1 2 4 0
# i 0 1 2 3[4]
# 3, 2+1, 1+2, 1+1+1

# v 1 1 2 4 7
# i 0 1 2 3 4

# how do we ensure no duplicate solutions - maintain the count of each denomination
# for each amount, we store the count of each coin in a 0 indexed array
# O(amount * len(coins))