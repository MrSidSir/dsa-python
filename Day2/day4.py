# 5. Tower of Hanoi
def hanoi(n, src, aux, dest):
    if n == 1:
        print(f"Move {n} from {src} to {dest}")
        return
    hanoi(n-1, src, aux, dest)
    print(f"Move {n} from {src} to {dest}")
    hanoi(n-1, aux, dest, src)

# Call hanoi function
hanoi(3, "A", "B", "C")

print("\n" + "="*40 + "\n")

# 10. LCS
def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0]*(n+1) for i in range(m+1)]
    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[m][n]

print(f"LCS Result: {lcs('abcde', 'ace')}")  # 3

print("\n" + "="*40 + "\n")

# 12. Knapsack
def knapsack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if wt[n-1] > W:
        return knapsack(W, wt, val, n-1)
    else:
        return max(val[n-1] + knapsack(W-wt[n-1], wt, val, n-1), 
                   knapsack(W, wt, val, n-1))

print(f"Knapsack Result: {knapsack(50, [10,20,30], [60,100,120], 3)}")  # 220


# Move 1 from A to C
# Move 2 from A to C
# Move 1 from B to A
# Move 3 from A to C
# Move 1 from B to A
# Move 2 from B to A
# Move 1 from C to B

# ========================================

# LCS Result: 3

# ========================================

# Knapsack Result: 220