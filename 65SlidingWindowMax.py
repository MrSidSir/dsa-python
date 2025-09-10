# Problem: given array and window size k, find max in each window
# Real-world use: Tracking max traffic in last k minutes
# Approach: Use deque storing indices of useful elements

from collections import deque

def maxSlidingWindow(nums, k):
    dq = deque()  # Fixed: dp -> dq
    res = []
    
    for i, n in enumerate(nums):
        # Remove indices that are out of current window
        while dq and dq[0] <= i - k:  # Fixed: dp -> dq
            dq.popleft()
        
        # Remove indices whose corresponding values are smaller than current
        while dq and nums[dq[-1]] < n:
            dq.pop()
        
        # Add current index
        dq.append(i)
        
        # If we have processed at least k elements, add result
        if i >= k - 1:  # Fixed: k -1 -> k - 1 (spacing)
            res.append(nums[dq[0]])
    
    return res  # Fixed: indentation and moved outside loop

# Example
print(maxSlidingWindow([1, 2, -1, -3, 5, 3, 6, 7], 3))  # [2, 2, 5, 5, 6, 7]

# More test cases
print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]
print(maxSlidingWindow([1], 1))  # [1]
print(maxSlidingWindow([1, -1], 1))  # [1, -1]
print(maxSlidingWindow([9, 11], 2))  # [11]