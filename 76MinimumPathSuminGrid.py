def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Base case: starting point
    dp[0][0] = grid[0][0]

    # Fill first row (only from left)
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # Fill first column (only from top)
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # Fill rest of dp table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]


# ✅ Example
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(minPathSum(grid))  # Output: 7 (Path: 1→3→1→1→1)
