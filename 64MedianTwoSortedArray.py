# Problem: Find median in O(log(min(m,n))) time
# Real-Time analytics like median income calculation
# Approach: Binary search on smaller array, partitioning arrays into left/right halves

def findMedianSortedArrays(nums1, nums2):
    A, B = nums1, nums2
    if len(A) > len(B):
        A, B = B, A
    
    total = len(A) + len(B)
    half = total // 2
    
    l, r = 0, len(A) - 1
    
    while True:
        i = (l + r) // 2  # partition for A
        j = half - i - 2  # partition for B
        
        Aleft = A[i] if i >= 0 else float('-inf')
        Aright = A[i + 1] if (i + 1) < len(A) else float('inf')
        Bleft = B[j] if j >= 0 else float('-inf')
        Bright = B[j + 1] if (j + 1) < len(B) else float('inf')  # Fixed: J+1 -> j+1
        
        if Aleft <= Bright and Bleft <= Aright:  # Fixed: Alert -> Aleft
            # Correct partition found
            if total % 2:
                return min(Aright, Bright)
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2  # Fixed: //2 -> /2 and Alert -> Aleft
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1

# Example
print(findMedianSortedArrays([1, 3], [2]))  # Output: 2.0

# More test cases
print(findMedianSortedArrays([1, 2], [3, 4]))  # Output: 2.5
print(findMedianSortedArrays([0, 0], [0, 0]))  # Output: 0.0
print(findMedianSortedArrays([], [1]))  # Output: 1.0
print(findMedianSortedArrays([2], []))  # Output: 2.0