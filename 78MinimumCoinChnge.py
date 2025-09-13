# Approach:
# DP: For each amount i, try every coin and take the minimum.
# dp[i] = min(dp[i], dp[i - coin] + 1)

def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0   # base case: 0 coins to make amount 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage
print(coinChange([1, 2, 5], 11))  # Output: 3 (11 = 5+5+1)
