# Hashing
# Real-world use: Track login streak in apps, social media, or employee attendance
# Problem: given an unsorted array of integers, find the length of the longest consecutive element sequences
# Workflow:
# Use a set to store all elements
# For each number, if it's the start of a sequence (num-1 not in set), expand right

def longestConsecutive(nums):
    if not nums:  # Handle empty array case
        return 0
    
    num_set = set(nums)
    longest = 0

    for num in nums:
        # Check if this is the start of a sequence
        if num - 1 not in num_set:
            length = 0  # Fixed: lenght -> length (typo)
            while num + length in num_set:
                length += 1
            longest = max(longest, length)  # Fixed: moved outside while loop
    
    return longest  # Fixed: moved outside for loop

# Example
print(longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4 (1,2,3,4)

# More test cases
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9 (0,1,2,3,4,5,6,7,8)
print(longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))  # 7 (-1,0,1,3,4,5,6,7,8,9)
print(longestConsecutive([]))  # 0
print(longestConsecutive([5]))  # 1
print(longestConsecutive([1, 2, 0, 1]))  # 3 (0,1,2)