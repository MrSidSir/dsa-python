# Function to count inversions using merge sort
def merge_sort(arr):
    def merge(left, right):
        i = j = inv = 0
        res = []

        # Merge the two halves and count inversions
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                inv += len(left) - i  # All remaining elements in left are greater than right[j]
                j += 1

        # Append any remaining elements
        res += left[i:]
        res += right[j:]
        return res, inv

    # Base case
    if len(arr) <= 1:
        return arr, 0

    # Divide the array
    mid = len(arr) // 2
    left, inv1 = merge_sort(arr[:mid])
    right, inv2 = merge_sort(arr[mid:])

    # Conquer and combine
    merged, inv3 = merge(left, right)
    return merged, inv1 + inv2 + inv3

# 🔍 Real-World Use: Measures how sorted an array is.
# ✅ Example:
arr = [2, 4, 1, 3, 5]
_, inversions = merge_sort(arr)
print("Total Inversions:", inversions)

# Total Inversions: 3
