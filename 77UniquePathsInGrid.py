def uniquePaths(m, n):
    # Initialize DP grid with 1s because there's only one way
    # to reach any cell in the first row/first column
    dp = [[1] * n for _ in range(m)]

    # Fill the DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]


# ✅ Example
print(uniquePaths(3, 7))  # Output: 28
