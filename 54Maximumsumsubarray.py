# 🔍 Real-world Use Case:
# This helps in analyzing stock prices, temperature fluctuations, or sales data
# to find the best period of gain or profit (maximum continuous subarray sum).

def maxSubArray(nums):
    # ✅ Initialize max sum with the first element
    max_sum = nums[0]
    current_sum = nums[0]

    # ✅ Track subarray boundaries
    start = 0
    end = 0
    temp_start = 0

    # ✅ Traverse the array from the second element
    for i in range(1, len(nums)):
        # If starting fresh gives better sum, update current sum and temp_start
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]

        # ✅ Update max_sum and the subarray bounds if we found a new max
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    # ✅ Return max sum and the subarray contributing to it
    max_subarray = nums[start:end + 1]
    return max_sum, max_subarray


# 🎯 Example Usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, subarray = maxSubArray(arr)

print("✅ Max Sum:", max_sum)
print("📊 Max Subarray:", subarray)


# ✅ Max Sum: 6
# 📊 Max Subarray: [4, -1, 2, 1]