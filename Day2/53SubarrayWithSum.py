# Function to find subarray with given sum using Sliding Window
def subarraySum(arr, target):
    start = 0
    curr_sum = 0

    # Loop through the array
    for end in range(len(arr)):
        curr_sum += arr[end]  # Add current element to window

        # Shrink window if current sum exceeds target
        while curr_sum > target and start <= end:
            curr_sum -= arr[start]
            start += 1

        # Check if current window matches the target sum
        if curr_sum == target:
            return (start, end)  # Return start & end index of subarray

    return -1  # No such subarray found


# Example Run
arr = [1, 4, 20, 3, 10, 5]
target = 33
result = subarraySum(arr, target)
print("Subarray found at indices:", result)

# Subarray found at indices: (2, 4)