def trap(height):
    l, r = 0, len(height) - 1      # two pointers
    left_max = right_max = 0
    res = 0

    while l < r:
        if height[l] < height[r]:
            # Update left_max or trap water
            if height[l] >= left_max:
                left_max = height[l]
            else:
                res += left_max - height[l]
            l += 1
        else:
            # Update right_max or trap water
            if height[r] >= right_max:
                right_max = height[r]
            else:
                res += right_max - height[r]
            r -= 1
    return res

# Example
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6
