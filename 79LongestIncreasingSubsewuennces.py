# Approach:
# DP: dp[i] = 1 + max(dp[j]) for all j < i where nums[j] < nums[i]
# O(n^2) solution

def LIS(nums):
    n = len(nums)
    if n == 0:
        return 0

    dp = [1] * n  # each element itself is a subsequence of length 1

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Example usage
print(LIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4 (LIS = [2,3,7,101])
