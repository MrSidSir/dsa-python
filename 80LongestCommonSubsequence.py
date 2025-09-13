# Approach:
# Classic DP
# dp[i][j] = 1 + dp[i-1][j-1] if characters match
# else dp[i][j] = max(dp[i-1][j], dp[i][j-1])

def LCS(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# Example usage:
print(LCS("abcde", "ace"))   # Output: 3 ("ace")
print(LCS("AGGTAB", "GXTXAYB"))  # Output: 4 ("GTAB")
