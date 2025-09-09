# Problem: Search in a rotated sorted array and return the index of the target, else -1.
# Real-world use: Searching in rotated logs or circular buffers efficiently.

def search(nums, target):
    l, r = 0, len(nums) - 1
    
    # Binary search
    while l <= r:
        mid = (l + r) // 2
        
        # 1. Found target
        if nums[mid] == target:
            return mid
        
        # 2. Check if left half is sorted
        if nums[l] <= nums[mid]:
            # If target lies within the left sorted range
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            # 3. Right half is sorted
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    
    return -1


# ✅ Example run
print(search([4,5,6,7,0,1,2], 0))   # Output: 4
print(search([4,5,6,7,0,1,2], 3))   # Output: -1
print(search([1], 0))               # Output: -1
print(search([1,3], 3))             # Output: 1
