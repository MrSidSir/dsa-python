# Problem:
# Find index of a peak element (element greater than its neighbors).

# Real-world use:
# - Detecting high points in stock prices
# - Signal processing (finding local maxima)

def findPeak(nums):
    l, r = 0, len(nums) - 1
    
    while l < r:
        mid = (l + r) // 2
        
        # Workflow:
        # If mid element is less than its next element,
        # it means the peak lies on the right half.
        if nums[mid] < nums[mid + 1]:
            l = mid + 1
        else:
            # Otherwise, the peak is at mid or in the left half.
            r = mid
    
    # l and r converge to the peak index
    return l

# Example:
print(findPeak([1, 2, 3, 1]))  # Output: 2 (nums[2] = 3 is the peak)
print(findPeak([1, 2, 1, 3, 5, 6, 4]))  # Output could be 1 or 5 (both are peaks)
