# 🧠 Q57. Word Break (DP + Hash Set)
# Topic: Dynamic Programming
# Real-world Use: Input parsing like breaking hashtags (#codingisfun) into valid words.

def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break
    return dp[-1]


# ✅ Example usage:
print(wordBreak("leetcode", ["leet", "code"]))  # Output: True
