# 🪟 Q55. Minimum Window Substring (Cover All Chars)
# 🧠 Topic: Sliding Window + HashMap
# 🌍 Real-world Use: 
# Search engines or PDF readers finding the **smallest snippet** that contains all query keywords.

from collections import Counter

def minWindow(s, t):
    if not s or not t:
        return ""

    # ✅ Count required characters
    t_count = Counter(t)
    window_count = {}

    # ✅ Initialize window pointers and trackers
    have, need = 0, len(t_count)
    res = [-1, -1]
    res_len = float('inf')
    l = 0

    # ✅ Expand window with right pointer
    for r in range(len(s)):
        c = s[r]
        window_count[c] = window_count.get(c, 0) + 1

        # ✅ Check if current char count matches the required
        if c in t_count and window_count[c] == t_count[c]:
            have += 1

        # ✅ Contract window from left to shrink it
        while have == need:
            # 🎯 Update result if it's the smallest so far
            if (r - l + 1) < res_len:
                res = [l, r]
                res_len = r - l + 1

            # 🚪 Shrink from left
            window_count[s[l]] -= 1
            if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                have -= 1
            l += 1

    # ✅ Final result
    l, r = res
    return s[l:r+1] if res_len != float('inf') else ""

# 🎯 Example
result = minWindow("ADOBECODEBANC", "ABC")
print("✅ Minimum window:", result)  # Output: "BANC"


# ✅ Minimum window: BANC