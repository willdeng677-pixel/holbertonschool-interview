#!/usr/bin/python3

def makeChange(coins, total):
    # Handle edge cases where total is 0 or negative
    if total <= 0:
        return 0

    # Create a DP array initialized to a value larger than any possible coin count
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    # Build up the minimum coins required for every amount from 1 to total
    for amount in range(1, total + 1):
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], 1 + dp[amount - coin])

    # If dp[total] was never updated, the total cannot be met
    return dp[total] if dp[total] != total + 1 else -1
